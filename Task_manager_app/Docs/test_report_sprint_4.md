# Summary of testing results (updated per milestone)

This test report documents the results of the Test-Driven Development (TDD) process for the Group 4 Task Manager app.. The testing methodology follows a Red-Green-Refactor approach to ensure that all functionalities meet the required specifications before implementation.

## Milestone 4

Date: 3/31/25
Author: Devin Winters
Project: Task Manager
Version: 0.0.3
Tested By: 

| Test Case          | Test Type | Status    | Input | Expected Results | Actual Results |
| ------------------ | --------- | --------- | ----- | ---------------- | -------------- |
| Add Task           | Unit      | ✅ Passed | "Get milk", "Go to Wal-mart and use your coupon", 2 | tm.tasks[0].title == "Get milk", tm.tasks[0].desc == "Go to Wal-mart and use your coupon", tm.tasks[0].priority == 2 | tm.tasks[0].title == "Get milk", tm.tasks[0].desc == "Go to Wal-mart and use your coupon", tm.tasks[0].priority == 2 |
| Change Theme       | Manual    | ✅ Passed | Click on Switch Theme button. | Theme toggles correctly, except some hint text in the prompt boxes disappears in the light mode. | The theme switches between a "light" mode and a "dark" mode. |
