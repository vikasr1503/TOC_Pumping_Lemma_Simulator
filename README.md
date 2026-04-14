# Pumping Lemma Simulator

An interactive web-based tool to simulate and visualize the **Pumping Lemma** for both Regular and Context-Free Languages — built as part of my Theory of Computation (TOC) coursework.

---

## Why I built this

This started as an assignment for my TOC course (CSE core). The pumping lemma is one of those concepts that looks straightforward on paper but gets slippery fast when you're actually trying to apply it — especially figuring out how to pick the decomposition, why certain strings fail, and what "all values of i" actually means in practice.

I could've put together something minimal just to submit. But somewhere along the way I thought — if I'm already doing this, why not build it properly? Going through the full thing by myself (HTML, CSS, JS — no frameworks, no libraries) turned out to be a good way to actually sharpen those basics, which I'd been meaning to do for a while.

So it became two things at once: an assignment I could be proud of, and a personal exercise in building something functional from scratch.

---

## What it does

- **Regular Language checker** — Tests whether a given string can be pumped according to the pumping lemma for regular languages, with step-by-step decomposition into `xyz`
- **Context-Free Language checker** — Handles CFL pumping lemma logic with `uvxyz` decomposition
- Lets you input custom strings and languages and walks through each condition interactively
- Visual feedback for each pumping attempt — so you can see exactly where and why a string fails or passes
- Clean, responsive UI that works on desktop and mobile

---

## Tech stack

Vanilla HTML, CSS, and JavaScript — no frameworks, no build tools. Just the browser.

I deliberately kept it dependency-free. Part of the point was to get comfortable with the fundamentals without leaning on abstractions.

---

## Live demo

Deployed on Render: [TOC Pumping Lemma Simulator](https://toc-pumping-lemma-simulator-1.onrender.com/)

---

## Running locally

No setup needed.

```bash
git clone https://github.com/vikasr1503/TOC_Pumping_Lemma_Simulator.git
cd TOC_Pumping_Lemma_Simulator
```

Then just open `index.html` in your browser. That's it.

---

## Project structure

```
TOC_Pumping_Lemma_Simulator/
├── index.html        # Entry point and layout
├── style.css         # Styling and responsive layout
├── script.js         # Core simulation logic
└── README.md
```

---

## Concepts covered

- Pumping Lemma for Regular Languages
- Pumping Lemma for Context-Free Languages
- String decomposition and pumping conditions
- Formal language theory (CSE / TOC)

---

## Course context

**Subject:** Theory of Computation (TOC)
**Branch:** Computer Science Engineering (CSE Core)

---

## Notes

This isn't a research tool — it's a learning aid. The goal was to make the pumping lemma less abstract for students (including myself) who are seeing it for the first time. If you're studying TOC and find this useful, that's exactly what it was meant for.

Feedback and suggestions are welcome — open an issue or just drop a message.
