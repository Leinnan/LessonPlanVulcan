#!/usr/bin/python

#-*- coding: utf-8 -*-

import datetime

def current_time():
    # aktualny dzien, godzina i minuta
    current_time_array = [datetime.datetime.now().day, datetime.datetime.now().hour, datetime.datetime.now().minute];
    return current_time_array;
    # print(str(current_time_array[0]) + "\t" + str(current_time_array[1]) + "\t" + str(current_time_array[2]))
    
