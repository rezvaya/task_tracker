def read_tasks_from_file(file_name):
    tasks = []
    tasks_list = []
    
    with open(file_name, 'r') as file:
        tasks = file.readlines()
        
    for task in tasks:
        current_task = task.split("-")
        if "True" in current_task[1]:
            current_task[1] = True
        else:
            current_task[1] = False
        tasks_list.append(current_task)

    return tasks_list


def save_tasks_in_file(tasks, file_name):
    with open(file_name, 'w') as file:
        for task in tasks:
            file.write(f"{task[0]}-{task[1]}\n")


# list_tasks = [['task3', True], ['task4', False]]
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
        print("1")
    elif user_choice == '2':
        print("2")
    elif user_choice == '3':
        print("3")
    elif user_choice == '4':
        save_tasks_in_file(tasks, filename)
        print("Все сохранили! До свидания!")
        break
    else:
        print("Выбрана несуществующая опция!")