# Summary of testing results (updated per milestone)

This test report documents the results of the Test-Driven Development (TDD) process for the Group 4 Task Manager app.. The testing methodology follows a Red-Green-Refactor approach to ensure that all functionalities meet the required specifications before implementation.

## Milestone 4

Date: 3/31/25
Author: Devin Winters
Project: Task Manager
Version: 0.0.3
Tested By: Devin Winters

| Test Case          | Test Type | Status    | Input | Expected Results | Actual Results |
| ------------------ | --------- | --------- | ----- | ---------------- | -------------- |
| Add Task (UI)      | Manual    | ✅ Passed | Text input: "Get milk", "Other", "Go get milk at Wal-mart". Selected priority is "High" | A task with "Get milk" as the title, "Other" as the tag, "Go get milk at Wal-mart" as the description, and a priority of "High". | Expected input achieved. |
| Change Theme       | Manual    | ✅ Passed | Click on Switch Theme button. | Theme toggles correctly, except some hint text in the prompt boxes disappears in the light mode. | The theme switches between a "light" mode and a "dark" mode. |
