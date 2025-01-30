# Project Setup Guide

## Step 1: Clone the Repository

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

---

## Step 2: Navigate to the Project Folder

1. Enter the project directory:
   ```bash
   cd Group-4-CS2450
   ```

---

## IDE and Virtual Environment Setup

### 1. Install an IDE (Recommended: VS Code)

- Download **[VS Code](https://code.visualstudio.com/)**.

- Install the **Python** and **GitHub** extensions from the VS Code marketplace.

---

### 2. Add Conda to PATH (If Applicable)

#### Windows:

1. Locate Conda’s installation folder (e.g., `C:\Users\<YourUsername>\Anaconda3`).

2. Search for "Environment Variables" in the Start menu.

3. Edit the `Path` variable under System Variables and add:

   - `<Conda_Install_Dir>\Scripts`
   - `<Conda_Install_Dir>\condabin`

4. Save the changes.

#### Mac/Linux:

1. Open your terminal and edit the appropriate shell config file (e.g., `~/.bashrc`):

   ```bash
   nano ~/.bashrc
   ```

2. Add the line:
   ```bash
   export PATH="<Conda_Install_Dir>/bin:$PATH"
   ```
3. Save the file and run:
   ```bash
   source ~/.bashrc
   ```

#### Verify:

Run the following to check if Conda is added to PATH:

```bash
conda --version
```

---

### 3. Set Up a Virtual Environment

1. Install **[Anaconda](https://www.anaconda.com/products/individual)** if not already installed.

<<<<<<< HEAD
2. Create and activate a new environment:
=======
Vlad Kashchuk: Developer/tester 
>>>>>>> a0b8ef64a1f2f1ea16a8ef0b11693a774f1403f3

   ```bash
   conda create --name myenv python=3.x
   conda activate myenv
   ```

   Replace `3.x` with the desired Python version.

<<<<<<< HEAD
3. Install dependencies:
   ```bash
   conda install --file requirements.txt
   ```
=======
Jacob West: Recorder 

Devin Winters: Product Owner 


## Workflow and Tool Usage 

Version Control Tool: GitHub 

Purpose: Code repository, collaboration, and version tracking. 

Workflow: Each feature or fix is developed on a branch, reviewed via pull requests, and merged into the main branch after approval. 
>>>>>>> a0b8ef64a1f2f1ea16a8ef0b11693a774f1403f3

---

### 4. Configure VS Code with Virtual Environment

1. Open VS Code and press `Ctrl+Shift+P`.

2. Select **Python: Select Interpreter** and choose `myenv`.

---

## Version Control Workflow

### 1. Create a New Branch

```bash
git checkout -b your-branch-name
```

### 2. Commit Changes

1. Stage your changes:
   ```bash
   git add .
   ```
2. Commit with a message:
   ```bash
   git commit -m "Your commit message"
   ```

### 3. Push Changes

```bash
git push origin your-branch-name
```

### 4. Pull Latest Updates

```bash
git pull origin main
```

---

## Team Members and Roles

- **Uladzislau Kashchuk**: Developer/Tester
- **Keomony Mary**: Developer/Tester
- **Brippney Vargas**: Scrum Master
- **Jacob West**: Recorder
- **Devin Winters**: Product Owner

---

## Workflow Tools

### 1. **Version Control**

<<<<<<< HEAD
- **Tool**: GitHub

- **Purpose**: Code repository, collaboration, and version tracking.

- **Workflow**: Use branches and pull requests for development and merge after reviews.

### 2. **Task Management**

- **Tool**: GitHub Projects

- **Purpose**: Track tasks, assign responsibilities, and monitor progress.

- **Workflow**: Break tasks into actionable items and organize them under milestones.

### 3. **Communication**

- **Tool**: Microsoft Teams

- **Purpose**: Communication, video calls, and updates.

- **Workflow**: Daily stand-ups and asynchronous discussions.

### 4. **Scheduling Meetings**

- **Tool**: When2Meet

- **Purpose**: Coordinate team availability for meetings.

- **Workflow**: Input availability and determine the best time slot for everyone.
=======
 
>>>>>>> a0b8ef64a1f2f1ea16a8ef0b11693a774f1403f3
