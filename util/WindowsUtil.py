# -*- coding: utf-8 -*-
# @Time : 2020/12/16
# @Author : handsomezhou
import os

import psutil
import win32api
from win32com.client import GetObject


#https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
from constant import Constant, WindowsProgramConstant
from util import TimeUtil


# https://www.jb51.net/article/61955.htm
def getVersionName(file_name):
    info = win32api.GetFileVersionInfo(file_name, os.sep)
    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    version = '%d.%d.%d.%d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
    return version

#是否升级
def isUpgrade(newVersionName,oldVersionName):
    return compareVersionName(newVersionName,oldVersionName)>0

#srcVersionName-dstVersionName>0 升级
#srcVersionName-dstVersionName<=0 不升级
def compareVersionName(newVersionName,oldVersionName):
    value=int(0)
    if newVersionName is None:
        if oldVersionName is None:
            return value
        else:
            value=-int(1)
            return value
    else:
        if oldVersionName is None:
            value = int(1)
            return value

    newVersionNameList=str(newVersionName).split(Constant.FULL_STOP)
    oldVersionNameList=str(oldVersionName).split(Constant.FULL_STOP)

    minListLen= 0
    maxListLen=0
    if len(newVersionNameList)>len(oldVersionNameList):
        minListLen=len(oldVersionNameList)
        maxListLen=len(newVersionNameList)
    else:
        minListLen=len(newVersionNameList)
        maxListLen=len(oldVersionNameList)

    for i in range(minListLen):
        if int(newVersionNameList[i]) > int(oldVersionNameList[i]):
            value = int(1)
            return value
        if int(newVersionNameList[i]) < int(oldVersionNameList[i]):
            value = -int(1)
            return value

    if maxListLen != minListLen:
        if len(newVersionNameList)>len(oldVersionNameList):
            value = int(1)
        else:
            value = -int(1)

    return value


#带后缀不带后缀均可
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        #except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        except Exception as e:
            print(TimeUtil.getLogTime(),Constant.COLON,"异常 ",e)

    return False

#带后缀不带后缀均可
def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name','create_time'])
            # Check if process name contains the given name string.
            if processName.lower() in pinfo['name'].lower() :
                listOfProcessObjects.append(pinfo)
        #except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
        except Exception as e:
            print(TimeUtil.getLogTime(),Constant.COLON,"异常 ",e)

    return listOfProcessObjects

"""
def find_all_programs():
    return psutil.process_iter()
"""

#python中3种调用可执行文件.exe的方法  https://blog.csdn.net/zsc201825/article/details/80918185

#https://blog.csdn.net/Chase_zq/article/details/90043329
#此方法ok,但是A调用B,B使用了A的上下文,如果A和B程序中没有使用绝对路径加载db等数据,而又不同目录的话,B无法在A目录中找到本应在B目录下的db等数据资源
#解决方法直接将程序与守护程序放到同一个目录
def openApp(app_full_path_dir):
    openSuccess=False
    try:
        os.startfile(app_full_path_dir) #os.startfile（）打开外部应该程序，与windows双击相同
        openSuccess=True
    except Exception as e:
        print(TimeUtil.getLogTime(),Constant.COLON,"open_app 异常 ",e)

    return openSuccess

#https://www.jb51.net/article/164186.htm
#带后缀不带后缀均可
def closeApp(app_name):
    closeSuccess=False
    app_name_with_suffix=app_name
    if app_name.endswith(WindowsProgramConstant.WINDOWS_BIN_SUFFIX) is False:
        app_name_with_suffix=app_name+Constant.FULL_STOP+WindowsProgramConstant.WINDOWS_BIN_SUFFIX

    cmd=WindowsProgramConstant.CLOSE_APP_PREFIX+app_name_with_suffix
    print("cmd",cmd)
    try:
        os.system(cmd)
        closeSuccess=True
    except Exception as e:
        print(TimeUtil.getLogTime(),Constant.COLON,"异常 ",e)

    return closeSuccess

"""
https://blog.csdn.net/qdPython/article/details/105667857
"""
def open_dir(dir):
    # 利用explorer.exe执行
    try:
        if dir is not None:
            os.system("explorer.exe %s" % dir)
    except Exception as e:
        print(TimeUtil.getLogTime(),Constant.COLON,"open_dir",e)

if __name__ == "__main__":
    print(getVersionName(WindowsProgramConstant.PY_DEMO_FULL_PATH_BIN))
    print(checkIfProcessRunning(WindowsProgramConstant.PyDemoNameWithSuffix))
    print(checkIfProcessRunning(WindowsProgramConstant.PyDemo))
    print(findProcessIdByName(WindowsProgramConstant.PyDemoNameWithSuffix))
    print(findProcessIdByName(WindowsProgramConstant.PyDemo))
    openApp(WindowsProgramConstant.PY_DEMO_FULL_PATH_BIN)
    closeApp(WindowsProgramConstant.PyDemo)
    closeApp(WindowsProgramConstant.PyDemoNameWithSuffix)

