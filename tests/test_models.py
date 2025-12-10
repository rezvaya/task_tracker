from task_tracker.models import Task, StudyTask

def test_task_marked():
    task = Task("test", False)
    task.mark_done()
    assert task.status is True

def test_study_task_show():
    task = StudyTask("test", False, "10.12.2025")
    assert "Дедлайн" in task.show_task()

def test_task_show():
    task = Task("test", False)
    assert not "Дедлайн" in task.show_task()