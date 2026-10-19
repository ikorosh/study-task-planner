import pytest

from task_planner import add_task, complete_task


def test_add_task_creates_task_with_id_and_title():
    tasks = []
    task = add_task(tasks, "Learn Git")
    assert task == {"id": 1, "title": "Learn Git", "done": False}
    assert tasks == [task]


def test_add_task_strips_whitespace():
    tasks = []
    task = add_task(tasks, "  Learn Git  ")
    assert task["title"] == "Learn Git"


def test_add_task_rejects_empty_title():
    with pytest.raises(ValueError):
        add_task([], "   ")


def test_complete_task_marks_task_done():
    tasks = []
    add_task(tasks, "Learn Git")
    complete_task(tasks, 1)
    assert tasks[0]["done"] is True


def test_complete_task_unknown_id_raises():
    with pytest.raises(ValueError):
        complete_task([], 99)


def test_complete_task_twice_keeps_task_done():
    tasks = []
    add_task(tasks, "Learn Git")
    complete_task(tasks, 1)
    complete_task(tasks, 1)
    assert tasks[0]["done"] is True