# -*- coding: utf-8 -*-
# @Time : 2020/8/11
# @Author : handsomezhou
import math
import time
from datetime import datetime

from constant import Constant, TimePatternConstant

HOUR_PER_DAY = 24

MINUTE_PER_HOUR = 60

SECOND_PER_MINUTE = 60

MILLISECOND_PER_SECOND = 1000

def getCurrentTimeMillis():

    return round(time.time()* MILLISECOND_PER_SECOND)

def getCurrentTimeSec():

    return round(time.time())

def ms2sec (ms):
    sec = (ms/MILLISECOND_PER_SECOND)
    return round(sec)

def ms2min (ms):
    min = (ms/MILLISECOND_PER_SECOND/SECOND_PER_MINUTE)
    return round(min)

def ms_2_min_4_ceil(ms):
    min = (ms/MILLISECOND_PER_SECOND/SECOND_PER_MINUTE)
    return math.ceil(min)

def ms_2_min_4_floor(ms):
    min = (ms/MILLISECOND_PER_SECOND/SECOND_PER_MINUTE)
    return math.floor(min)

def ms2hour (ms):
    hour = (ms/MILLISECOND_PER_SECOND/SECOND_PER_MINUTE/MINUTE_PER_HOUR)
    return round(hour)

def ms2day (ms):
    day = (ms/MILLISECOND_PER_SECOND/SECOND_PER_MINUTE/MINUTE_PER_HOUR/HOUR_PER_DAY)
    return round(day)

def sec2ms (sec):
    ms = sec*MILLISECOND_PER_SECOND
    return round(ms)

def sec2min (sec):
    min = sec/SECOND_PER_MINUTE
    return round(min)

def sec2hour (sec):
    hour = (sec/SECOND_PER_MINUTE/MINUTE_PER_HOUR)
    return round(hour)

def sec2day (sec):
    day = (sec/SECOND_PER_MINUTE/MINUTE_PER_HOUR/HOUR_PER_DAY)
    return round(day)


def min2ms (min):
    ms = min*SECOND_PER_MINUTE*MILLISECOND_PER_SECOND
    return round(ms)

def min2sec (min):
    sec = min*SECOND_PER_MINUTE
    return round(sec)

def min2hour (min):
    hour = min/MINUTE_PER_HOUR
    return round(hour)

def min2day (min):
    day = min/MINUTE_PER_HOUR/HOUR_PER_DAY
    return round(day)

def hour2ms(hour):
    ms = ( hour * MINUTE_PER_HOUR * SECOND_PER_MINUTE* MILLISECOND_PER_SECOND)
    return round(ms)

def hour2sec(hour):
    sec = ( hour * MINUTE_PER_HOUR * SECOND_PER_MINUTE)
    return round(sec)

def hour2min(hour):
    min = ( hour * MINUTE_PER_HOUR)
    return round(min)

def hour2day(hour):
    day = ( hour /HOUR_PER_DAY)
    return round(day)

def day2ms(day):
    ms = day * HOUR_PER_DAY * MINUTE_PER_HOUR * SECOND_PER_MINUTE * MILLISECOND_PER_SECOND
    return round(ms)

def day2sec(day):
    sec = day * HOUR_PER_DAY * MINUTE_PER_HOUR * SECOND_PER_MINUTE
    return round(sec)

def day2min(day):
    min = day * HOUR_PER_DAY * MINUTE_PER_HOUR
    return round(min)

def day2hour(day):
    hour = day * HOUR_PER_DAY
    return round(hour)

def week2ms(week):
    ms = week * Constant.SEVEN_OF_INTEGER * HOUR_PER_DAY * MINUTE_PER_HOUR * SECOND_PER_MINUTE * MILLISECOND_PER_SECOND
    return round(ms)

def week2sec(week):
    sec = week * Constant.SEVEN_OF_INTEGER * HOUR_PER_DAY * MINUTE_PER_HOUR * SECOND_PER_MINUTE
    return round(sec)

def week2min(week):
    min = week * Constant.SEVEN_OF_INTEGER * HOUR_PER_DAY * MINUTE_PER_HOUR
    return round(min)

def week2hour(week):
    hour = week * Constant.SEVEN_OF_INTEGER * HOUR_PER_DAY
    return round(hour)

def week2day(week):
    day = week * Constant.SEVEN_OF_INTEGER
    return round(day)

def getLogTime():
    # time.tme() 得到的是float型时间戳
    struct_time = time.localtime(time.time())  # 得到结构化时间格式
    tm = time.strftime(TimePatternConstant.YEAR_TO_SEC, struct_time)
    return tm

def get_log_time_by_ms(millis):
    # time.tme() 得到的是float型时间戳
    struct_time = time.localtime(ms2sec(millis))  # 得到结构化时间格式
    tm = time.strftime(TimePatternConstant.YEAR_TO_SEC, struct_time)
    return tm

# https://blog.csdn.net/ieeso/article/details/96888073
def get_microsecond_of_day():
    return datetime.now().microsecond

def get_second_of_day():
    return datetime.now().second


def get_minute_of_day():
    return datetime.now().minute


def get_hour_of_day():
    return datetime.now().hour


def get_day_of_month():
    return datetime.now().day


def get_month_of_year():
    return datetime.now().month


def get_year():
    return datetime.now().year

def get_the_day_start_time_ms(time_ms:int):
    # 将毫秒值转化为datetime对象  // 是 Python 中的整数除法操作符，表示对两个数进行相除后向下取整得到的整数部分
    dt = datetime.fromtimestamp(time_ms // MILLISECOND_PER_SECOND)

    # 获取当天的开始时间
    start_of_day = dt.replace(hour=0, minute=0, second=0, microsecond=0)

    # 将开始时间转换回毫秒值
    the_day_start_time_ms = int(start_of_day.timestamp() * MILLISECOND_PER_SECOND)

    return the_day_start_time_ms

def get_the_day_end_time_ms(time_ms):
    the_day_end_time_ms=get_the_day_start_time_ms(time_ms)+hour2ms(24)

    #print("the_day_end_time_ms",the_day_end_time_ms)
    #print("get_log_time_by_ms",get_log_time_by_ms(the_day_end_time_ms))
    return the_day_end_time_ms


"""
Reference: https://blog.csdn.net/jingyi130705008/article/details/78169733
"""
def strftime(year_to_sec:str):
    return datetime.strptime(year_to_sec,TimePatternConstant.YEAR_TO_SEC)

def str_2_datetime(date_string:str, format:str):
    return datetime.strptime(date_string,format)

def datetime_2_str(date_time:datetime):
    date_time_str=None
    if date_time is not None:
        date_time_str = str(date_time)
    return date_time_str

"""
[python将字符串格式的时间转换为整数(以毫秒为单位)](https://www.jianshu.com/p/6eafd81aa97f)
"""
def str_2_ms(date_string:str, format:str):
    strptime=time.strptime(date_string, format)
    ms = int(time.mktime(strptime) * 1000)

    return ms

"""
[python time和datetime的常用转换处理](https://www.cnblogs.com/lxmhhy/p/6030730.html)
"""
def datetime_2_ms(date_time:datetime):
    ms = int(time.mktime(date_time.timetuple()) * 1000)
    return ms

if __name__ == "__main__":
    ms=getCurrentTimeMillis()
    t= get_log_time_by_ms(ms)
    print(t,type(t))
    # print("ms ",ms)
    # print(ms2sec(ms))
    # print(ms2min(ms))
    # print(ms2hour(ms))
    # print(ms2day(ms))
    #
    # sec=ms2sec(ms)
    #
    # print(sec2ms(sec))
    # print("sec ", sec)
    # print(sec2min(sec))
    # print(sec2hour(sec))
    # print(sec2day(sec))
    #
    # min=ms2min(ms)
    # print(min2ms(min))
    # print(min2sec(min))
    # print("min ",min)
    # print(min2hour(min))
    # print(min2day(min))
    #
    # print(get_year())
    # print(get_month_of_year())
    # print(get_day_of_month())
    # print(get_hour_of_day())
    # print(get_minute_of_day())
    # print(get_second_of_day())
    #
    # get_the_day_start_time_ms(getCurrentTimeMillis())
    # get_the_day_end_time_ms(getCurrentTimeMillis())

    the_day_start_time_ms=get_the_day_start_time_ms(getCurrentTimeMillis())
    print("the_day_start_time_ms",the_day_start_time_ms,get_log_time_by_ms(the_day_start_time_ms))

    the_day_end_time_ms=get_the_day_end_time_ms(getCurrentTimeMillis())
    print("the_day_end_time_ms",the_day_end_time_ms,get_log_time_by_ms(the_day_end_time_ms))

    date_string = getLogTime()
    format = TimePatternConstant.YEAR_TO_SEC
    print("date_string", date_string, "format", format)
    date_time = str_2_datetime(date_string, format)
    print("date_time ", date_time)
    print("year", date_time.year)
    print("month", date_time.month)
    print("day", date_time.day)
    print("hour", date_time.hour)
    print("minute", date_time.minute)
    print("second", date_time.second)

    date_string2 = "2021-07-23"
    format = TimePatternConstant.YEAR_TO_DAY
    print("\ndate_string", date_string2, "format", format)
    date_time = str_2_datetime(date_string2, TimePatternConstant.YEAR_TO_DAY)

    date_time.time()
    #print(type())
    print("date_time ", date_time)
    print("year", date_time.year)
    print("month", date_time.month)
    print("day", date_time.day)
    print("hour", date_time.hour)
    print("minute", date_time.minute)
    print("second", date_time.second)

    ms = str_2_ms(date_string2, TimePatternConstant.YEAR_TO_DAY)
    print(date_string2, "->", ms)

    date_string3 = "2021-07-23 01:23:45"
    ms = str_2_ms(date_string3, TimePatternConstant.YEAR_TO_SEC)
    print(date_string3, "->", ms)

    datetime_now=datetime.now()
    print(type(datetime_now),datetime_now)
    ms=datetime_2_ms(datetime_now)
    print("ms",ms,get_log_time_by_ms(ms))

