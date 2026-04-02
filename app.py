"""
Pumping Lemma Visual Lab — Flask Backend
A web app demonstrating the Pumping Lemma for Regular Languages.
"""

from flask import Flask, render_template, request
import re
import os

app = Flask(__name__)

# ─── Predefined Example Languages ──────────────────────────────────────────────

EXAMPLES = [
    {
        "id": "0n1n",
        "name": "L = { 0ⁿ1ⁿ | n ≥ 1 }",
        "description": "Equal number of 0s followed by equal number of 1s",
        "sample": "000111",
        "pumping_length": 3,
        "tooltip": "Classic non-regular language. Any split pumps extra 0s, breaking the 0ⁿ1ⁿ balance."
    },
    {
        "id": "anbn",
        "name": "L = { aⁿbⁿ | n ≥ 1 }",
        "description": "Equal number of a's followed by equal number of b's",
        "sample": "aaabbb",
        "pumping_length": 3,
        "tooltip": "Pumping y (within the a-prefix) adds more a's than b's → contradiction."
    },
    {
        "id": "ww",
        "name": "L = { ww | w ∈ {a,b}* }",
        "description": "String that is a repetition of some substring",
        "sample": "abcabc",
        "pumping_length": 3,
        "tooltip": "Pumping disrupts the exact duplication required by ww."
    },
    {
        "id": "palindrome",
        "name": "L = { w | w is a palindrome over {a,b} }",
        "description": "Strings that read the same forwards and backwards",
        "sample": "aabbaa",
        "pumping_length": 3,
        "tooltip": "Pumping within one side of the palindrome destroys symmetry."
    },
    {
        "id": "prime_length",
        "name": "L = { aⁿ | n is prime }",
        "description": "Strings of a's whose length is a prime number",
        "sample": "aaaaaaa",
        "pumping_length": 3,
        "tooltip": "Pumping can produce strings of non-prime length → contradiction."
    },
]

# ─── Language Checkers ─────────────────────────────────────────────────────────

def check_language(lang_id, string):
    """Check if a string belongs to the specified language."""
    if lang_id == "0n1n":
        match = re.fullmatch(r'(0+)(1+)', string)
        if not match:
            return False
        return len(match.group(1)) == len(match.group(2))

    elif lang_id == "anbn":
        match = re.fullmatch(r'(a+)(b+)', string)
        if not match:
            return False
        return len(match.group(1)) == len(match.group(2))

    elif lang_id == "ww":
        n = len(string)
        if n % 2 != 0:
            return False
        half = n // 2
        return string[:half] == string[half:]

    elif lang_id == "palindrome":
        return string == string[::-1]

    elif lang_id == "prime_length":
        n = len(string)
        if n < 2:
            return False
        if not all(c == 'a' for c in string):
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Default: unknown language — no contradiction detection
    return None


def decompose_string(string, pumping_length):
    """
    Decompose string w into x, y, z such that:
      - |xy| ≤ p
      - |y| > 0
    We choose y to be as large as possible within the constraint.
    """
    p = min(pumping_length, len(string))
    if p <= 0:
        return "", "", string

    # y occupies positions [0..p-1] minus at least one char for potential x
    # Standard choice: x = s[0:0] = "", y = s[0:p], z = s[p:]
    # But better to show a nontrivial split: x = s[0:1], y = s[1:p], z = s[p:]
    # If p == 1, then x = "", y = s[0:1], z = s[1:]
    if p == 1:
        x = ""
        y = string[0:1]
        z = string[1:]
    else:
        x = string[0:1]
        y = string[1:p]
        z = string[p:]

    return x, y, z


def pump_string(x, y, z, pump_count):
    """Generate pumped string xy^i z."""
    return x + (y * pump_count) + z


# ─── Routes ────────────────────────────────────────────────────────────────────

@app.route("/", methods=["GET"])
def index():
    """Render the main page with default state."""
    return render_template(
        "index.html",
        examples=EXAMPLES,
        string="",
        pumping_length=2,
        pump_count=1,
        selected_example="",
        result=None,
    )


@app.route("/pump", methods=["POST"])
def pump():
    """Process the pumping request and return results."""
    string = request.form.get("string", "").strip()
    pumping_length = int(request.form.get("pumping_length", 2))
    pump_count = int(request.form.get("pump_count", 1))
    selected_example = request.form.get("selected_example", "")
    action = request.form.get("action", "pump")

    # Handle example loading
    if action == "load_example" and selected_example:
        example = next((e for e in EXAMPLES if e["id"] == selected_example), None)
        if example:
            string = example["sample"]
            pumping_length = example["pumping_length"]
            pump_count = 1

    # Handle reset
    if action == "reset":
        return render_template(
            "index.html",
            examples=EXAMPLES,
            string="",
            pumping_length=2,
            pump_count=1,
            selected_example="",
            result=None,
        )

    # Handle pump increment/decrement
    if action == "pump_up":
        pump_count = min(pump_count + 1, 10)
    elif action == "pump_down":
        pump_count = max(pump_count - 1, 0)

    result = None
    if string:
        x, y, z = decompose_string(string, pumping_length)
        pumped = pump_string(x, y, z, pump_count)

        # Build explanation steps
        steps = [
            {
                "title": "Original String (w)",
                "value": string,
                "detail": f"Length |w| = {len(string)}"
            },
            {
                "title": "Pumping Length (p)",
                "value": str(pumping_length),
                "detail": f"We choose p = {pumping_length}"
            },
            {
                "title": "Decomposition",
                "value": f'x = "{x}", y = "{y}", z = "{z}"',
                "detail": f"|xy| = {len(x) + len(y)} ≤ {pumping_length} ✓  |  |y| = {len(y)} > 0 ✓"
            },
            {
                "title": f"Pumped String (xy{superscript(pump_count)}z)",
                "value": pumped,
                "detail": f"Length = {len(pumped)} (i = {pump_count})"
            },
        ]

        # Check contradiction
        contradiction = None
        lang_name = ""
        if selected_example:
            example = next((e for e in EXAMPLES if e["id"] == selected_example), None)
            if example:
                lang_name = example["name"]
                belongs = check_language(selected_example, pumped)
                original_belongs = check_language(selected_example, string)
                if belongs is not None:
                    if original_belongs and not belongs:
                        contradiction = {
                            "found": True,
                            "message": f'"{pumped}" ∉ {lang_name}',
                            "explanation": f"The pumped string violates the language pattern. Since we found an i = {pump_count} where xy^i z ∉ L, this is a contradiction!"
                        }
                    elif not original_belongs:
                        contradiction = {
                            "found": None,
                            "message": f'Original string "{string}" ∉ {lang_name}',
                            "explanation": "The original string doesn't belong to the language. Try a valid string."
                        }
                    else:
                        contradiction = {
                            "found": False,
                            "message": f'"{pumped}" ∈ {lang_name}',
                            "explanation": f"The pumped string still satisfies the language conditions for i = {pump_count}. Try pumping more!"
                        }

        result = {
            "x": x,
            "y": y,
            "z": z,
            "pumped": pumped,
            "pump_count": pump_count,
            "steps": steps,
            "contradiction": contradiction,
            "original_chars": list(string),
            "x_len": len(x),
            "y_len": len(y),
            "z_len": len(z),
            "pumped_chars": list(pumped),
            "pumped_x": x,
            "pumped_y": y * pump_count,
            "pumped_z": z,
        }

    return render_template(
        "index.html",
        examples=EXAMPLES,
        string=string,
        pumping_length=pumping_length,
        pump_count=pump_count,
        selected_example=selected_example,
        result=result,
    )


def superscript(n):
    """Return Unicode superscript for a number."""
    sup_map = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    return str(n).translate(sup_map)


# ─── Entry Point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(debug=True, host="0.0.0.0", port=port)
