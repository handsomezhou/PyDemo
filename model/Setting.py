# -*- coding: utf-8 -*-
# @Time : 2021/9/22
# @Author : handsomezhou

class Setting:
    def __init__(self,id,key,value,create_time,update_time):
        self.id=id
        self.key=key
        self.value = value
        self.create_time =create_time
        self.update_time=update_time