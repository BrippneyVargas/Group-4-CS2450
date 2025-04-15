# Summary of testing results (updated per milestone)

This test report documents the results of the Test-Driven Development (TDD) process for the Group 4 Task Manager app. The testing methodology follows a Red-Green-Refactor approach to ensure that all functionalities meet the required specifications before implementation.

## Milestone 4

Date: 4/14/25
Author: Jacob West  
Project: Task Manager  
Version: 0.0.4
Tested By: Jacob West

| Test Case                 | Test Type | Status    | Input                                     | Expected Results                                                                                                                                                                                                                     | Actual Results                                                                                                                                               |
| ------------------------- | --------- | --------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SQL Connection Creation   | Unit      | ✅ Passed | Database file: "test_db.db"               | A new SQLite connection is established with `check_same_thread=False` (if applicable), the required tables (`task`, `user`, `task_user`, `tag`) are created, and the `sqlite_sequence` table is generated for autoincrement columns. | Connection successfully established; all tables created as per schema definitions, and the `sqlite_sequence` table is present to track autoincrement values. |
| Table Schema Verification | Unit      | ✅ Passed | SQLiteManager.\__make_\* functions called | Each table (`task`, `user`, `task_user`, `tag`) is present in the database with the correct column names and constraints (e.g., primary keys, foreign keys, NOT NULL constraints)                                                    | Database inspected; tables correctly created with expected columns and constraints.                                                                          |
