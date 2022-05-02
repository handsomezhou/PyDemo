# -*- coding: utf-8 -*-
# @Time : 2021/1/3
# @Author : handsomezhou

from constant import DataBaseConstant, Constant, SettingConstant
from database import SqliteCmd, SettingSqliteCmd
from database.SqliteSql import SqliteSql
from model.Setting import Setting
from util import TimeUtil, CommonUtil

DB_NAME_4_PY_DEMO = "PyDemo"

LIMIT_COUNT_MIN_VALUE = 1
LIMIT_COUNT_MAX_VALUE = 1000000
LIMIT_COUNT_DEFAULT_VALUE = 200000



def item_2_setting(item):
    setting = None
    if item is not None:
        if len(item)>0:
            start_index = int(0)
            id=item[SettingSqliteCmd.INDEX_ID - start_index]
            key=item[SettingSqliteCmd.INDEX_KEY - start_index]
            value=item[SettingSqliteCmd.INDEX_VALUE - start_index]
            create_time=item[SettingSqliteCmd.INDEX_CREATE_TIME - start_index]
            update_time=item[SettingSqliteCmd.INDEX_UPDATE_TIME - start_index]

            setting = Setting(id,key,value,create_time,update_time)
    return setting



class PyDemoSqliteSql:
    def __init__(self):
        self.sqlite_sql=None
        self.print_log = True


        self.init_sqlite_sql()


        return
    
    def close(self):
        if self.sqlite_sql is not None:
            self.sqlite_sql.close()

    def init_sqlite_sql(self):
        if self.sqlite_sql is None:
            filename = DB_NAME_4_PY_DEMO + DataBaseConstant.DB_SUFFIX_WITH_FULL_STOP
            #db_path_path = str(utility.get_file_path(filename))
            db_path_path=filename
            self.sqlite_sql = SqliteSql(db_path_path)
            self.create_table()

        return

    def is_table_exist(self,table_name):
        table_exist =False
        row=self.sqlite_sql.query(SqliteCmd.IS_TABLE_EXIST, (table_name,))

        count=int(row[0][0])
        table_exist= count > 0
        print(TimeUtil.getLogTime(),Constant.COLON,"table_name[",table_name,"]table_exist [",table_exist,"]count[",count,"]")
        return table_exist

    def is_table_exist2(self,table_name,print_log:bool):
        table_exist =False
        row=self.sqlite_sql.query(SqliteCmd.IS_TABLE_EXIST, (table_name,))

        count=int(row[0][0])
        table_exist= count > 0
        if print_log is True:
            print(TimeUtil.getLogTime(),Constant.COLON,"table_name[",table_name,"]table_exist [",table_exist,"]count[",count,"]")
        return table_exist


    """
    创建表
    """
    def create_table(self):
        if self.sqlite_sql is None:
            self.init_sqlite_sql()

        self.create_table_setting()

        return

    #start:setting
    def is_table_setting_exist(self):

        return self.is_table_exist(SettingSqliteCmd.table_setting)

    def create_table_setting(self):
        if self.sqlite_sql is None:
            self.init_sqlite_sql()

        if self.is_table_setting_exist() is False:
            executeSuccess = self.sqlite_sql.execute(SettingSqliteCmd.CREATE_TABLE_SETTING)
            print(TimeUtil.getLogTime(), Constant.COLON, "create_table_setting [", SettingSqliteCmd.CREATE_TABLE_SETTING,"]executeSuccess[", executeSuccess, "]")
        return

    def set_table_setting_str_value(self,key:str, value:str):
        id=TimeUtil.getCurrentTimeMillis()
        self.insert_table_setting_data(id,key,value)
        return

    def get_table_setting_str_value(self,key:str):
        return self.load_setting_value(key)


    def set_table_setting_bool_value(self,key:str, value:bool):
        id=TimeUtil.getCurrentTimeMillis()
        self.insert_table_setting_data(id,key,str(value))
        return

    def set_table_setting_int_value(self,key:str, value:int):
        id=TimeUtil.getCurrentTimeMillis()
        self.insert_table_setting_data(id,key,str(value))
        return

    def get_table_setting_int_value(self,key:str):
        value=None
        v=self.load_setting_value(key)
        value=CommonUtil.get_int_value(v)
        return value

    def get_table_setting_bool_value(self,key:str):
        value=None
        v=self.load_setting_value(key)
        value=CommonUtil.get_bool_value(v)
        return  value

    def insert_table_setting_data(self,id, key, value,show_asterisk=False):
        item_count=self.find_table_setting_item_count(key)
        if item_count <=0:

            create_time = TimeUtil.getLogTime()
            update_time = create_time  # TimeUtil.getLogTime()
            if self.print_log is True:
                if show_asterisk is True:
                    print(TimeUtil.getLogTime(), Constant.COLON, "insert data id[", id, "]key[", key, "]value[", CommonUtil.get_asterisk(value),"]create_time[", create_time, "]update_time[", update_time, "]")
                else:
                    print(TimeUtil.getLogTime(), Constant.COLON, "insert data id[", id, "]key[", key, "]value[", value,"]create_time[", create_time, "]update_time[", update_time, "]")
            self.sqlite_sql.execute(SettingSqliteCmd.INSERT_TABLE_SETTING_ITEM, (id, key, value, create_time, update_time))
        else:
            update_time=TimeUtil.getLogTime()
            if self.print_log is True:
                if show_asterisk is True:
                    print(TimeUtil.getLogTime(), Constant.COLON, "update data key[", key, "]value[", CommonUtil.get_asterisk(value), "]update_time[", update_time, "] item_count", item_count)
                else:
                    print(TimeUtil.getLogTime(), Constant.COLON, "update data key[", key, "]value[", value, "]update_time[", update_time, "] item_count", item_count)

            self.update_table_setting(key,value,update_time)

        return


    def update_table_setting(self,key,value,update_time):
        self.sqlite_sql.execute(SettingSqliteCmd.UPDATE_TABLE_SETTING_ITEM,(value,update_time,key,))
        return

    def find_table_setting_item(self, key):
        return self.sqlite_sql.query(SettingSqliteCmd.FIND_TABLE_SETTING_ITEM_BY_KEY, (key,))

    def find_table_setting_item_count(self,key):
        return len(self.sqlite_sql.query(SettingSqliteCmd.FIND_TABLE_SETTING_ITEM_BY_KEY, (key,)))

    def find_table_setting_item_id_key_value_create_time_update_time(self, key):
        return self.sqlite_sql.query(SettingSqliteCmd.FIND_TABLE_SETTING_ITEM_ID_KEY_VALUE_CREATE_TIME_UPDATE_TIME_BY_KEY,(key,))

    def find_table_all_setting_item_id_key_value_create_time_update_time(self):
        return self.sqlite_sql.query(SettingSqliteCmd.FIND_TABLE_SETTING_ITEM_ID_KEY_VALUE_CREATE_TIME_UPDATE_TIME)

    def load_setting_item_list(self,key):
        data_list = []
        items=self.find_table_setting_item_id_key_value_create_time_update_time(key)
        for item in items:
            data = item_2_setting(item)

            if data is not None:
                data_list.append(data)

        return data_list

    def load_setting_value(self,key):
        value=None
        item_list=self.load_setting_item_list(key)
        if len(item_list)<=0:
            return value

        value=item_list[0].value
        return value

    def find_table_setting_value(self, key):
        return self.sqlite_sql.query(SettingSqliteCmd.FIND_TABLE_SETTING_VALUE_BY_KEY, (key,))
    #end:setting


if __name__ == "__main__":
    print("no test")
    pyDemoSql = PyDemoSqliteSql()
    data=pyDemoSql.find_table_setting_value("test")
    print(data,len(data))

    current_time_millis=TimeUtil.getCurrentTimeMillis()
    pyDemoSql.insert_table_setting_data(id=current_time_millis,key=SettingConstant.key_py_demo_heartbeat_time,value=str(current_time_millis))
    data=pyDemoSql.find_table_setting_value(SettingConstant.key_py_demo_heartbeat_time)
    print(data)
    data=pyDemoSql.find_table_setting_item_id_key_value_create_time_update_time(SettingConstant.key_py_demo_heartbeat_time)
    print(data)
    data=pyDemoSql.load_setting_value(SettingConstant.key_py_demo_heartbeat_time)
    print(data)



