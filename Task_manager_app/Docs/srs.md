## SRS Document

### Functional Requirements:

- The system allows users to add tags to their tasks, making it easier to filter and view them later. For example, users can tag tasks with labels such as className, groupWork, research, or quiz to organize and quickly access related tasks.
- The system allows users to set priority for each of their tasks.
- The system will send a reminder if the task approaches the deadline, if users enable it.
- The system allows users to view a specific number of tasks per page.
- The system allows users to delete a task.
- The system allows users to save and load tasks using JSON.
- The system allows users to update the task’s status (to-do, in-progress and completed).
- The system allows users to search for a task.
- The system can count the total number of tasks, or filter the count to show only to-do tasks, in-progress tasks, or completed tasks.
- The system will notify the user if the same task title is added.

  #### GUI:

  - The systems displays the task to the screen automatically once the task is succesfully added.
  - Tasks and task lists are displayed in tabular mode.
  - The 'edit' and 'delete' button is in-line with the task for easier navigation.
  - The system allows mulitple tasks adding.
  - The system has the button 'Save Tasks' on top if user wants to save their added tasks into json file and dowload into a local machine.
  - The system has the the button 'Load Tasks' for user to load their json file.
  - The system provides user with task title in the Title box.
  - The system provides Description box for user to enter detail information related to their tasks.
  - The system has three radio buttons for user to select the priority level of their tasks.
  - Priority level is color coded (High= red, Medium= orange, Low=yellow)
  - The interface places the 'Add Task' button at the end, creating a natural flow where users can input all details first and then simply save and complete the process.

### Non-Functional Requirements:

- The system must load tasks from a SQL database within 0.1 seconds
- Task creation/modification operations must complete within 0.5 seconds
- Ensure privacy and security, such as user authentication.
- Task deletion operations must complete within 0.3 seconds.
- Search and filter operations must return results within 0.2 seconds.
- Simple but aesthetic interface that is user-friendly and easy to navigate.
- The system should load the dashboard within 2 seconds.
- The response time for adding, updating, or deleting tasks should be less than 1 second.
- The application should be designed to scale horizontally to accommodate increasing users and tasks.
- The system must support both light and dark themes.
- The interface must be responsive across different screen sizes.
- The system shall delete the task once the 'delete' button has been clicked only once.
- The system shall response to delete task within 1 second.
- The interface should allow multiple pages that correlate with each other.

### Use Cases and User Stories:

- User Stories:

  1. As an impulsive person, I want to be able to recover tasks that I deleted within a set time period in case I want to recover something I should not have deleted. (Story point = 6)

  2. As a person who gets lost in my notes if they are not organized, I would like to be able to label my tasks. Tagging something as pertaining to school or work will hopefully help me stay on track and not get lost in an avalanche of notes.

  3. As a person who gets overwhelmed, I would like to not have all my notes in one place. Instead, I would like them to be divided into different folders or pages by type. This will make the app a lot more usable for me. (Story point = 7)

  4. As a person who tends to ignore a lot of my phone notifications, I would like to be able to decide the priority of tasks I make and how I am reminded of tasks of varying priority. This will help me not ignore more important tasks. (Story point = 4)

  5. As a person who uses their phone too much at night, I would like to be able to set the app to use a light or dark theme, or to default to my device's settings. This will make my experience using the app at varying times of day more enjoyable. (Story point = 2)

  6. As a person who values customization and visual learning, I would like to be able to change the colors of each task I create. This will help me more quickly identify which task I want to find. (Story point = 2)

  7. As a user, I want to add notes to tasks so I can keep additional details for each task. (story point = 1)

  8. As a user, I want to make my tasks private but also enable sharing if I want to. (story point = 8)

  9. As a user who wants to feel accomplished, I want to be able to mark a task as complete. This will allow me to know what I have done and still have yet to do in a given day. (Story point = 3)

  10. As a busy person, I want an app that loads quickly and experiences few performance hiccups. This will help me be more efficient with my time. (Story point = 7)

  11. As a person whose eyesight is worsening, I would like to be able to change the size of the font inside the app. This will lessen the strain on my eyes. (Story point = 2)

  12. As a normal person, I want an app with few visual glitches and bugs. I want something pleasing to look at and that will not delete my tasks. My day would go a whole lot better that way. (Story point = 8)

  13. As a person who speaks multiple languages, I would like to be able to change the language the app uses. This will make it easier when I forget what a certain button does. (Story point = 9)

  14. As a person who forgets to lock the door when I leave work, I would like to be able to remind myself to do so when I get too far from where I work. This would help me not get in trouble with security. (Story point = 10)
  15. As a user, I want the system to notify me if I add duplicate tasks (task with the same title). (Story point = 2)
  16. As a person who has to take medication at the same time every day, I want repeatable reminders (series) that I can define the timeframe of so I do not have to repeatedly set the same reminders. (Story points: 5)

- Use Cases to reflect implemented featues:

  - Primary Actor: student, admin
  - Student: Use Case 1: Add Task

    - Description: Allows students to add new tasks to the system
    - Main Flow:
      - Student initiates “Add Task” function
      - Student enters basic task details
    - Choose the tags (optional)
      - System prompts for tags before saving
      - Student can add tags for their tasks:
        - exam
        - assignments
        - labworks
        - quizzes
        - Group projects
        - Research etc
        - Student can add multiple tags to categorize task
    - Priority Setting (optional): student can choose to set a priority level for each task
      - High Priority
      - Medium Priority
      - Low priority
    - System saves the task
    - System notifies once the task is added successfully.

  - Student: Use Case 2: View Task

    - Description: Enables students to view tasks
    - Main Flow:
      - Students accesses “View Tasks”
      - System displays organized task list
      - Student can filter by categories
      - System displays the number of tasks per page.

  - Student: Use Case 3: Delete Task
    - Description: Enables students to delete the tasks
      - Main Flow:
        - Student selects task to delete
        - System checks for existing task
        - System processes deletion
        - Extension points:
          - Error Handling:
            - Shows error if no task exists
            - Provide recovery options
            -
  - Admin: Use Case 1: Access System Settings
    - Description: Manage system settings and task priorities
    - Main Flow:
      - If users enable it, the reminders will pop up to alert user if deadline of a specific task is approaching.

- Add user stories for edge cases or additional functionality:
  - When a user enters a duplicate task (task with the same title), the system will notify the user.
  - When the user accidentally deleted a task, the system can help undo the action easily.
  - The system allows users to view added tasks offline.
  - The system allows users to edit the task after it is already saved.

#### Advanced features:

1. **Progress Visualization:**
   - Use a library like `Matplotlib` to display task completion progress via charts (e.g., bar or pie charts).
2. **Dark/Light Mode:**
   * Allow users to toggle between dark and light themes to improve visual comfort and accessibility.
2. **Avoiding task duplication based on title:**
   * Backend implementation of checking for existing tasks and displaying correct message in the fronend.
3. **SQLite integration to store data (tasks/users):**
   * Storing both task and user data in database.

## Future Enhancements Section:

#### AI-powered Task Automation:

1. Implement AI-driven task suggestions based on user behavior and priorities.
2. Use natural language processing to allow users to create tasks via voice or chat.
3. Introduce automated reminders and follow-ups based on task deadlines and urgency.

#### Security & Privacy Enhancements:

1. Offer end-to-end encryption for sensitive task data.
2. Provide automatic daily cloud backups.
