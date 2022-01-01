# -*- coding: utf-8 -*-
# @Time : 2021/1/3
# @Author : handsomezhou

#start:common
#https://blog.csdn.net/wuyou1336/article/details/53770799
IS_TABLE_EXIST = "select count(*)  from sqlite_master where type='table' and name = ?;"
#end:common


