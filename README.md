# Study and Task Planner

A small command-line task planner written in Python. It stores tasks in a local JSON file and has automated tests. I am building it as a learning project while preparing for an IT apprenticeship (Ausbildung) in Germany.

## Current features

- Add a task (empty titles are rejected)
- List all tasks, with [ ] for open and [x] for finished tasks
- Mark a task as done by its id
- Input checks for unknown menu choices, non-numeric ids and ids that do not exist
- Tasks are saved in tasks.json in the project folder
- Automated tests with pytest

## Requirements

- Python 3.9 or newer
- pytest (only needed to run the tests)

## Usage

python task_planner.py
The program asks for one action per run: add, list or done.

Choose add, list or done: add
Task title: Learn Git basics
Added task 1: Learn Git basics
```
Choose add, list or done: list
[ ] 1. Learn Git basics


Choose add, list or done: done
Task id: 1
Marked task 1 as done.

## Running the tests

python -m pip install pytest
python -m pytest

The tests cover adding tasks, trimming whitespace, rejecting empty titles, marking tasks as done and handling unknown ids. They call the functions directly, which is possible because the task logic is separate from the `input()` and `print()` code.

## Project structure

task_planner.py       task logic, JSON storage and the menu
test_task_planner.py  pytest tests
.gitignore            keeps tasks.json and caches out of the repository
`

## Design decisions

- Only the Python standard library is used, so there is nothing to install to run the program.
- The task logic (`add_task`, `complete_task`) is separate from user input and output, so it can be tested without typing anything.
- Validation happens inside `add_task` and `complete_task`, so the rules apply no matter how the functions are called.
- Marking an already finished task as done again is accepted silently and keeps it done.

## Known limitations

- The menu handles one action per run.
- A damaged or invalid `tasks.json` is not handled yet and will cause an error.
- Task ids are based on the number of tasks, so they would clash once tasks can be deleted.
- Tasks cannot be edited or deleted yet.

## Planned

- Handle a damaged `tasks.json` safely
- Edit and delete tasks
- A loop so several actions can be done in one run

## How this was built

I built this step by step . I run and test every change myself, and I can explain how each part works.# Study and Task Planner
