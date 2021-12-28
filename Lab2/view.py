import controller
import pandas as pd
from model import Model

class View:
    def __init__(self, table, records):
        self.table = table
        self.records = records

    @staticmethod
    def input_item(item):
        data = input("Input {}: ".format(item))
        return data


    @staticmethod
    def item_entering(item):
        data = input('Enter {}: '.format(item))
        return data

    @staticmethod
    def list():
        print('''
        1 -> Customer
        2 -> Bill
        3 -> Car
        4 -> CarSalesManager
        5 -> Car_CarSalesManager
        ''')

    @staticmethod
    def listofcolumn(table):
        if table == 1:
            print('''
            1 -> Customer'sFullName
            ''')
        elif table == 2:
            print('''
            1 -> Date
            2 -> CustomerID
            3 -> ManagerID 
            ''')
        elif table == 3:
            print('''
            1 -> Model
            2 -> CustomerID
            ''')
        elif table == 4:
            print('''
            1 -> Manager'sFullName
            ''')
        elif table == 5:
            print('''
            1 -> ManagerID
            2 -> VIN
            ''')

    def show_table(self):
        print('--------------------------------------')
        if self.table == 1:
            print('--------------Customer----------------')
            print('--------------------------------------')
            for row in self.records:
                print('CustomerID = {}'.format(row[0]))
                print('Customer\'sFullName = {}'.format(row[1]))
                print('--------------------------------------')
        elif self.table == 2:
            print('----------------Bill------------------')
            print('--------------------------------------')
            for row in self.records:
                print('BillID = {}'.format(row[0]))
                print('Date = {}'.format(row[1]))
                print('CustomerID = {}'.format(row[2]))
                print('ManagerID = {}'.format(row[3]))
                print('--------------------------------------')
        elif self.table == 3:
            print('----------------Car-------------------')
            print('--------------------------------------')
            for row in self.records:
                print('VIN = {}'.format(row[0]))
                print('Model = {}'.format(row[1]))
                print('CustomerID = {}'.format(row[2]))
                print('--------------------------------------')
        elif self.table == 4:
            print('----------CarSalesManager-------------')
            print('--------------------------------------')
            for row in self.records:
                print('ManagerID = {}'.format(row[0]))
                print('Manager\'sFullName = {}'.format(row[1]))
                print('--------------------------------------')
        elif self.table == 5:
            print('--------Car_CarSalesManager-----------')
            print('--------------------------------------')
            for row in self.records:
                print('SaleID = {}'.format(row[0]))
                print('ManagerID = {}'.format(row[1]))
                print('VIN = {}'.format(row[2]))
                print('--------------------------------------')


    def select_show_table(self):
        print('--------------------------------------')
        if self.table == 1:
            print('----------------foo-------------------')
            print('--------------------------------------')
            for row in self.records:
                print('Customer\'sFullName = {}'.format(row[0]))
                print('VIN = {}'.format(row[1]))
                print('Model = {}'.format(row[2]))
                print('--------------------------------------')

        elif self.table == 2:
            print('----------------foo-------------------')
            print('--------------------------------------')
            for row in self.records:
                print('Manager\'sFullName = {}'.format(row[0]))
                print('BillID = {}'.format(row[1]))
                print('Date = {}'.format(row[2]))
                print('--------------------------------------')

        elif self.table == 3:
            print('----------------foo-------------------')
            print('--------------------------------------')
            for row in self.records:
                print('Customer\'sFullName = {}'.format(row[0]))
                print('BillID = {}'.format(row[1]))
                print('Date = {}'.format(row[2]))
                print('--------------------------------------')



class Menu:
    @staticmethod
    def menu():
        while True:
            print('''
            1 -> Show one table
            2 -> Show all tables
            3 -> Insert information
            4 -> Delete information
            5 -> Update information
            6 -> Random information
            7 -> Select information
            8 -> Exit
            ''')
            choice = input('Please, make a choice: ')
            if choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    View.list()
                    numoftable = controller.valid_table()
                    records = Model.show_one_table(numoftable)
                    obj = View(numoftable, records)
                    obj.show_table()
                elif choice == 2:
                    for i in range(1, 6):
                        records = Model.show_one_table(i)
                        obj = View(i, records)
                        obj.show_table()
                elif choice == 3:
                    View.list()
                    numoftable = controller.valid_table()
                    goodnews = 'inserted'
                    cicle = True
                    while cicle:
                        if numoftable == 1:
                            custid = View.input_item("CustomerID")
                            custfullname = View.input_item("Customer\'sFullName")
                            row = [custid, custfullname]
                            istrue = controller.valid_data_to_insert(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.insertToCustomer(custid, custfullname, goodnews)
                        elif numoftable == 2:
                            billid = View.input_item("BillID")
                            date = View.input_item("Date")
                            custid = View.input_item("CustomerID")
                            manid = View.input_item("ManagerID")
                            row = [billid, date, custid, manid]
                            istrue = controller.valid_data_to_insert(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.insertToBill(custid, billid, manid, date, goodnews)
                        elif numoftable == 3:
                            vin = View.input_item("VIN")
                            mod = View.input_item("Model")
                            custid = View.input_item("CustomerID")
                            row = [vin, mod, custid]
                            istrue = controller.valid_data_to_insert(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.insertToCar(vin, mod, custid, goodnews)
                        elif numoftable == 4:
                            manid = View.input_item("ManagerID")
                            manfullname = View.input_item("Manager\'sFullName")
                            row = [manid, manfullname]
                            istrue = controller.valid_data_to_insert(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.insertToCarSalesManager(manid, manfullname, goodnews)
                        elif numoftable == 5:
                            saleid = View.input_item("SaleID")
                            manid = View.input_item("ManagerID")
                            vin = View.input_item("VIN")
                            row = [saleid, manid, vin]
                            istrue = controller.valid_data_to_insert(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.insertToCar_CarSalesManager(saleid, manid, vin, goodnews)
                        cont = True
                        while cont:
                            print('''
                            1 -> Continue insertion in this table
                            2 -> Stop insertion in this table
                            ''')
                            ch = input('Your choice -> ')
                            if ch == '2':
                                cicle = False
                                cont = False
                            elif ch == '1':
                                cont = False
                                pass
                            else:
                                print('Try again')
                            continue
                elif choice == 4:
                    View.list()
                    numoftable = controller.valid_table()
                    goodnews = 'deleted'
                    cicle = True
                    while cicle:
                        if numoftable == 1:
                            custid = View.input_item("CustomerID")
                            istrue = controller.valid_data_to_delete(custid)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.deleteInCustomer(custid, goodnews)

                        elif numoftable == 2:
                            billid = View.input_item("BillID")
                            istrue = controller.valid_data_to_delete(billid)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.deleteInBill(billid, goodnews)

                        elif numoftable == 3:
                            vin = View.input_item("VIN")
                            Model.deleteInCar(vin, goodnews)

                        elif numoftable == 4:
                            manid = View.input_item("ManagerID")
                            istrue = controller.valid_data_to_delete(manid)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.deleteInCarSalesManager(manid, goodnews)

                        elif numoftable == 5:
                            saleid = View.input_item("SaleID")
                            istrue = controller.valid_data_to_delete(saleid)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.deleteInCar_CarSalesManager(saleid, goodnews)
                        cont = True
                        while cont:
                            print('''
                            1 -> Continue delete in this table
                            2 -> Stop delete in this table
                            ''')
                            ch = input('Your choice -> ')
                            if ch == '2':
                                cicle = False
                                cont = False
                            elif ch == '1':
                                cont = False
                                pass
                            else:
                                print('Try again.')

                elif choice == 5:
                    View.list()
                    numoftable = controller.valid_table()
                    goodnews = 'updated'
                    cicle = True
                    while cicle:
                        if numoftable == 1:
                            custid = View.input_item("CustomerID")
                            custfullname = View.input_item("Customer\'sFullName")
                            row = [custid, custfullname]
                            istrue = controller.valid_data_to_update(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.updateCustomer(custid, custfullname, goodnews)
                        elif numoftable == 2:
                            billid = View.input_item("BillID")
                            date = View.input_item("Date")
                            row = [billid, date]
                            istrue = controller.valid_data_to_update(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.updateBill(billid, date, goodnews)

                        elif numoftable == 3:
                            vin = View.input_item("VIN")
                            mod = View.input_item("Model")
                            row = [vin, mod]
                            istrue = controller.valid_data_to_update(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.updateCar(vin, mod, goodnews)
                        elif numoftable == 4:
                            manid = View.input_item("ManagerID")
                            manfullname = View.input_item("Manager\'sFullName")
                            row = [manid, manfullname]
                            istrue = controller.valid_data_to_update(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.updateCarSalesManager(manid, manfullname, goodnews)
                        elif numoftable == 5:
                            controller.msg('You can not update something in this table. Sorry, try another.')
                            break
                        cont = True
                        while cont:
                            print('''
                            1 -> Continue update this table
                            2 -> Stop update this table 
                            ''')
                            ch = input('Your choice -> ')
                            if ch == '2':
                                cicle = False
                                cont = False
                            elif ch == '1':
                                cont = False
                                pass
                            else:
                                print('Try again.')

                elif choice == 6:
                    View.list()
                    numoftable = controller.valid_table()
                    goodnews = 'inserted randomly'
                    badnews = 'something went wrong.'
                    cicle = True
                    while cicle:
                        if numoftable == 1:
                            num = View.input_item("count of new elements")
                            num = controller.valid_data_to_random(num)
                            if num == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.randomToCustomer(num, goodnews, badnews)
                        elif numoftable == 2:
                            num = View.input_item("count of new elements")
                            num = controller.valid_data_to_random(num)
                            if num == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.randomToBill(num, goodnews, badnews)
                        elif numoftable == 3:
                            num = View.input_item("count of new elements")
                            num = controller.valid_data_to_random(num)
                            if num == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.randomToCar(num, goodnews, badnews)
                        elif numoftable == 4:
                            num = View.input_item("count of new elements")
                            num = controller.valid_data_to_random(num)
                            if num == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.randomToCarSalesManager(num, goodnews, badnews)
                        elif numoftable == 5:
                            num = View.input_item("count of new elements")
                            num = controller.valid_data_to_random(num)
                            if num == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                Model.randomToCar_CarSalesManager(num, goodnews, badnews)
                        cont = True
                        while cont:
                            print('''
                            1 -> Continue random in this table
                            2 -> Stop random in this table
                            ''')
                            ch = input('Your choice -> ')
                            if ch == '2':
                                cicle = False
                                cont = False
                            elif ch == '1':
                                cont = False
                                pass
                            else:
                                print('Try again.')
                elif choice == 7:
                    cicle = True
                    while cicle:
                        print('----------------------------------------')
                        print('1 -> Show Customer\'sFullName, VIN and Model where VIN includes some letter and where length of model name more or equal then some number')
                        print('----------------------------------------')
                        print('----------------------------------------')
                        print('2 -> Show the history of certain manager')
                        print('----------------------------------------')
                        print('----------------------------------------')
                        print('3 -> Show the history of certain customer')
                        print('----------------------------------------')
                        choice = controller.valid_choice_to_select()
                        if choice == 1:
                            letters = View.input_item("letters")
                            number = controller.valid_select_first()
                            records = Model.select_first(letters, number)
                            obj = View(choice, records)
                            obj.select_show_table()
                        elif choice == 2:
                            manfullname = View.input_item("Manager\'sFullName")
                            records = Model.select_second(manfullname)
                            obj = View(choice, records)
                            obj.select_show_table()
                        elif choice == 3:
                            custfullname = View.input_item("Customer\'sFullName")
                            records = Model.select_third(custfullname)
                            obj = View(choice, records)
                            obj.select_show_table()
                        cont = True
                        while cont:
                            print('''
                            1 -> Continue selection 
                            2 -> Stop selection 
                            ''')
                            ch = input('Your choice -> ')
                            if ch == '2':
                                cicle = False
                                cont = False
                            elif ch == '1':
                                cont = False
                                pass
                            else:
                                print('Try again.')

                elif choice == 8:
                    controller.msg('Good bye!')
                    break
                else:
                    controller.msg("Try something another.")
            else:
                print('Please, enter the digit.')
