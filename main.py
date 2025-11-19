from task import Task, StudyTask

def read_tasks_from_file(file_name):
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
            tasks_list.append(StudyTask(current_task[0], current_task[1], current_task[2]))
        else:
            tasks_list.append(Task(current_task[0], current_task[1]))

    return tasks_list


def save_tasks_in_file(tasks, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for task in tasks:
            file.write(f"{task.str_to_file()}\n")


def marked(tasks, number_task_for_marked):
    tasks[number_task_for_marked - 1].mark_done()




def check_date_format(deadline):
    list_of_ddl = deadline.split(".") 
    if len(list_of_ddl) != 3:
        return False
    else:
        try:
            if (int(list_of_ddl[0]) < 32) and (int(list_of_ddl[1]) < 13) and (int(list_of_ddl[2]) > 999):
                return True
            else:
                return False      
        except Exception as e:
            return False

# list_tasks = [['task3', True], ['task4', False]]
# list_tasks = [task3, task4]

filename = 'tasks.txt'
tasks = read_tasks_from_file('tasks.txt')

while True:
    print("Меню: ")
    print("1. Показать задачи")
    print("2. Добавить задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Сохранить и выйти")
    user_choice = input("Выберите действие: ")
    if user_choice == '1':
        for task in tasks:
            print(task.show_task())

    elif user_choice == '2':
        print("Укажите тип задачи: ")
        print("1. Обычная")
        print("2. Учебная")
        task_type = input()
        if not (task_type in ["1", "2"]):
            print("Выбран неверный тип задачи!")
        else:
            title = input("Введите название новой задачи: ")
            if task_type == '1':
                tasks.append(Task(title, False))
                print("Задача создана!")
            elif task_type == '2':
                deadline = input("Введите дедлайн в формате dd.mm.yyyy: ")
                if check_date_format(deadline):
                    tasks.append(StudyTask(title, False, deadline))
                    print("Учебная задача создана!")
                else: 
                    print("Неверный формат ддл!")
        
    elif user_choice == '3':
        for i, task in enumerate(tasks):
            print(f"-----(# {i + 1}) {task.show_task()}")
        try:
            task_number = int(input("Введите номер выполненной задачи: "))
            marked(tasks, task_number)
        except IndexError:
            print("Такой задачи не существует!")
        except Exception as e:
            print("Произошла ошибка! Попробуйте еще раз.")

    elif user_choice == '4':
        save_tasks_in_file(tasks, filename)
        print("Все сохранили! До свидания!")
        break
    else:
        print("Выбрана несуществующая опция!")