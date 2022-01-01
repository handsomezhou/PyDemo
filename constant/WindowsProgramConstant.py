# -*- coding: utf-8 -*-
# @Time : 2020/12/16
# @Author : handsomezhou
from constant import Constant

MIN_VERSION_NAME="0.0.0.0"
FULL_STOP_AND_ZIP_SUFFIX=".zip"

PyDemoNameWithSuffix= "PyDemo.exe"
PyDemoDaemonNameWithSuffix= "PyDemoDaemon.exe"

#PyDemo不带后缀
PyDemo="PyDemo"
#PyDemoDaemon不带后缀
PyDemoDaemon="PyDemoDaemonName"

#指定应用程序目录
PY_DEMO_BIN_DIR = r'C:\Soft\PyDemo'
#PY_DEMO_DAEMON_BIN_DIR = r'C:\Soft\PyDemoDaemon'
#指定同一目录
PY_DEMO_DAEMON_BIN_DIR =PY_DEMO_BIN_DIR


#指定应用程序临时目录(下载,解压,拷贝,删除)
PY_DEMO_BIN_TMP_DIR = r'C:\Soft\PyDemoTmp'
PY_DEMO_DAEMON_BIN_TMP_DIR = r'C:\Soft\PyDemoDaemonTmp'

#当前程序运行目录
CURRENT_PROGRAM_RUNNING_DIR=r'C:\Soft\PyDemo'

#导出数据
EXPORT_DATA_DIR="ExportData"

#指定应用程序完整路径
PY_DEMO_FULL_PATH_BIN = r'C:\Soft\PyDemo\PyDemo.exe'
#PY_DEMO_DAEMON_FULL_PATH_BIN = r'C:\Soft\PyDemoDaemon\PyDemoDaemon.exe'
#指定同一目录
PY_DEMO_DAEMON_FULL_PATH_BIN = r'C:\Soft\PyDemo\PyDemoDaemon.exe'


#Windows程序后缀
WINDOWS_BIN_SUFFIX="exe"
CLOSE_APP_PREFIX="taskkill /F /IM "