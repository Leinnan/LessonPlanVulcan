#!/usr/bin/python

#-*- coding: utf-8 -*-

import datetime

def current_time():
    # aktualny dzien, godzina i minuta
    current_time_array = [datetime.datetime.now().weekday(), 
                            datetime.datetime.now().hour, 
                            datetime.datetime.now().minute]
    return current_time_array
    
