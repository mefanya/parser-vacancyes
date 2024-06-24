def test_get_data_from_file(first_job_list):
    result = first_job_list.get_data_from_file()

    if result:
        test = True
    else:
        test = False
    assert test is True
