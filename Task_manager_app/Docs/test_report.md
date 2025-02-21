# Summary of testing results (updated per milestone)

This test report documents the results of the Test-Driven Development (TDD) process for the Group 4 Task Manager app.. The testing methodology follows a Red-Green-Refactor approach to ensure that all functionalities meet the required specifications before implementation.

## Milestone II

Date: 2/18/25
Author: Jacob West, Devin Winters
Project: Task Manager
Version: 0.0.1
Tested By: Devin Winters

| Test Case               | Test Type      | Status    | Result                                                                                              |
| ----------------------- | -------------- | --------- | --------------------------------------------------------------------------------------------------- |
| Add Task                | Unit           | ✅ Passed | Tasks are being created successfully!                                                               |
| Delete Task             | Unit           | ✅ Passed | Tasks are being deleted successfully!                                                               |
| Save Tasks              | Unit           | ✅ Passed | The Task Manager can save the loaded/created tasks to a json file!                                  |
| Load Tasks              | Unit           | ✅ Passed | The Task Manager can load files from a json file!                                                   |
| View Tasks              | Unit           | ✅ Passed | Tasks can be displayed in the CLI in a tabular format!                                              |
| Delete Nonexistent Task | Error Handling | ✅ Passed | Attempting to delete a task that doesn't exist will not result in a crash!                          |
| Load Incorrect Json     | Error Handling | ✅ Passed | Loading bad data, either in incorrect format or from a corrupted file, will properly handle errors! |
| Invalid Priority        | Error Handling | ✅ Passed | Tasks assigned with priorities outside the 1-5 range are handled!                                   |

Each test was created prior to development, and was created with the `unittest` library.
