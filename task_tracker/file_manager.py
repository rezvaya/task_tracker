from models import Task, StudyTask


def read_tasks_from_file(file_name):
    '''
    Функция, которая ...
    Возвращает...
    '''
    tasks = []
    tasks_list = []
    try:
        with open(file_name, 'r') as file:
            tasks = file.readlines()
    except FileNotFoundError:
        print(f"Файл {file_name} не существует")
    except PermissionError:
        print(f"Файл {file_name} не доступен для чтения")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    for task in tasks:
        current_task = task.split("-")

        if "True" in current_task[1]:
            current_task[1] = True
        else:
            current_task[1] = False
        if len(current_task) == 3:
            tasks_list.append(
                StudyTask(current_task[0], current_task[1], current_task[2]))
        else:
            tasks_list.append(Task(current_task[0], current_task[1]))

    return tasks_list


def save_tasks_in_file(tasks, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for task in tasks:
            file.write(f"{task.str_to_file()}\n")
