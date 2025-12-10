from interface import cli
from file_manager import read_tasks_from_file

FILENAME = 'tasks.txt'
tasks = read_tasks_from_file('tasks.txt')

if __name__ == "__main__":
    cli(FILENAME, tasks)