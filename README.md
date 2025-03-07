# How To Run The Program

To run the application, execute:
- ```python3 app.py``` OR ```python app.py``` (FROM terminal or command prompt)
- excute the app.py (from IDE)

# Project Setup Guide

### Step 1: Clone the Repository
2. Open your terminal and navigate to your desired folder:
   ```bash
   cd path/to/folder
   ```
3. Clone the repository:
   ```bash
   git clone git@github.com:BrippneyVargas/Group-4-CS2450.git
   ```

### Step 2: Navigate to the Project Folder
   ```bash
   cd Group-4-CS2450
   ```
   
### Step 3: Switch to dev branch
   ```bash
   git switch dev
   ```
   
### Step 4: Create a Python virtual environment
   ```bash
   python3 -m venv ./ 
   ```
   If you want to install it directly in the folder you are currently in, otherwise provide a different directory name.
   IMPORTANT: If you intstall it elsewhere and not inside Group-4-CS2450, make sure you're updating the same requirements.txt located inside the Group-4-CS2450.

### Step 5: Switch to virtual environment
mac/linux:
   ```bash
   source bin/activate
   ```
windows:
   ```bash
   bin/activate
   ```
   Assumng you installed VE directly inside Group-4-CS2450, otherwise provide the correct path.
   
### Step 5: Install required dependecies
   ```bash
   pip install -r requirements.txt
   ```
   Assuming you are inside Group-4-CS2450.

### Step 6: Run the fastAPI server
   ```bash
   fastAPI dev Task_manager_app/src/main.py
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

## Team members' roles and responsibilities.


Vlad Kashchuk: Developer/tester 

Keomony Mary: Developer/tester 

Brippney Vargas: Scrum Master 

Jacob West: Recorder 

Devin Winters: Product Owner 


## Workflow and Tool Usage 

Version Control Tool: GitHub 

Purpose: Code repository, collaboration, and version tracking. 

Workflow: Each feature or fix is developed on a branch, reviewed via pull requests, and merged into the main branch after approval. 

---

Task Management:

Tool: GitHub Projects

Purpose: Tracks tasks, assigns responsibilities, sets deadlines, and monitors progress to ensure efficient collaboration and project completion.

Workflow: Tasks are divided into actionable items under milestones, providing a clear structure for achieving specific goals within the project timeline.

---

Communication: 

Tool:  Microsoft Teams 

Purpose: Quick communication, videocalls meetings, and updates. 

Workflow: Daily stand-ups and asynchronous discussions. 

---

Schedule Meeting:

Tool: When2Meet

Purpose: Identifies team members' availability to streamline scheduling and find the most convenient time for everyone.

Workflow: Team members input their availability into the tool, which generates an overview to determine the best meeting time based on the overlap of available slots.


 
