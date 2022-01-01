# -*- coding: utf-8 -*-
# @Time : 2021/6/2
# @Author : handsomezhou



from constant import WindowsProgramConstant, Constant

"""
获取当前程序运行目录
注意通过程序运行自动获取,目录不正确,尝试找解决方法
暂时固定,如果上述方法不行,也可以做成可配置的选项
"""
def get_current_program_running_dir():
    return WindowsProgramConstant.CURRENT_PROGRAM_RUNNING_DIR

def get_export_data_dir():
    export_data_dir=get_current_program_running_dir()+Constant.BACK_SLASH+WindowsProgramConstant.EXPORT_DATA_DIR
    return export_data_dir