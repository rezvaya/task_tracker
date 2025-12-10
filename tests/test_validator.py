from task_tracker.validators import check_date_format

def test_data_format():
    assert check_date_format("10.12.2025")

def test_incorrect_data():
    assert not check_date_format("100.120.2025")