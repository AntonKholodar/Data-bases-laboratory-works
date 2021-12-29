import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "postgresql+psycopg2://postgres:qwerty@localhost:5432/antonynewbase"
Base = declarative_base()
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

s = Session()

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

def valid_to_insert_customer(id: int, nameoftable):
    f = bool(s.query(nameoftable).filter_by(CustomerID=id).first())
    if f == True:
        return 0
    else:
        return 1

def valid_to_insert_bill(id: int, custid: int, manid: int, nameoftable, custtable, mantable):
    f = bool(s.query(nameoftable).filter_by(BillID=id).first())
    p = bool(s.query(custtable).filter_by(CustomerID=custid).first())
    t = bool(s.query(mantable).filter_by(ManagerID=manid).first())
    if f == False and p == True and t == True:
        return 1
    else:
        return 0

def valid_to_insert_car(vin: str, custid: int, nameoftable, custtable):
    f = bool(s.query(nameoftable).filter_by(VIN=vin).first())
    p = bool(s.query(custtable).filter_by(CustomerID=custid).first())
    if f == False and p == True:
        return 1
    else:
        return 0


def valid_to_insert_carsalesmanager(id: int, nameoftable):
    f = bool(s.query(nameoftable).filter_by(ManagerID=id).first())
    if f == True:
        return 0
    else:
        return 1

def valid_to_insert_car_carsalesmanager(id: int, vin: str, manid: int, nameoftable, cartable, mantable):
    f = bool(s.query(nameoftable).filter_by(SaleID=id).first())
    p = bool(s.query(cartable).filter_by(VIN=vin).first())
    t = bool(s.query(mantable).filter_by(ManagerID=manid).first())
    if f == False and p == True and t == True:
        return 1
    else:
        return 0


def valid_data_to_delete(id):
    if str(id).isdigit():
        return 1
    else:
        return 0


def valid_to_delete_customer(id: int, customer, billtable, cartable):
    t = bool(s.query(customer).filter_by(CustomerID=id).first())
    f = bool(s.query(billtable).filter_by(CustomerID=id).first())
    p = bool(s.query(cartable).filter_by(CustomerID=id).first())
    if t == False:
        msg("Nothing to delete.")
        return 0
    elif f == True or p == True:
        msg("There are some dependencies in Bill or in Car on it.")
        return 0
    else:
        return 1

def valid_to_delete_bill(id:int, billtable):
    t = bool(s.query(billtable).filter_by(BillID=id).first())
    if t == False:
        msg("Nothing to delete.")
        return 0
    else:
        return 1

def valid_to_delete_car(vin: str, car, car_carsalesmanagertable):
    t = bool(s.query(car).filter_by(VIN=vin).first())
    f = bool(s.query(car_carsalesmanagertable).filter_by(VIN=vin).first())
    if t == False:
        msg("Nothing to delete.")
        return 0
    elif f == True:
        msg("There are some dependencies in Car_CarSalesManager on it")
        return 0
    else:
        return 1

def valid_to_delete_carsalesmanager(id: int, carsalesmamanger, billtable, car_carsalesmanagertable):
    t = bool(s.query(carsalesmamanger).filter_by(ManagerID=id).first())
    f = bool(s.query(billtable).filter_by(ManagerID=id).first())
    p = bool(s.query(car_carsalesmanagertable).filter_by(ManagerID=id).first())
    if t == False:
        msg("Nothing to delete.")
        return 0
    elif f == True or p == True:
        msg("There are some dependencies in Bill or in Car_CarSalesManager on it")
        return 0
    else:
        return 1

def valid_to_delete_car_carsalesmanager(id: int, car_carsalesmanager):
    t = bool(s.query(car_carsalesmanager).filter_by(SaleID=id).first())
    if t == False:
        msg("Nothing to delete.")
        return 0
    else:
        return 1


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


def valid_to_update_customer(id: int, Customer):
    f = bool(s.query(Customer).filter_by(CustomerID=id).first())
    if f == True:
        return 1
    else:
        return 0

def valid_to_update_bill(id: int, Bill):
    f = bool(s.query(Bill).filter_by(BillID=id).first())
    if f == True:
        return 1
    else:
        return 0

def valid_to_update_car(vin: str, Car):
    f = bool(s.query(Car).filter_by(VIN=vin).first())
    if f == True:
        return 1
    else:
        return 0

def valid_to_update_carsalesmanager(id:int, CarSalesManager):
    f = bool(s.query(CarSalesManager).filter_by(ManagerID=id).first())
    if f == True:
        return 1
    else:
        return 0