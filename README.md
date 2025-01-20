
# Project Setup Guide

### Step 1: Clone the Repository
1. Copy the repository URL:
   ```
   https://github.com/BrippneyVargas/Group-4-CS2450.git
   ```
2. Open your terminal and navigate to your desired folder:
   ```bash
   cd path/to/folder
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/BrippneyVargas/Group-4-CS2450.git
   ```

### Step 2: Navigate to the Project Folder
1. Change into the project directory:
   ```bash
   cd Group-4-CS2450
   ```

---

## IDE and Virtual Environment Setup

1. **Install IDE (Recommended: VS Code)(if applicable):**
   - Download and install **[Visual Studio Code](https://code.visualstudio.com/)**.
   - Install the **Python** and **GitHub** extensions in VS Code.

2. **Set Up a Virtual Environment:**
   - Install **[Anaconda](https://www.anaconda.com/products/individual)** if you don't have it already.
   - Open the Anaconda prompt, navigate to the project folder, and create a new environment:
     ```bash
     conda create --name myenv python=3.x
     conda activate myenv
     ```
     Replace `3.x` with the version of Python you want to use.

3. **Configure VSCode with Your Virtual Environment:**
   - In VS Code, press `Ctrl+Shift+P` and select **Python: Select Interpreter**.
   - Choose the `myenv` environment from the list.

4. **Install Python Dependencies:**
   - Install required packages using:
     ```bash
     conda install --file requirements.txt
     ```
     (Currently empty, but will include dependencies in the future.)
---

## Version Control Operations

Avoid making changes directly to the `main` branch. Create a new branch instead.

1. **Create a New Branch:**
   ```bash
   git checkout -b new-branch-name
   ```

2. **Make Changes & Commit:**
   - Modify any file in the project.
   - Stage and commit your changes:
     ```bash
     git add .
     git commit -m "Your commit message"
     ```

3. **Push Changes to the Repository:**
   - Push your changes to the remote repository:
     ```bash
     git push origin new-branch-name
     ```

4. **Pull the Latest Changes:**
   - Before working, always pull the latest updates:
     ```bash
     git pull origin main
     ```

---

## Project Management Tool

We will use **GitHub Project** for task and milestone management, and **Schej.it** for scheduling meetings

---

## Team Roles and Responsibilities

- **Team Member 1:** 
- **Team Member 2:**
- **Team Member 3:** 

---


