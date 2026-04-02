# 🔬 Pumping Lemma Visual Lab

An interactive web simulation for demonstrating the **Pumping Lemma for Regular Languages** — a core concept in the Theory of Computation.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![Deploy](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render)

---

## 🎯 What It Does

Enter a string, set a pumping length, and watch the app:

1. **Decompose** the string into **x**, **y**, **z** (satisfying |xy| ≤ p, |y| > 0)
2. **Visualize** each character as colored boxes — blue (x), orange (y), grey (z)
3. **Pump** the y-segment (y → y² → y³ …) with animated transitions
4. **Detect contradictions** — if the pumped string leaves the language, it proves the language is **not regular**

## ✨ Features

- 🎨 **Modern UI** — Light canvas background, dark navy sidebar, glassmorphism-inspired cards
- 📚 **5 Predefined Examples** — 0ⁿ1ⁿ, aⁿbⁿ, ww, palindromes, prime-length strings
- 🔬 **Step-by-Step Explanation** — Decomposition, length conditions, pumped result
- 💥 **Contradiction Detection** — Visual alerts when pumped string violates the language
- ℹ️ **Tooltips** — Hover for theory explanations
- 📱 **Responsive** — Works on desktop and mobile

## 🛠️ Tech Stack

| Layer    | Technology     |
| -------- | -------------- |
| Backend  | Python + Flask |
| Frontend | HTML + CSS     |
| Server   | Gunicorn       |
| Hosting  | Render         |

## 📁 Project Structure

```
pumping-lemma-lab/
├── app.py                 # Flask app — routes, pumping logic, language checkers
├── templates/
│   └── index.html         # Full UI — HTML + inline CSS + minimal JS
├── requirements.txt       # Python dependencies
├── render.yaml            # Render deployment config
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/pumping-lemma-lab.git
cd pumping-lemma-lab

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Open in browser
# → http://localhost:5050
```

## 🌐 Deploy on Render

### Option A: Auto-deploy with `render.yaml`

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → **New** → **Blueprint**
3. Connect your GitHub repo
4. Render auto-detects `render.yaml` and deploys

### Option B: Manual setup

1. Go to [render.com](https://render.com) → **New** → **Web Service**
2. Connect your GitHub repo
3. Set the following:
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Click **Deploy**

## 🎨 Color Palette

| Color          | Hex       | Usage                     |
| -------------- | --------- | ------------------------- |
| Primary Orange | `#F97316` | Buttons, highlights, CTAs |
| Secondary Blue | `#2563EB` | Secondary actions, links  |
| Dark Blue      | `#1E3A8A` | Top navbar background     |
| Navy Dark      | `#0F172A` | Sidebar / examples card   |
| Light BG       | `#F4EDE2` | Main canvas background    |

## 📖 Theory Background

The **Pumping Lemma** states that for any regular language L, there exists a pumping length p such that any string w ∈ L with |w| ≥ p can be split into w = xyz where:

- |xy| ≤ p
- |y| > 0
- For all i ≥ 0, xy^i z ∈ L

If we can find a string where pumping produces a string **outside** the language, we have a **contradiction**, proving the language is **not regular**.

---

Built with 🧡 for Theory of Computation
