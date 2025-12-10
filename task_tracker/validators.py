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
        except Exception:
            return False
