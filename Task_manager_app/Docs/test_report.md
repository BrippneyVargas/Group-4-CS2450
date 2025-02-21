# Summary of testing results (updated per milestone)

This test report documents the results of the Test-Driven Development (TDD) process for the Group 4 Task Manager app.. The testing methodology follows a Red-Green-Refactor approach to ensure that all functionalities meet the required specifications before implementation.

## Milestone II

Date: 2/18/25
Author: Jacob West, Devin Winters
Project: Task Manager
Version: 0.0.1
Tested By: Jacob West

| Test Case               | Test Type      | Status    | Result                                                                                              | Input | Expected Results | Actual Results |
| ----------------------- | -------------- | --------- | --------------------------------------------------------------------------------------------------- | - | - | - |
| Add Task                | Unit           | ✅ Passed | Tasks are being created successfully!                                                               | "Get milk", "Go to Wal-mart and use your coupon", 2 | tm.tasks[0].title == "Get milk", tm.tasks[0].desc == "Go to Wal-mart and use your coupon", tm.tasks[0].priority == 2 | tm.tasks[0].title == "Get milk", tm.tasks[0].desc == "Go to Wal-mart and use your coupon", tm.tasks[0].priority == 2 |
| Delete Task             | Unit           | ✅ Passed | Tasks are being deleted successfully!                                                               | None | tm.tasks == [] | tm.tasks == [] |
| Save Tasks              | Unit           | ✅ Passed | The Task Manager can save the loaded/created tasks to a json file!                                  | "tests.json" (empty) | "tests.json" contains { title: "Get soda", desc: "Use coupons at Smith's", priority: 2 } { title: "Take medicine", desc: "Should be underneath sink", priority: 3 } | { title: "Get soda", desc: "Use coupons at Smith's", priority: 2 } { title: "Take medicine", desc: "Should be underneath sink", priority: 3 } |
| Load Tasks              | Unit           | ✅ Passed | The Task Manager can load files from a json file!                                                   | "tests.json" (empty) | TODO | TODO | 
| View Tasks              | Unit           | ✅ Passed | Tasks can be displayed in the CLI in a tabular format!                                              | None | {"Title": "Complete Project", "Description": "Finish the project report by...", "Priority": 1}, {"Title": "Workout", "Description": "Exercise for 30 minutes at the gym.", "Priority": 2}, {"Title": "Buy Groceries", "Description": "Get milk, eggs, and bread.", "Priority": 3} | {"Title": "Complete Project", "Description": "Finish the project report by...", "Priority": 1}, {"Title": "Workout", "Description": "Exercise for 30 minutes at the gym.", "Priority": 2}, {"Title": "Buy Groceries", "Description": "Get milk, eggs, and bread.", "Priority": 3} |
| Delete Nonexistent Task | Error Handling | ✅ Passed | Attempting to delete a task that doesn't exist will not result in a crash!                          | None | "Task not found.\n" | "Task not found.\n" |
| Load Incorrect Json     | Error Handling | ✅ Passed | Loading bad data, either in incorrect format or from a corrupted file, will properly handle errors! | None | json.JSONDecodeError | json.JSONDecodeError |
| Invalid Priority        | Error Handling | ✅ Passed | Tasks assigned with priorities outside the 1-5 range are handled!                                   | None | None | None |

Each test was created prior to development, and was created with the `unittest` library.
