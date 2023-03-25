# -*- coding: utf-8 -*-
# @Time : 2022/9/8
# @Author : handsomezhou
import threading
from concurrent.futures.thread import ThreadPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler
from constant import ThreadPoolConstant, Constant
from database.PyDemoSqliteSql import PyDemoSqliteSql
from util import TimeUtil

start_run_time_ms=TimeUtil.getCurrentTimeMillis()
cur_time_ms=TimeUtil.getCurrentTimeMillis()
count=int(0)

threadPoolExecutor = ThreadPoolExecutor(max_workers=ThreadPoolConstant.MAX_WORKERS)


py_demo_sqlite_sql=PyDemoSqliteSql()


test_1_task_check_is_run=False
test_1_task_count=int(0)
test_1_task_interval_time_sec=5 #任务执行完毕,下次开启该任务间隔时间 秒



test_2_task_check_is_run=False
test_2_task_count=int(0)
test_2_task_interval_time_sec=12 #任务执行完毕,下次开启该任务间隔时间 秒


#start:test_0_task
def test_0_task():
    try:
        global start_run_time_ms
        global cur_time_ms
        cur_time_ms=TimeUtil.getCurrentTimeMillis()
        print(TimeUtil.getLogTime(), Constant.COLON,"执行 test_0_task start_run_time_ms[",TimeUtil.get_log_time_by_ms(start_run_time_ms),"] cur_time_ms[",TimeUtil.get_log_time_by_ms(cur_time_ms),"]")
    except Exception as e:
        print(TimeUtil.getLogTime(), Constant.COLON,str(e))
    return
#end:test_0_task



#start: test 1 task
def start_test_1_task():
    global test_1_task_check_is_run
    global test_1_task_count
    if test_1_task_check_is_run is False:
        test_1_task_check_is_run = True
        try_to_test_1_task()

    print(TimeUtil.getLogTime(), Constant.COLON,"start_test_1_task test_1_task_count",test_1_task_count,"test_1_task_check_is_run",test_1_task_check_is_run)

    return


def stop_test_1_task():
    global test_1_task_check_is_run
    global test_1_task_count
    test_1_task_check_is_run=False
    print(TimeUtil.getLogTime(), Constant.COLON,"stop_test_1_task test_1_task_count",test_1_task_count,"test_1_task_check_is_run",test_1_task_check_is_run)
    return

def try_to_test_1_task():
    global test_1_task_count
    test_1_task_count += 1
    threadPoolExecutor.submit(test_1_task)
    return

def test_1_task():
    print(TimeUtil.getLogTime(), Constant.COLON,"执行 test_1_task")

    start_next_test_1_task()
    return

def start_next_test_1_task():
    global test_1_task_check_is_run
    global test_1_task_interval_time_sec
    global test_1_task_count
    if test_1_task_check_is_run is True:
        interval_time_sec= test_1_task_interval_time_sec
        print(TimeUtil.getLogTime(), Constant.COLON,interval_time_sec,"秒后执行test_1_task")
        t = threading.Timer(interval_time_sec, try_to_test_1_task)
        t.start()
    else:
        print(TimeUtil.getLogTime(), Constant.COLON, "will stop export data task as  test_1_task_count",test_1_task_count,"test_1_task_check_is_run",test_1_task_check_is_run)

    return
#end:test 1 task

#start: test 2 task
def start_test_2_task():
    global test_2_task_check_is_run
    global test_2_task_count
    if test_2_task_check_is_run is False:
        test_2_task_check_is_run = True
        try_to_test_2_task()

    print(TimeUtil.getLogTime(), Constant.COLON,"start_test_2_task test_2_task_count",test_2_task_count,"test_2_task_check_is_run",test_2_task_check_is_run)

    return


def stop_test_2_task():
    global test_2_task_check_is_run
    global test_2_task_count
    test_2_task_check_is_run=False
    print(TimeUtil.getLogTime(), Constant.COLON,"stop_test_2_task test_2_task_count",test_2_task_count,"test_2_task_check_is_run",test_2_task_check_is_run)
    return

def try_to_test_2_task():
    global  test_2_task_count
    test_2_task_count += 1
    threadPoolExecutor.submit(test_2_task)
    return

def test_2_task():
    print(TimeUtil.getLogTime(), Constant.COLON,"执行 test_2_task")

    start_next_test_2_task()
    return

def start_next_test_2_task():
    global test_2_task_check_is_run
    global test_2_task_interval_time_sec
    global test_2_task_count
    if test_2_task_check_is_run is True:
        interval_time_sec= test_2_task_interval_time_sec
        print(TimeUtil.getLogTime(), Constant.COLON,interval_time_sec,"秒后执行test_2_task")
        t = threading.Timer(interval_time_sec, try_to_test_2_task)
        t.start()
    else:
        print(TimeUtil.getLogTime(), Constant.COLON, "will stop export data task as  test_2_task_count",test_2_task_count,"test_2_task_check_is_run",test_2_task_check_is_run)

    return
#end:test 2 task

if __name__ == '__main__':
    start_test_1_task()
    start_test_2_task()
    blocking_scheduler=BlockingScheduler()
    blocking_scheduler.add_job(test_0_task,"interval",seconds=10)
    blocking_scheduler.start()