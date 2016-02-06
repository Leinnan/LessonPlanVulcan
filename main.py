#!/usr/bin/python

#-*- coding: utf-8 -*-

import lesson 
import argparse

parser = argparse.ArgumentParser(description='Pokazuje plan lekcji',
                                    epilog='Program stworzony przez Leinnana.')
parser.add_argument('-c', '--current', dest='current_only', help='Pokazuje tylko aktualny/najblizszy dzien', action='store_true')
args = parser.parse_args()


global show_current_only;
show_current_only = parser.parse_args().current_only; 



logo = """\033[1m

    _   ___                     ___  ______ 
    | | / / |                   /   | |  ___|
    | |/ /| | __ _ ___  __ _   / /| | | |_   
    |    \| |/ _` / __|/ _` | / /_| | |  _|  
    | |\  \ | (_| \__ \ (_| | \___  | | |    
    \_| \_/_|\__,_|___/\__,_|     |_/ \_|    
                                         
                                         
\033[0m
"""

print(logo)

my_lessons_array = lesson.getLessons();
lesson.printLessons(my_lessons_array, show_current_only);