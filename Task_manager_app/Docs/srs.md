## SRS Document 
### Functional Requirements:
  - The system allows users to add tags to their tasks, making it easier to filter and view them later. For example, users can tag tasks with labels such as className, groupWork, research, or quiz to organize and quickly access related tasks.
  - The system allows users to set priority for each of their tasks. 
  - The system will send a reminder if the task approaches the deadline, if users enable it. 
  - The system allows users to view a specific number of tasks per page. 
  - The system allows users to delete a task.
  - The system allows users to save and load tasks using JSON.
  - The system allows users to update the task’s status (to-do,  in-progress and completed).
  - The system allows users to search for a task. 
  - The system can count the total number of tasks, or filter the count to show only to-do tasks, in-progress tasks, or completed tasks.
  - The system will notify the user if the same task title is added. 

### Non-Functional Requirements:
  - The system must load tasks from a JSON file within 0.1 seconds.
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
    
### Use Cases and User Stories:
  - User Stories:
    1. As an impulsive person, I want to be able to recover tasks that I deleted within a set time period in case I want to recover something I should not have deleted.
    
    2. As a person who gets lost in my notes if they are not organized, I would like to be able to label my tasks. Tagging something as pertaining to school or work will hopefully help me stay on track and not get lost in an avalanche of notes.
    
    3. As a person who gets overwhelmed, I would like to not have all my notes in one place. Instead, I would like them to be divided into different folders or pages by type. This will make the app a lot more usable for me.
    
    4. As a person who tends to ignore a lot of my phone notifications, I would like to be able to decide the priority of tasks I make and how I am reminded of tasks of varying priority. This will help me not ignore more important tasks.
    
    5. As a person who uses their phone too much at night, I would like to be able to set the app to use a light or dark theme, or to default to my device's settings. This will make my experience using the app at varying times of day more enjoyable.
    
    6. As a person who values customization and visual learning, I would like to be able to change the colors of each task I create. This will help me more quickly identify which task I want to find.
    
    7. As a user, I want to add notes to tasks so I can keep additional details for each task.
    
    8. As a user, I want to make my tasks private but also enable sharing if I want to.
    
    9. As a user who wants to feel accomplished, I want to be able to mark a task as complete. This will allow me to know what I have done and still have yet to do in a given day.
    
    10. As a busy person, I want an app that loads quickly and experiences few performance hiccups. This will help me be more efficient with my time.
    
    11. As a person whose eyesight is worsening, I would like to be able to change the size of the font inside the app. This will lessen the strain on my eyes.
    
    12. As a normal person, I want an app with few visual glitches and bugs. I want something pleasing to look at and that will not delete my tasks. My day would go a whole lot better that way.
    
    13. As a person who speaks multiple languages, I would like to be able to change the language the app uses. This will make it easier when I forget what a certain button does.
    
    14. As a person who forgets to lock the door when I leave work, I would like to be able to remind myself to do so when I get too far from where I work. This would help me not get in trouble with security.
        
    16. As a user, I want the system to notify me if I add duplicate tasks (task with the same title). 

  - Use Cases:
    1. ??


## Future Enhancements Section:

#### A list of advanced features brainstormed by the team:

1. Using Flask.
2. Recurring tasks.

#### AI-powered Task Automation:

1. Implement AI-driven task suggestions based on user behavior and priorities.
2. Use natural language processing to allow users to create tasks via voice or chat.
3. Introduce automated reminders and follow-ups based on task deadlines and urgency.

#### Security & Privacy Enhancements:

1. Offer end-to-end encryption for sensitive task data.
2. Provide automatic daily cloud backups.
