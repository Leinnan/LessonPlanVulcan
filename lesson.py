#-*- coding: utf-8 -*-


import my_time

class lesson:
    def __init__(self, number_of_class, subject_name):
        self.number_of_class = number_of_class
        self.subject_name = subject_name
      
def getLessons(): 
    # tablica z lista zmiennych
    # nr 0 to tylko nazwa dnia
    # od 1 do 8 to obiekty lekcji
    lesson_array = [[0]*9 for i in range(5)]

    # poniedzialek
    lesson_array[0][0] = "Poniedziałek"
    lesson_array[0][1] = lesson(16,"matematyka")
    lesson_array[0][2] = lesson(16,"matematyka")
    lesson_array[0][3] = lesson(11,"j. polski")
    lesson_array[0][4] = lesson(38,"informatyka")
    lesson_array[0][5] = lesson(38,"informatyka")
    lesson_array[0][6] = lesson(29,"j. angielski")
    lesson_array[0][7] = lesson(29,"j. angielski")

    # wtorek
    lesson_array[1][0] = "Wtorek"
    lesson_array[1][1] = lesson(16,"matematyka")
    lesson_array[1][2] = lesson(23,"historia")
    lesson_array[1][3] = lesson(16,"zaj. wych.")
    lesson_array[1][4] = lesson(29,"j. angielski")
    lesson_array[1][5] = lesson(1,"religia")
    lesson_array[1][6] = lesson(11,"j. polski")
    lesson_array[1][7] = lesson(11,"j. polski")

    # sroda
    lesson_array[2][0] = "Środa"
    lesson_array[2][1] = lesson(16,"matematyka")
    lesson_array[2][2] = lesson(16,"matematyka")
    lesson_array[2][3] = lesson(11,"j. polski")
    lesson_array[2][4] = lesson(19,"informatyka")
    lesson_array[2][5] = lesson(19,"informatyka")
    lesson_array[2][6] = lesson(29,"j. angielski")

    # czwartek
    lesson_array[3][0] = "Czwartek"
    lesson_array[3][1] = lesson(0,"wf")
    lesson_array[3][2] = lesson(23,"historia")
    lesson_array[3][3] = lesson(38,"informatyka")
    lesson_array[3][4] = lesson(38,"informatyka")
    lesson_array[3][5] = lesson(29,"j. angielski")
    lesson_array[3][6] = lesson(23,"historia")

    # piatek
    lesson_array[4][0] = "Piątek"
    lesson_array[4][1] = lesson(0,"wf")
    lesson_array[4][2] = lesson(0,"wf")
    lesson_array[4][3] = lesson(16,"matematyka")
    lesson_array[4][4] = lesson(16,"matematyka")
    lesson_array[4][5] = lesson(11,"j. polski")
    lesson_array[4][6] = lesson(38,"informatyka")
    lesson_array[4][7] = lesson(1,"religia")
    
    return lesson_array;


def printLessons(lesson_array, show_current_only, show__days_inline):
    
    # odejmuje jeden bo pierwszy dzien ma numer 0, a nie 1
    current_day = my_time.current_time()[0]
    is_weekend = False
    
    # jesli jest po 15 to ustawia jako aktualny dzien nastepny
    if my_time.current_time()[1] > 15:
        current_day += 1
    
    # po piatku najblizszy jest poniedzialek
    if current_day > 5:
        current_day = 0
        is_weekend = True
    
    # wyswietlanie dni obok siebie start
    if show__days_inline and not show_current_only:
        # najpierw nazwy dni
        for i in range(0,len(lesson_array)):
            print('\033[94m{:^18}\033[0m'.format(
                        str(lesson_array[i][0])), end="\t")
            

        # teraz po kolei dana godzina w kazdym dniu
        for j in range(1,len(lesson_array[i])):
            print("\n",end="")
            for i in range(0,len(lesson_array)):
                if not lesson_array[i][j]:
                    print("{: ^18}".format("-"), end="\t")
                else:
                    if i == current_day:
                        print('\033[93m{: <16}{: >2}\033[0m'.format(
                            lesson_array[i][j].subject_name,
                            lesson_array[i][j].number_of_class), end="\t")
                    else:
                        print('{: <16}{: >2}'.format(
                            lesson_array[i][j].subject_name,
                            lesson_array[i][j].number_of_class), end="\t")
        print("\n",end="")
        return 1
    # wyswietlanie dni obok siebie end

    for i in range(0,len(lesson_array)):
        # jesli zmienna show_current_only jest rowna true
        # wyswietla tylko najblizszy/aktualny dzien
        if show_current_only == True and not i == current_day:
            continue
    
        # kontynuuje jesli pierwsza komórka 
        # w danym rzedzie ma jakakolwiek wartosc 
        if lesson_array[i][0]:
            print('\033[94m{:^18}\033[0m'.format(
                        str(lesson_array[i][0])))
            
            
            for j in range(1,len(lesson_array[i])):
                # przerywamy petle 
                # gdy trafiamy na puste komórki
                if not lesson_array[i][j]:
                    continue
                    
                
                if i == current_day:
                    print('\033[93m{: <16}{: >2}\033[0m'.format(
                        lesson_array[i][j].subject_name,
                        lesson_array[i][j].number_of_class))
                else:
                    print('{: <16}{: >2}'.format(
                        lesson_array[i][j].subject_name,
                        lesson_array[i][j].number_of_class))
    return 1
