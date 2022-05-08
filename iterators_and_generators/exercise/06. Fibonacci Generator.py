def fibonacci():
    pvs_num, cnt_num = 0, 1
    while True:
        yield pvs_num
        pvs_num, cnt_num = cnt_num, pvs_num + cnt_num
