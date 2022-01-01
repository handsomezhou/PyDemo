# -*- coding: utf-8 -*-
# @Time : 2021/1/3
# @Author : handsomezhou

#start:setting

table_setting="setting"

INDEX_ID=int(0)
INDEX_KEY=int(1)
INDEX_VALUE=int(2)
INDEX_CREATE_TIME=int(3)
INDEX_UPDATE_TIME=int(4)

id = "id"
key = "key"
value = "value"
create_time = "create_time"
update_time = "update_time"


CREATE_TABLE_SETTING = "CREATE TABLE IF NOT EXISTS "+table_setting+"("+id+" INTEGER PRIMARY KEY,"+key+" TEXT NOT NULL,"+value+" TEXT NOT NULL,"+create_time+" TEXT NOT NULL,"+update_time+" TEXT NOT NULL);"

INSERT_TABLE_SETTING_ITEM="INSERT INTO "+table_setting+" ("+id+","+key+","+value+","+create_time+","+update_time+") VALUES (?, ?, ?, ?, ? );"
UPDATE_TABLE_SETTING_ITEM = "UPDATE "+table_setting+" SET "+value+" = ?,"+update_time+" = ? WHERE "+key+" = ?;"
FIND_TABLE_SETTING_ITEM_BY_KEY = "SELECT * FROM " +table_setting + " WHERE "+key+" = ? ;"
FIND_TABLE_SETTING_ITEM_ID_KEY_VALUE_CREATE_TIME_UPDATE_TIME_BY_KEY = "SELECT " + id + "," + key + "," + value + "," + create_time + "," + update_time + " FROM " + table_setting + " WHERE " + key + " = ? ;"
FIND_TABLE_SETTING_ITEM_ID_KEY_VALUE_CREATE_TIME_UPDATE_TIME = "SELECT " + id + "," + key + "," + value + "," + create_time + "," + update_time + " FROM " + table_setting + " ;"
FIND_TABLE_SETTING_VALUE_BY_KEY = "SELECT "+value+" FROM " +table_setting + " WHERE "+key+" = ? ;"

#end:setting
