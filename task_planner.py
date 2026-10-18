import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks: list[dict]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(tasks: list[dict], title: str) -> dict:
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    return task


if __name__ == "__main__":
    tasks = load_tasks()
    title = input("Task title: ")
    try:
        new_task = add_task(tasks, title)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        save_tasks(tasks)
        print(f"Added task {new_task['id']}: {new_task['title']}")