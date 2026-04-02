# 🚀 Instructions to Run: Pumping Lemma Visual Lab

This document explains how anyone (your friends, classmates, or professors) can run and interact with the Pumping Lemma Visual Lab project on their own computers or phones!

There are three ways to share this project depending on whether they are just clicking a link or running the code themselves.

---

## Option 1: Share a Live Link (No installation needed! Recommended)

The absolute easiest way to share the lab is to deploy it to the internet using **Render**. Once deployed, anyone can access it via a URL, even on their phones!

### How to do it:

1. Create a free account on [GitHub](https://github.com/) and upload this entire project folder to a new repository.
2. Create a free account on [Render.com](https://render.com/).
3. On Render's dashboard, click **New+** -> **Blueprint** or **Web Service**.
4. Connect your Render account to your GitHub repository and select the `pumping-lemma-lab` repo.
5. Render will automatically detect the `render.yaml` file, install dependencies, and launch the server.
6. Once deployed, Render will give you a public URL like `https://pumping-lemma-lab.onrender.com`. Just text/email that link to your friends!

---

## Option 2: Send the ZIP File (Easiest local setup)

If you don't want to host it online, you can just send the code files directly.

### What you need to do:

1. Right-click the `pumping-lemma-lab` folder on your computer and select "Compress to ZIP file".
2. Send that `.zip` file via email, WhatsApp, or Google Drive.

### What your friend needs to do:

1. Extract/Unzip the folder on their laptop.
2. Ensure they have [Python](https://www.python.org/downloads/) installed.
3. Open their terminal (Command Prompt/PowerShell), navigate into the folder, and run these commands:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
4. Open a web browser and go to: `http://localhost:5050/`

---

## Option 3: Via GitHub Clone (For Developer Friends)

If your friend is a developer or knows how to use Git, they can clone the code directly from your repository.

### What you need to do:

1. Upload this folder to a public GitHub repository.
2. Send them the link to the repository.

### What your friend needs to do:

They simply need to open their terminal and run these commands in order:

```bash
# Clone the repository
git clone https://github.com/your-username/pumping-lemma-lab.git

# Enter the directory
cd pumping-lemma-lab

# Install the required Flask packages
pip install -r requirements.txt

# Run the app
python app.py
```

After the server starts, they can view the lab by going to `http://localhost:5050/` in their browser.
