import json
import os
import shutil
import sys

sys.path.insert(0, os.path.join("Task_manager_app", "src", "model"))
from task_manager import *

def test_add_task():
    tm = TaskManager()
    tm.add_task("Get milk", "Go to Wal-mart and use your coupon", 2)

    assert tm.tasks[0].title == "Get milk"
    assert tm.tasks[0].desc == "Go to Wal-mart and use your coupon"
    assert tm.tasks[0].priority == 2

def test_delete_task():
    tm = TaskManager()
    tm.add_task("Get milk", "Go to Wal-mart and use your coupon", 2)
    tm.delete_task(tm.tasks[0])

    assert tm.tasks == []

def test_save_task():
    tm = TaskManager()
    tm.add_task("Get milk", "Go to Wal-mart and use your coupon", 2)

    file = open("tasks.json", "r")
    data = json.load(file)
    file.close()

    assert data[0]["title"] == "Get milk"
    assert data[0]["desc"] == "Go to Wal-mart and use your coupon"
    assert data[0]["priority"] == 2

def test_load_tasks():
    shutil.copy("test.json", ".")
    new_path = os.path.join(".", "tasks.json")
    shutil.move(os.path.join(".", "test.json"), new_path)

    tm = TaskManager()

    assert tm.tasks[0].title == "Get soda"
    assert tm.tasks[0].desc == "Use coupons at Smith's"
    assert tm.tasks[0].priority == 2

    assert tm.tasks[1].title == "Take medicine"
    assert tm.tasks[1].desc == "Should be underneath sink"
    assert tm.tasks[1].priority == 3
