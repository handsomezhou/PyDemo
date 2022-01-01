# -*- coding: utf-8 -*-
# @Time : 2021/1/3
# @Author : handsomezhou
# Reference : https://www.cnblogs.com/boxker/p/10542896.html

import sqlite3
import threading

from constant import DataBaseConstant

lock = threading.Lock()

class SqliteSql:
    """
     simpleToolSql for sqlite3
     简单数据库工具类
     编写这个类主要是为了封装sqlite，继承此类复用方法
     """
    def __init__(self,db_file_path="test.db"):

        #初始化数据库，默认文件名 test.db
        #filename：文件名

        #A:[Python-Sqlite3模块-解决报错问题: SQLite objects created in a thread can only be used in that same thread](https://blog.csdn.net/qq_31445217/article/details/107955952)
        #elf.connect = sqlite3.connect(self.filename,timeout=10, check_same_thread=False)
        self.connect = sqlite3.connect(db_file_path, timeout=10, check_same_thread=False)
        self.cursor = self.connect.cursor()

    def close(self):
        """
        关闭数据库
        """
        if self.cursor is not None:
            self.cursor.close()

        if self.connect is not None:
            self.connect.close()

    """
    Q:Recursive use of cursors not allowed.
    A:
    https://blog.csdn.net/qq_46269068/article/details/108377309?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-2&spm=1001.2101.3001.4242
    def execute(self,sql,param=None):
        
        #执行数据库的增、删、改
        #sql：sql语句
        #param：数据，可以是list或tuple，亦可是None
        #retutn：成功返回True
        
        try:
            if param is None:
                self.cursor.execute(sql)
            else:
                if type(param) is list:
                    self.cursor.executemany(sql,param)
                else :
                    self.cursor.execute(sql,param)
            count = self.connect.total_changes
            self.connect.commit()
        except Exception as e:
            print(e)
            return False,e
        if count > 0 :
            return True
        else :
            return False
    """
    def execute(self,sql,param=None):
        execute_success=False
        """
        执行数据库的增、删、改
        sql：sql语句
        param：数据，可以是list或tuple，亦可是None
        retutn：成功返回True
        """
        lock.acquire()
        try:
            if param is None:
                self.cursor.execute(sql)
            else:
                if type(param) is list:
                    self.cursor.executemany(sql,param)
                else :
                    self.cursor.execute(sql,param)
            count = self.connect.total_changes
            self.connect.commit()

            execute_success = True
        except Exception as e:
            print(e)
            #return False,e
            execute_success = False
        finally:
            lock.release()

        """
        if count > 0 :
            return True
        else :
            return False
        """
        return execute_success

    """
    def query(self, sql, param=None):
        
        #查询语句
        #sql：sql语句
        #param：参数,可为None
        #retutn：成功返回True
        
        if param is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, param)
        return self.cursor.fetchall()
    """
    def query(self,sql,param=None):
        """
        查询语句
        sql：sql语句
        param：参数,可为None
        retutn：成功返回True
        """
        lock.acquire()
        all_rows=None
        try:
            if param is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql,param)

            all_rows=self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            lock.release()

        return all_rows

    # def set(self,table,field=" * ",where="",isWhere=False):
    #     self.table = table
    #     self.filed = field
    #     if where != "" :
    #         self.where = where
    #         self.isWhere = True
    #     return True


if __name__ == "__main__":
    """
    测试代码
    """
    filename = "test2" + DataBaseConstant.DB_SUFFIX_WITH_FULL_STOP
    db_path_path = filename
    #db_path_path = str(utility.get_file_path(filename))
    sql = SqliteSql(db_path_path)

    f = sql.execute("create table test (id int not null,name text not null,age int);")
    print("ok")
    sql.execute("insert into test (id,name,age) values (?,?,?);",[(1,'abc',15),(2,'bca',16)])
    res = sql.query("select * from test;")
    print(res)
    sql.execute("insert into test (id,name) values (?,?);",(3,'bac'))
    res = sql.query("select * from test where id=?;",(3,))
    print(res)
    sql.close()