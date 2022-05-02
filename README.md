#PyDemo
PyDemo

#编译
pyinstaller  -F  PyDemo.py

#编译-带版本信息
pyinstaller  -F --version-file=file_version_info.txt PyDemo.py

#编译-带图标带版本信息
pyinstaller  -F --icon=PyDemo.ico --version-file=file_version_info.txt PyDemo.py

1.Q:如何将Python打包成exe?

A:[Python 如何将项目打包成exe可执行程序](https://blog.csdn.net/qq_33462307/article/details/90479045)

    exe生成目录:PyDemo\dist\PyDemo.exe
    exe运行路径(默认):C:\Soft\PyDemo\PyDemo.exe  #手动创建相关目录,并将exe拷贝到该路径即可,注意程序及其守护进程在同一个目录并共享同一个db文件

2.如何生成ico图标?

A:[ico在线转换工具](http://www.bitbug.net/)

3.Q:如何手动安装依赖?

    pip install requests
    pip install psutil
    pip install wmi #设备id相关
    pip install pyinstaller #编译相关

4.Q:如何修改成其它项目名(如:PyDemo->PythonDemo)?

A:

    PyDemo -> PythonDemo
    pyDemo -> pythonDemo
    py_demo -> python_demo
    PY_DEMO -> PYTHON_DEMO
    
    database/PyDemoSqliteSql.py-> database/PythonDemoSqliteSql.py
    PyDemo.py -> PythonDemo.py
    PyDemo.ico -> PythonDemo.ico
    file_version_info.py 中 CompanyName  FileDescription FileVersion filevers prodvers
