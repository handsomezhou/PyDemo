# -*- coding: utf-8 -*-
# @Time : 2021/9/22
# @Author : handsomezhou
import threading
import tkinter as tk
from concurrent.futures.thread import ThreadPoolExecutor

from constant import ThreadPoolConstant, Constant, WindowsProgramConstant, DaemonConstant, SettingConstant, \
    StringConstant
from database.PyDemoSqliteSql import PyDemoSqliteSql
from util import TimeUtil, WindowsUtil, FileUtil, CommonUtil


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.start_run_time_ms=TimeUtil.getCurrentTimeMillis()
        self.cur_time_ms=TimeUtil.getCurrentTimeMillis()
        self.count=int(0)

        self.pack()
        self.create_widgets()
        self.threadPoolExecutor = ThreadPoolExecutor(max_workers=ThreadPoolConstant.MAX_WORKERS)

        #用于心跳检测等与业务线程分开,避免业务线程全部持续占用导致心跳不正常
        self.baseThreadPoolExecutor= ThreadPoolExecutor(max_workers=ThreadPoolConstant.BASE_WORKERS)

        self.py_demo_sqlite_sql=PyDemoSqliteSql()
        self.last_write_py_demo_heartbeat_time_ms = int(0)
        self.last_read_py_demo_daemon_heartbeat_time_ms = int(0)
        self.try_to_start_py_demo_check()

        self.test_1_task_check_is_run=False
        self.test_1_task_count=int(0)
        self.test_1_task_interval_time_sec=5 #任务执行完毕,下次开启该任务间隔时间 秒
        self.start_test_1_task()


        self.test_2_task_check_is_run=False
        self.test_2_task_count=int(0)
        self.test_2_task_interval_time_sec=12 #任务执行完毕,下次开启该任务间隔时间 秒
        self.start_test_2_task()


    def create_widgets(self):
        # https://www.cnblogs.com/shwee/p/9427975.html#D1
        # https://www.tianqiweiqi.com/python-tkinter-button.html

        # """

        self.start_run_time_label_tips = tk.Label(self, text=StringConstant.start_run_time_label_tips)
        self.start_run_time_label_tips.pack()

        self.start_run_time_label = tk.Label(self, text=TimeUtil.get_log_time_by_ms(self.start_run_time_ms))
        self.start_run_time_label.pack()



        self.tips=None
        self.tips_string_var= tk.StringVar()
        self.tips_label = tk.Label(self, textvariable=self.tips_string_var)
        #self.tips_label.pack(side=tk.BOTTOM)
        self.refresh_tips_label()


    def clear_tips(self):
        if CommonUtil.is_empty(self.tips) is False:
            self.set_tips(Constant.NULL_STRING)
        return

    def set_tips(self,tips):
        self.tips=tips
        self.tips_string_var.set(tips)
        self.refresh_tips_label()
        return

    def refresh_tips_label(self):
        if CommonUtil.is_empty(self.tips):
            self.hide_tips_label()
        else:
            self.show_tips_label()

        return
    def show_tips_label(self):
        self.tips_label.pack(side=tk.BOTTOM)
        return

    def hide_tips_label(self):
        self.tips_label.pack_forget()
        return


    #start:py_demo_check
    def try_to_start_py_demo_check(self):
        self.baseThreadPoolExecutor.submit(self.py_demo_check)
        return

    def py_demo_check(self):

        try:

            py_demo_daemon_running=self.is_py_demo_daemon_running()

            if py_demo_daemon_running is False:
                has_installed=self.has_py_demo_daemon_installed()
                if has_installed is False:
                    force_upgrade = True

                    self.check_py_demo_daemon_upgrade(force_upgrade)
                    has_installed=self.has_py_demo_daemon_installed()

                if has_installed is True:
                    print(TimeUtil.getLogTime(),Constant.COLON,"开启PyDemo守护进程程序")
                    self.open_py_demo_daemon()
                else:
                    print(TimeUtil.getLogTime(),Constant.COLON,"PyDemo守护进程程序未安装,无法打开该程序")
            else:
                self.try_to_restart_py_demo_daemon()

        except Exception as e:
            print(TimeUtil.getLogTime(), Constant.COLON, e.__traceback__.tb_frame.f_globals[Constant.__file__],e.__traceback__.tb_lineno, " py_demo_check 异常 ", e)
        finally:
            self.try_to_update_py_demo_heartbeat()


        self.start_next_py_demo_check()
        return

    def try_to_update_py_demo_heartbeat(self):
        try:
            current_time_millis = TimeUtil.getCurrentTimeMillis()
            last_update_interval_time_ms = current_time_millis - self.last_write_py_demo_heartbeat_time_ms
            if last_update_interval_time_ms > DaemonConstant.PY_DEMO_HEARTBEAT_TIME_UPDATE_MIN_INTERVAL_TIME_MS:
                self.last_write_py_demo_heartbeat_time_ms = current_time_millis
                id = current_time_millis
                value = str(id)
                self.py_demo_sqlite_sql.insert_table_setting_data(id=id,key=SettingConstant.key_py_demo_heartbeat_time,value=value)
                print(TimeUtil.getLogTime(), Constant.COLON, "更新PyDemo心跳 [",TimeUtil.get_log_time_by_ms(current_time_millis), "] 距离上次更新时间[", TimeUtil.ms2sec(last_update_interval_time_ms), "]秒")
            else:
                print(TimeUtil.getLogTime(), Constant.COLON, "本次不更新更新PyDemo心跳 上次更新时间为[",TimeUtil.get_log_time_by_ms(self.last_write_py_demo_heartbeat_time_ms), "] 距离上次更新时间[", TimeUtil.ms2sec(last_update_interval_time_ms), "]秒")
        except Exception as e:
            print(TimeUtil.getLogTime(), Constant.COLON, e.__traceback__.tb_frame.f_globals[Constant.__file__],e.__traceback__.tb_lineno, " try_to_update_py_demo_heartbeat 异常 ", e)


        return

    def try_to_restart_py_demo_daemon(self):
        try:
            current_time_millis = TimeUtil.getCurrentTimeMillis()
            last_update_interval_time_ms = current_time_millis - self.last_read_py_demo_daemon_heartbeat_time_ms
            if last_update_interval_time_ms > DaemonConstant.PY_DEMO_HEARTBEAT_TIME_UPDATE_MIN_INTERVAL_TIME_MS:
                self.last_read_py_demo_daemon_heartbeat_time_ms = current_time_millis

                value=self.py_demo_sqlite_sql.load_setting_value(SettingConstant.key_py_demo_daemon_heartbeat_time)

                if value is not None:
                    py_demo_daemon_heartbeat_time=int(value)
                    last_heartbeat_interval_time_ms=current_time_millis-py_demo_daemon_heartbeat_time
                    if (last_heartbeat_interval_time_ms)>DaemonConstant.PY_DEMO_DAEMON_HEARTBEAT_TIME_UPDATE_MAX_INTERVAL_TIME_MS:
                        print(TimeUtil.getLogTime(), Constant.COLON, "PyDemo守护进程心跳异常 上次心跳时间[",TimeUtil.get_log_time_by_ms(py_demo_daemon_heartbeat_time),"] 在[",TimeUtil.ms2sec(last_heartbeat_interval_time_ms),"]秒前,将自动重启PyDemo守护进程")
                        self.close_py_demo_daemon()
                        self.open_py_demo_daemon()
                    else:
                        print(TimeUtil.getLogTime(), Constant.COLON,"PyDemo守护进程心跳正常 上次心跳时间[",TimeUtil.get_log_time_by_ms(py_demo_daemon_heartbeat_time),"] 在[",TimeUtil.ms2sec(last_heartbeat_interval_time_ms),"]秒前")

                else:
                    print(TimeUtil.getLogTime(), Constant.COLON, "未读取到PyDemo守护进程心跳时间,请确保该应用存在")


            else:
                print(TimeUtil.getLogTime(), Constant.COLON, "本次不读取PyDemo守护进程心跳时间 上次读取时间 [",TimeUtil.get_log_time_by_ms(self.last_read_py_demo_daemon_heartbeat_time_ms), "] 在[", TimeUtil.ms2sec(last_update_interval_time_ms), "]秒前")
        except Exception as e:
            print(TimeUtil.getLogTime(), Constant.COLON, e.__traceback__.tb_frame.f_globals[Constant.__file__],e.__traceback__.tb_lineno, " try_to_restart_py_demo_daemon 异常 ", e)
        return

    def start_next_py_demo_check(self):
        interval_time_sec=DaemonConstant.PY_DEMO_CHECK_INTERVAL_TIME_SEC
        print(TimeUtil.getLogTime(),Constant.COLON,interval_time_sec,"秒后,开启下一轮守护检测")
        t = threading.Timer(interval_time_sec, self.try_to_start_py_demo_check)
        t.start()

    def is_py_demo_daemon_running(self):
        py_demo_daemon_running=WindowsUtil.checkIfProcessRunning(WindowsProgramConstant.PyDemoDaemonNameWithSuffix)
        print(TimeUtil.getLogTime(),Constant.COLON,"PyDemo守护进程程序是否运行中[",py_demo_daemon_running,"]")
        return py_demo_daemon_running

    def close_py_demo_daemon(self):
        close_success=WindowsUtil.closeApp(WindowsProgramConstant.PyDemoDaemonNameWithSuffix)
        return close_success

    def open_py_demo_daemon(self):
        open_success =WindowsUtil.openApp(WindowsProgramConstant.PY_DEMO_DAEMON_FULL_PATH_BIN)
        return open_success

    def has_py_demo_daemon_installed(self):
        has_installed = FileUtil.exists(WindowsProgramConstant.PY_DEMO_DAEMON_FULL_PATH_BIN)
        print(TimeUtil.getLogTime(),Constant.COLON,"PyDemo守护进程程序是否安装[",has_installed,"]")
        return has_installed

    def check_py_demo_daemon_upgrade(self, force_upgrade):
        print(TimeUtil.getLogTime(), Constant.COLON, "请拷贝相关程序到指定目录 ", WindowsProgramConstant.PY_DEMO_DAEMON_FULL_PATH_BIN)
        return
    #end:py_demo_check


    #start: test 1 task
    def start_test_1_task(self):

        if self.test_1_task_check_is_run is False:
            self.test_1_task_check_is_run = True
            self.try_to_test_1_task()

        print(TimeUtil.getLogTime(), Constant.COLON,"start_test_1_task test_1_task_count",self.test_1_task_count,"test_1_task_check_is_run",self.test_1_task_check_is_run)

        return


    def stop_test_1_task(self):
        self.test_1_task_check_is_run=False
        print(TimeUtil.getLogTime(), Constant.COLON,"stop_test_1_task test_1_task_count",self.test_1_task_count,"test_1_task_check_is_run",self.test_1_task_check_is_run)
        return

    def try_to_test_1_task(self):
        self.test_1_task_count += 1
        self.threadPoolExecutor.submit(self.test_1_task)
        return

    def test_1_task(self):
        print(TimeUtil.getLogTime(), Constant.COLON,"执行 test_1_task")

        self.start_next_test_1_task()
        return

    def start_next_test_1_task(self):
        if self.test_1_task_check_is_run is True:
            interval_time_sec= self.test_1_task_interval_time_sec
            print(TimeUtil.getLogTime(), Constant.COLON,interval_time_sec,"秒后执行test_1_task")
            t = threading.Timer(interval_time_sec, self.try_to_test_1_task)
            t.start()
        else:
            print(TimeUtil.getLogTime(), Constant.COLON, "will stop export data task as  test_1_task_count",self.test_1_task_count,"test_1_task_check_is_run",self.test_1_task_check_is_run)

        return
    #end:test 1 task

    #start: test 2 task
    def start_test_2_task(self):

        if self.test_2_task_check_is_run is False:
            self.test_2_task_check_is_run = True
            self.try_to_test_2_task()

        print(TimeUtil.getLogTime(), Constant.COLON,"start_test_2_task test_2_task_count",self.test_2_task_count,"test_2_task_check_is_run",self.test_2_task_check_is_run)

        return


    def stop_test_2_task(self):
        self.test_2_task_check_is_run=False
        print(TimeUtil.getLogTime(), Constant.COLON,"stop_test_2_task test_2_task_count",self.test_2_task_count,"test_2_task_check_is_run",self.test_2_task_check_is_run)
        return

    def try_to_test_2_task(self):
        self.test_2_task_count += 1
        self.threadPoolExecutor.submit(self.test_2_task)
        return

    def test_2_task(self):
        print(TimeUtil.getLogTime(), Constant.COLON,"执行 test_2_task")

        self.start_next_test_2_task()
        return

    def start_next_test_2_task(self):
        if self.test_2_task_check_is_run is True:
            interval_time_sec= self.test_2_task_interval_time_sec
            print(TimeUtil.getLogTime(), Constant.COLON,interval_time_sec,"秒后执行test_2_task")
            t = threading.Timer(interval_time_sec, self.try_to_test_2_task)
            t.start()
        else:
            print(TimeUtil.getLogTime(), Constant.COLON, "will stop export data task as  test_2_task_count",self.test_2_task_count,"test_2_task_check_is_run",self.test_2_task_check_is_run)

        return
    #end:test 2 task
if __name__ == '__main__':
    root = tk.Tk()
    root.title(StringConstant.py_demo)
    root.geometry(StringConstant.main_window_geometry)
    app = Application(master=root)
    app.mainloop()