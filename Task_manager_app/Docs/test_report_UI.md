
# Summary of testing results (UI)

## Milestone III

Date: 3/17/2025
Author: Brippney Vargas
Project: Task Manager
Version: 0.0.1
Tested By: 

This test report documents the results of the UI testing process for Task Manager app. The testing methodology focuses on verifying the user interface elements and interactions meet the required specifications.

| Test Case | Test Type | Status | Result | Input | Expected Results | Actual Results |
|-----------|-----------|--------|--------|-------|------------------|---------------|
| Connection Status | manual    | ✅ Passed | API Connection indicator displays correctly | None | API Connected indicator shows green checkmark | API Connected indicator shows green checkmark with text "API Connected" |
| Add Task Form | manual    | ✅ Passed | All form fields display correctly | None | Title field, Tag dropdown, Description textarea, Priority radio buttons, Add Task button all present | All form elements present and labeled correctly |
| Task Creation | manual    | ✅ Passed | Task is added to the list when form is submitted | Title: "Operating System", Tag: "Labwork", Description: "Complete assn5", Priority: High | New task appears in task list with correct data | Task appears in list with entered details and correct priority color |
| Priority Display | manual    | ✅ Passed | Priority indicators show correct colors | Create tasks with different priorities | High: Red, Medium: Orange, Low: Yellow | High shows as red button, Low shows as yellow button |
| Task List Headers | manual    | ✅ Passed | Task list displays all column headers | None | Headers for Title, Tag, Description, Priority, Edit, Delete | All column headers display correctly |
| Load Tasks Button | manual    | ✅ Passed | Load Tasks button functions correctly | Click "Load Tasks" button | Button clickable, success message appears | Button clicked, "Tasks loaded successfully!" message displayed |
| Save Tasks Button | manual    | ✅ Passed | Save Tasks button appears correctly | None | Button visible and clickable | Save Tasks button appears with disk icon and is clickable |
| Edit Task Button | manual    | ✅ Passed | Edit buttons appear for each task | None | Pencil icon in Edit column for each task | Edit buttons appear as pencil icons for all tasks |
| Delete Task Button | manual    | ✅ Passed | Delete buttons appear for each task | None | Trash icon in Delete column for each task | Delete buttons appear as trash icons for all tasks |
| Tag Dropdown | manuak    | ✅ Passed | Tag dropdown expands with options | Click on Tag dropdown | Dropdown expands with options including "Other" and "Labwork" | Dropdown expands showing all available tag options |
| Description Textarea | manual    | ✅ Passed | Description textarea accepts input | Enter "Complete assn5" | Text appears in textarea | Text entered successfully and displayed in textarea |
| Priority Selection | manual    | ✅ Passed | Priority radio buttons function correctly | Click each radio button | Only one radio button can be selected at a time | Radio buttons function as expected with mutual exclusivity |
| Success Message Display | manual    | ✅ Passed | Success message appears and is readable | Load tasks | "Tasks loaded successfully!" message appears in green box | Success message displayed with correct styling and text |
| Task List Row Styling | manual    | ✅ Passed | Task list rows have consistent styling | None | All rows have consistent height, spacing, and alignment | Task list rows display with uniform styling |
| Application Title | manual    | ✅ Passed | Application title is visible | None | "Task Manager" title appears at top of application | Title appears with correct text and icon |
| Mobile Responsiveness | manual    | ✅ Passed | UI adjusts for smaller screens | Resize browser window | Elements should reflow appropriately for smaller screens | UI elements properly reflow on mobile screens with no overlapping |
| Form Validation | manual    | ✅ Passed | Form prevents submission with empty Title and empty Description| Attempt to add task with empty title and description | Form should prevent submission | Form does not submit with empty title and description field and a warning message pops up |
| Character Limit Handling | manual    | ✅ Passed | Description field handles long text | Enter very long description | Text should be contained within field with scrolling | Description field correctly handles overflow with scrollbar |


