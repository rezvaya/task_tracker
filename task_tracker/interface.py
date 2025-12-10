from validators import check_date_format, marked
from file_manager import save_tasks_in_file
from models import Task, StudyTask

# TO-DO: реализовать функцию для абстрактного интерфейса


def cli(filename, tasks):
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
            except Exception:
                print("Произошла ошибка! Попробуйте еще раз.")

        elif user_choice == '4':
            save_tasks_in_file(tasks, filename)
            print("Все сохранили! До свидания!")
            break
        else:
            print("Выбрана несуществующая опция!")
