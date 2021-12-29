import controller
from model import Model, Customer, Bill, Car, CarSalesManager, Car_CarSalesManager
import psycopg2



class View:
    def __init__(self, table, datas):
        self.table = table
        self.datas = datas

    @staticmethod
    def input_item(item):
        data = input("Input {}: ".format(item))
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
                6 -> Exit
                ''')
            choice = input('Please, make a choice: ')
            if choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    View.list()
                    numoftable = controller.valid_table()
                    Model.show_one_table(numoftable)
                elif choice == 2:
                    for i in range(1, 6):
                        Model.show_one_table(i)
                elif choice == 3:
                    cicle = True
                    View.list()
                    numoftable = controller.valid_table()
                    while cicle:
                        if numoftable == 1:
                            custid = View.input_item("CustomerID")
                            custfullname = View.input_item("Customer\'sFullName")
                            row = [custid, custfullname]
                            custid = int(custid)
                            trueis = controller.valid_to_insert_customer(custid, Customer)
                            istrue = controller.valid_data_to_insert(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            elif trueis == 0:
                                controller.msg('CustomerID = {} is exist.'.format(custid))
                            else:
                                Model.insertToCustomer(custid, custfullname)
                                controller.msg('inserted')
                        elif numoftable == 2:
                            billid = View.input_item("BillID")
                            date = View.input_item("Date")
                            custid = View.input_item("CustomerID")
                            manid = View.input_item("ManagerID")
                            row = [billid, date, custid, manid]
                            billid = int(billid)
                            custid = int(custid)
                            manid = int(manid)
                            trueis = controller.valid_to_insert_bill(billid, custid, manid, Bill, Customer, CarSalesManager)
                            istrue = controller.valid_data_to_insert(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            elif trueis == 0:
                                controller.msg('BillID = {} is exist or CustomerID = {} is not exist or ManagerID = {} is not exist.'.format(billid, custid, manid))
                            else:
                                Model.insertToBill(billid, date, custid, manid)
                                controller.msg('inserted')
                        elif numoftable == 3:
                            vin = View.input_item("VIN")
                            mod = View.input_item("Model")
                            custid = View.input_item("CustomerID")
                            row = [vin, mod, custid]
                            custid = int(custid)
                            trueis = controller.valid_to_insert_car(vin, custid, Car, Customer)
                            istrue = controller.valid_data_to_insert(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            elif trueis == 0:
                                controller.msg('VIN = \'{}\' is exist or CustomerID = {} is not exist.'.format(vin, custid))
                            else:
                                Model.insertToCar(vin, mod, custid)
                                controller.msg('inserted')
                        elif numoftable == 4:
                            manid = View.input_item("ManagerID")
                            manfullname = View.input_item("Manager\'sFullName")
                            row = [manid, manfullname]
                            manid = int(manid)
                            trueis = controller.valid_to_insert_carsalesmanager(manid, CarSalesManager)
                            istrue = controller.valid_data_to_insert(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            elif trueis == 0:
                                controller.msg('ManagerID = {} is exist.'.format(manid))
                            else:
                                Model.insertToCarSalesManager(manid, manfullname)
                                controller.msg('inserted')
                        elif numoftable == 5:
                            saleid = View.input_item("SaleID")
                            manid = View.input_item("ManagerID")
                            vin = View.input_item("VIN")
                            row = [saleid, manid, vin]
                            saleid = int(saleid)
                            manid = int(manid)
                            trueis = controller.valid_to_insert_car_carsalesmanager(saleid, vin, manid, Car_CarSalesManager, Car, CarSalesManager)
                            istrue = controller.valid_data_to_insert(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            elif trueis == 0:
                                controller.msg('SaleID = {} is exist or VIN = \'{}\' is not exist or ManagerID = {} is not exist.'.format(saleid, vin, manid))
                            else:
                                Model.insertToCar_CarSalesManager(saleid, manid, vin)
                                controller.msg('inserted')
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
                    cicle = True
                    while cicle:
                        if numoftable == 1:
                            custid = View.input_item("CustomerID")
                            istrue = controller.valid_data_to_delete(custid)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                                continue
                            else:
                                custid = int(custid)
                                trueis = controller.valid_to_delete_customer(custid, Customer, Bill, Car)
                                if trueis == 0:
                                    controller.msg('Try something another.')
                                    break
                                else:
                                    Model.deleteInCustomer(custid)
                                    controller.msg('deleted')

                        elif numoftable == 2:
                            billid = View.input_item("BillID")
                            istrue = controller.valid_data_to_delete(billid)
                            billid = int(billid)
                            trueis = controller.valid_to_delete_bill(billid, Bill)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            elif trueis == 0:
                                controller.msg('Try something another.')
                            else:
                                Model.deleteBill(billid)
                                controller.msg('deleted')
                        elif numoftable == 3:
                            vin = View.input_item("VIN")
                            trueis = controller.valid_to_delete_car(vin, Car, Car_CarSalesManager)
                            if trueis == 0:
                                controller.msg('Try something another.')
                                break
                            else:
                                Model.deleteCar(vin)
                                controller.msg('deleted')
                        elif numoftable == 4:
                            manid = View.input_item("ManagerID")
                            istrue = controller.valid_data_to_delete(manid)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                                continue
                            else:
                                manid = int(manid)
                                trueis = controller.valid_to_delete_carsalesmanager(manid, CarSalesManager, Bill, Car_CarSalesManager)
                                if trueis == 0:
                                    controller.msg('Try something another.')
                                    continue
                                else:
                                    Model.deleteCarSalesManager(manid)
                                    controller.msg('deleted')
                        elif numoftable == 5:
                            saleid = View.input_item("SaleID")
                            istrue = controller.valid_data_to_delete(saleid)
                            saleid = int(saleid)
                            trueis = controller.valid_to_delete_car_carsalesmanager(saleid, Car_CarSalesManager)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            elif trueis == 0:
                                controller.msg('Try something another.')
                                continue
                            else:
                                Model.deleteCar_CarSalesManager(saleid)
                                controller.msg('deleted')
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
                    cicle = True
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
                                custid = int(custid)
                                trueis = controller.valid_to_update_customer(custid, Customer)
                                if trueis == 0:
                                    controller.msg('CustomerID = {} is not exist'.format(custid))
                                else:
                                    Model.updateCustomer(custid, custfullname)
                                    controller.msg('updated')
                        elif numoftable == 2:
                            billid = View.input_item("BillID")
                            date = View.input_item("Date")
                            row = [billid, date]
                            istrue = controller.valid_data_to_update(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                billid = int(billid)
                                trueis = controller.valid_to_update_bill(billid, Bill)
                                if trueis == 0:
                                    controller.msg('BillID = {} is not exist'.format(billid))
                                else:
                                    Model.updateBill(billid, date)
                                    controller.msg('updated')
                        elif numoftable == 3:
                            vin = View.input_item("VIN")
                            mod = View.input_item("Model")
                            row = [vin, mod]
                            istrue = controller.valid_data_to_update(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                trueis = controller.valid_to_update_car(vin, Car)
                                if trueis == 0:
                                    controller.msg('VIN = \'{}\' is not exist'.format(vin))
                                else:
                                    Model.updateCar(vin, mod)
                                    controller.msg('updated')
                        elif numoftable == 4:
                            manid = View.input_item("ManagerID")
                            manfullname = View.input_item("Manager\'sFullName")
                            row = [manid, manfullname]
                            istrue = controller.valid_data_to_update(numoftable, row)
                            if istrue == 0:
                                controller.msg('Your data are invalid. Try again.')
                            else:
                                manid = int(manid)
                                trueis = controller.valid_to_update_carsalesmanager(manid, CarSalesManager)
                                if trueis == 0:
                                    controller.msg('ManagerID = {} is not exist'.format(manid))
                                else:
                                    Model.updateCarSalesManager(manid, manfullname)
                                    controller.msg('updated')
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
                    controller.msg('Good bye!')
                    break
                else:
                    controller.msg("Try something another.")
            else:
                controller.msg("Please, enter the digit.")