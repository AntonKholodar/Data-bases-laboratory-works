import psycopg2
import view

def connection():
    return psycopg2.connect(
        user="postgres",
        password="qwerty",
        host="localhost",
        port="5432",
        database="antonybase",
    )
def disconnection(connection):
    connection.commit()
    connection.close()

def msg(text):
    return print(text)

def valid_table():
    while True:
        table = input ('Please, input table number: ')
        if table.isdigit():
            table = int(table)
            if table > 0 and table < 6:
                break
            else:
                print('Please, enter number from 1 to 5.')
        else:
            print('Please, enter a digit.')
    return table

def valid_data_to_insert(table, row):
    if table == 1:
        if str(row[0]).isdigit():
            return 1
        else:
            return 0
    elif table == 2:
        if str(row[0]).isdigit() and (len(row[1]) >= 10) and (row[1][4] == '-' and row[1][7] == '-' and int(row[1][5]) <= 1 and int(row[1][8]) <= 3)\
                and str(row[2]).isdigit() and str(row[3]).isdigit():
            if int(row[1][5]) == 0 and  int(row[1][6]) == 1:
                if int(row[1][8]) >= 3 and  int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and  int(row[1][6]) == 2:
                if int(row[1][8]) >= 2 and  int(row[1][9]) > 8:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and  int(row[1][6]) == 3:
                if int(row[1][8]) >= 3 and  int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and  int(row[1][6]) == 4:
                if int(row[1][8]) >= 3 and  int(row[1][9]) > 0:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and  int(row[1][6]) == 5:
                if int(row[1][8]) >= 3 and  int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and  int(row[1][6]) == 6:
                if int(row[1][8]) >= 3 and  int(row[1][9]) > 0:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and  int(row[1][6]) == 7:
                if int(row[1][8]) >= 3 and  int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and  int(row[1][6]) == 8:
                if int(row[1][8]) >= 3 and  int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and  int(row[1][6]) == 9:
                if int(row[1][8]) >= 3 and  int(row[1][9]) > 0:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 1 and  int(row[1][6]) == 0:
                if int(row[1][8]) >= 3 and  int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 1 and  int(row[1][6]) == 1:
                if int(row[1][8]) >= 3 and  int(row[1][9]) > 0:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 1 and  int(row[1][6]) == 2:
                if int(row[1][8]) >= 3 and  int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            else:
                return 0

        else:
            return 0
    elif table == 3:
        if str(row[2]).isdigit():
            return 1
        else:
            return 0
    elif table == 4:
        if str(row[0]).isdigit():
            return 1
        else:
            return 0
    elif table == 5:
        if str(row[0]).isdigit() and str(row[1]).isdigit():
            return 1
        else:
            return 0


def valid_data_to_delete(id):
    if str(id).isdigit():
        return 1
    else:
        return 0


def valid_data_to_update(table, row):
    if table == 1:
        if str(row[0]).isdigit():
            return 1
        else:
            return 0
    elif table == 2:
        if str(row[0]).isdigit() and (len(row[1]) >= 10) and (
                row[1][4] == '-' and row[1][7] == '-' and int(row[1][5]) <= 1 and int(row[1][8]) <= 3):
            if int(row[1][5]) == 0 and int(row[1][6]) == 1:
                if int(row[1][8]) >= 3 and int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and int(row[1][6]) == 2:
                if int(row[1][8]) >= 2 and int(row[1][9]) > 8:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and int(row[1][6]) == 3:
                if int(row[1][8]) >= 3 and int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and int(row[1][6]) == 4:
                if int(row[1][8]) >= 3 and int(row[1][9]) > 0:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and int(row[1][6]) == 5:
                if int(row[1][8]) >= 3 and int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and int(row[1][6]) == 6:
                if int(row[1][8]) >= 3 and int(row[1][9]) > 0:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and int(row[1][6]) == 7:
                if int(row[1][8]) >= 3 and int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and int(row[1][6]) == 8:
                if int(row[1][8]) >= 3 and int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 0 and int(row[1][6]) == 9:
                if int(row[1][8]) >= 3 and int(row[1][9]) > 0:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 1 and int(row[1][6]) == 0:
                if int(row[1][8]) >= 3 and int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 1 and int(row[1][6]) == 1:
                if int(row[1][8]) >= 3 and int(row[1][9]) > 0:
                    return 0
                else:
                    return 1
            elif int(row[1][5]) == 1 and int(row[1][6]) == 2:
                if int(row[1][8]) >= 3 and int(row[1][9]) > 1:
                    return 0
                else:
                    return 1
            else:
                return 0

        else:
            return 0
    elif table == 3:
            return 1
    elif table == 4:
        if str(row[0]).isdigit():
            return 1
        else:
            return 0



def valid_choice_to_select():
    while True:
        choice = input('Your choice -> ')
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice < 4:
                break
            else:
                print('Please, enter number from 1 to 3.')
        else:
            print('Please, enter a digit.')
    return choice

def valid_select_first():
    while True:
        number = input('Enter number: ')
        if number.isdigit():
            number = int(number)
            return number
        else:
            print('Please, enter a digit.')

def valid_data_to_random(id):
    if str(id).isdigit():
        id = int(id)
        return id
    else:
        return 0







