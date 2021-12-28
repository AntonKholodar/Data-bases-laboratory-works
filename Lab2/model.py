import controller
import time

tables = {
    1: 'Customer',
    2: 'Bill',
    3: 'Car',
    4: 'CarSalesManager',
    5: 'Car_CarSalesManager',
}

class Model:

    @staticmethod
    def show_one_table(table):
        connect = controller.connection()
        cursor = connect.cursor()
        show = 'select * from public."{}"'.format(tables[table])
        print("SQL request => ", show)
        print('')
        cursor.execute(show)
        records = cursor.fetchall()
        cursor.close()
        controller.disconnection(connect)
        return records


    @staticmethod
    def insertToCustomer(custid, fullname, goodnews):
        badnews = '"CustomerID" = {} is existing already.'.format(custid)
        connect = controller.connection()
        cursor = connect.cursor()
        insert = 'do $$ begin if not exists (select "CustomerID" from "Customer" where "CustomerID" = {}) ' \
                 'then insert into "Customer"("CustomerID", "Customer\'\'sFullName") VALUES ({},\'{}\'); ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$;'.format(custid, custid, fullname, goodnews, badnews)
        cursor.execute(insert)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def insertToBill(custid, billid, manid, date, goodnews):
        badnews = '"CustomerID" = {} is not exist or "BillID" = {} is existing already or "ManagerID" = {} is not exist.'.format(custid, billid, manid)
        connect = controller.connection()
        cursor = connect.cursor()
        insert = 'do $$ begin if exists (select "CustomerID" from "Customer" where "CustomerID" = {}) and not exists ' \
                 '(select "BillID" from "Bill" where "BillID" = {}) and exists (select "ManagerID" from "CarSalesManager" where "ManagerID" = {}) then ' \
                 'insert into "Bill"("BillID", "Date", "CustomerID", "ManagerID") values ({}, \'{}\', {}, {}); ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(custid, billid, manid, billid, date, custid, manid, goodnews, badnews)
        cursor.execute(insert)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def insertToCar(vin, mod, custid, goodnews):
        badnews = '"VIN" = "{}" is existing or "CustomerID" = {} is not existing.'.format(vin, custid)
        connect = controller.connection()
        cursor = connect.cursor()
        insert = 'do $$ begin if exists (select "CustomerID" from "Customer" where "CustomerID" = {}) ' \
                 'and not exists (select "VIN" from "Car" where "VIN" = \'{}\') then ' \
                 'insert into "Car"("VIN", "Model", "CustomerID") values (\'{}\', \'{}\', {}); ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(custid, vin, vin, mod, custid, goodnews, badnews)
        cursor.execute(insert)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def insertToCarSalesManager(manid, manfullname, goodnews):
        badnews = '"ManagerID" = {} is existing already.'.format(manid)
        connect = controller.connection()
        cursor = connect.cursor()
        insert = 'do $$ begin if not exists (select "ManagerID" from "CarSalesManager" where "ManagerID" = {}) ' \
                 'then insert into "CarSalesManager"("ManagerID", "Manager\'\'sFullName") values ({}, \'{}\'); ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(manid, manid, manfullname, goodnews, badnews)
        cursor.execute(insert)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def insertToCar_CarSalesManager(saleid, manid, vin, goodnews):
        badnews = '"ManagerID" = {} is not exist or "SaleID" = {} is existing already or "VIN" = "{}" is not exist.'.format(manid, saleid, vin)
        connect = controller.connection()
        cursor = connect.cursor()
        insert = 'do $$ begin if exists (select "ManagerID" from "CarSalesManager" where "ManagerID" = {}) and ' \
                 'exists (select "VIN" from "Car" where "VIN" = \'{}\') and not exists (select "SaleID" from "Car_CarSalesManager" where "SaleID" = {}) ' \
                 'then insert into "Car_CarSalesManager"("SaleID", "ManagerID", "VIN") values ({}, {}, \'{}\'); ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(manid, vin, saleid, saleid, manid, vin, goodnews, badnews)
        cursor.execute(insert)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)


    @staticmethod
    def deleteInCustomer(custid, goodnews):
        badnews = '"CustomerID" = {} is not exist or there are some dependencies on it.'.format(custid)
        connect = controller.connection()
        cursor = connect.cursor()
        delete = 'do $$ begin if exists (select "CustomerID" from "Customer" where "CustomerID" = {}) ' \
                 'and not exists (select "CustomerID" from "Bill" where "CustomerID" = {}) and not exists ' \
                 '(select "CustomerID" from "Car" where "CustomerID" = {}) then ' \
                 'delete from "Customer" where "CustomerID" = {}; ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(custid, custid, custid, custid, goodnews, badnews)
        cursor.execute(delete)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def deleteInBill(billid, goodnews):
        badnews = '"BillID" = {} is not exist.'.format(billid)
        connect = controller.connection()
        cursor = connect.cursor()
        delete = 'do $$ begin if exists (select "BillID" from "Bill" where "BillID" = {}) ' \
                 'then delete from "Bill" where "BillID" = {}; ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(billid, billid, goodnews, badnews)
        cursor.execute(delete)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)


    @staticmethod
    def deleteInCar(vin, goodnews):
        badnews = '"VIN" = "{}" is not exist or there are some dependencies on it.'.format(vin)
        connect = controller.connection()
        cursor = connect.cursor()
        delete = 'do $$ begin if exists (select "VIN" from "Car" where "VIN" = \'{}\') and ' \
                 'not exists (select "VIN" from "Car_CarSalesManager" where "VIN" = \'{}\') then ' \
                 'delete from "Car" where "VIN" = \'{}\'; ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '. format(vin, vin, vin, goodnews, badnews)
        cursor.execute(delete)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def deleteInCarSalesManager(manid, goodnews):
        badnews = '"ManagerID" = {} is not exist or there are some dependencies on it.'.format(manid)
        connect = controller.connection()
        cursor = connect.cursor()
        delete = 'do $$ begin if exists (select "ManagerID" from "CarSalesManager" where "ManagerID" = {}) and ' \
                 'not exists (select "ManagerID" from "Bill" where "ManagerID" = {}) and not exists ' \
                 '(select "ManagerID" from "Car_CarSalesManager" where "ManagerID" = {}) then ' \
                 'delete from "CarSalesManager" where "ManagerID" = {}; ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '. format(manid, manid, manid, manid, goodnews, badnews)
        cursor.execute(delete)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def deleteInCar_CarSalesManager(saleid, goodnews):
        badnews = '"SaleID" = {} is not exist.'.format(saleid)
        connect = controller.connection()
        cursor = connect.cursor()
        delete = 'do $$ begin if exists (select "SaleID" from "Car_CarSalesManager" where "SaleID" = {}) then ' \
                 'delete from "Car_CarSalesManager" where "SaleID" = {};' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(saleid, saleid, goodnews, badnews)
        cursor.execute(delete)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def updateCustomer(custid, custfullname, goodnews):
        badnews = '"CustomerID" = {} is not exist.'.format(custid)
        connect = controller.connection()
        cursor = connect.cursor()
        update = 'do $$ begin if exists (select "CustomerID" from "Customer" where "CustomerID" = {}) then ' \
                 'update "Customer" set "Customer\'\'sFullName" = \'{}\' where "CustomerID" = {}; ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(custid, custfullname, custid, goodnews, badnews)
        cursor.execute(update)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def updateBill(billid, date, goodnews):
        badnews = '"BillID" = {} is not exist'.format(billid)
        connect = controller.connection()
        cursor = connect.cursor()
        update = 'do $$ begin if exists (select "BillID" from "Bill" where "BillID" = {}) then ' \
                 'update "Bill" set "Date" = \'{}\' where "BillID" = {}; ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(billid, date, billid, goodnews, badnews)
        cursor.execute(update)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def updateCar(vin, mod, goodnews):
        badnews = '"VIN" = "{}" is not exist'.format(vin)
        connect = controller.connection()
        cursor = connect.cursor()
        update = 'do $$ begin if exists (select "VIN" from "Car" where "VIN" = \'{}\') then ' \
                 'update "Car" set "Model" = \'{}\' where "VIN" = \'{}\'; ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(vin, mod, vin, goodnews, badnews)
        cursor.execute(update)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def updateCarSalesManager(manid, manfullname, goodnews):
        badnews = '"ManagerID" = "{}" is not exist'.format(manid)
        connect = controller.connection()
        cursor = connect.cursor()
        update = 'do $$ begin if exists (select "ManagerID" from "CarSalesManager" where "ManagerID" = {}) then ' \
                 'update "CarSalesManager" set "Manager\'\'sFullName" = \'{}\' where "ManagerID" = {}; ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(manid, manfullname, manid, goodnews, badnews)
        cursor.execute(update)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def select_first(vin, modlen):
        connect = controller.connection()
        cursor = connect.cursor()
        select = 'select "Customer\'\'sFullName", "VIN", "Model" from (select c."Customer\'\'sFullName", p."VIN", p."Model" ' \
                 'from "Customer" c inner join "Car" p on p."CustomerID" = c."CustomerID" where p."VIN" like \'%{}%\' and length(p."Model") >= {} ' \
                 'group by c."Customer\'\'sFullName", p."VIN", p."Model") as foo'.format(vin, modlen)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        records = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)
        return records

    @staticmethod
    def select_second(manfullname):
        connect = controller.connection()
        cursor = connect.cursor()
        select = 'select "Manager\'\'sFullName", "BillID", "Date" from (select c."Manager\'\'sFullName", p."BillID", p."Date" ' \
                 'from "CarSalesManager" c inner join "Bill" p on p."ManagerID" = c."ManagerID" where c."Manager\'\'sFullName" like ' \
                 '\'{}\' group by c."Manager\'\'sFullName", p."BillID", p."Date") as foo'. format(manfullname)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        records = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)
        return records

    @staticmethod
    def select_third(custfullname):
        connect = controller.connection()
        cursor = connect.cursor()
        select = 'select "Customer\'\'sFullName", "BillID", "Date" from (select c."Customer\'\'sFullName", p."BillID", p."Date" ' \
                 'from "Customer" c inner join "Bill" p on p."CustomerID" = c."CustomerID" where c."Customer\'\'sFullName" like ' \
                 '\'{}\' group by c."Customer\'\'sFullName", p."BillID", p."Date") as foo'.format(custfullname)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        records = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)
        return records

    @staticmethod
    def randomToCustomer(num, goodnews, badnews):
        connect = controller.connection()
        cursor = connect.cursor()
        insert =  'do $$ begin if (1=1) then ' \
                  'insert into "Customer"("CustomerID", "Customer\'\'sFullName") select random()*99999, ' \
                 'substr(characters, (random() * length(characters) + 1)::integer, 10) ' \
                 'from (VALUES(\'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM\')) as symbols(characters), generate_series(1, {}); ' \
                 'raise notice \'{}\'; ' \
                  'else raise notice \'{}\'; ' \
                  'end if; end $$; '.format(num, goodnews, badnews)
        controller.msg("SQL request -> {}".format(insert))
        cursor.execute(insert)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def randomToBill(num, goodnews, badnews):
        connect = controller.connection()
        cursor = connect.cursor()
        insert = 'do $$ begin if  (1=1) then ' \
                 'insert into "Bill"("BillID", "Date", "CustomerID", "ManagerID") select random()*99999, ' \
                 'timestamp \'2020-01-10\' - random() * (timestamp \'2020-01-20\' - timestamp \'2021-01-10\'), ' \
                 '(select "CustomerID" from "Customer" order by random() limit 1), ' \
                 '(select "ManagerID" from "CarSalesManager" order by random() limit 1) ' \
                 'from generate_series(1, {}); ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(num, goodnews, badnews)
        controller.msg("SQL request -> {}".format(insert))
        cursor.execute(insert)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def randomToCar(num, goodnews, badnews):
        connect = controller.connection()
        cursor = connect.cursor()
        insert = 'do $$ begin if (1=1) then ' \
                 'insert into "Car"("VIN", "Model", "CustomerID") select substr(characters, (random() * length(characters) + 1)::integer, 10), ' \
                 'substr(characters, (random() * length(characters) + 1)::integer, 6), (select "CustomerID" from "Customer" order by random() limit 1) ' \
                 'from (VALUES(\'qwertyuiopasdfghjklzxcvbnm123456789QWERTYUIOPASDFGHJKLZXCVBNM\')) as symbols(characters), generate_series(1, {}); ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(num, goodnews, badnews)
        controller.msg("SQL request -> {}".format(insert))
        cursor.execute(insert)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)

    @staticmethod
    def randomToCarSalesManager(num, goodnews, badnews):
        connect = controller.connection()
        cursor = connect.cursor()
        insert = 'do $$ begin if (1=1) then ' \
                 'insert into "CarSalesManager"("ManagerID", "Manager\'\'sFullName") select random()*99999, ' \
                 'substr(characters, (random() * length(characters) + 1)::integer, 10) ' \
                 'from (VALUES(\'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM\')) as symbols(characters), generate_series(1, {}); ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(num, goodnews, badnews)
        controller.msg("SQL request -> {}".format(insert))
        cursor.execute(insert)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)


    @staticmethod
    def randomToCar_CarSalesManager(num, goodnews, badnews):
        connect = controller.connection()
        cursor = connect.cursor()
        insert = 'do $$ begin if (1=1) then ' \
                 'insert into "Car_CarSalesManager"("SaleID", "ManagerID", "VIN") select random()*99999, ' \
                 '(select "ManagerID" from "CarSalesManager" order by random() limit 1), ' \
                 '(select "VIN" from "Car" order by random() limit 1) from generate_series(1, {}); ' \
                 'raise notice \'{}\'; ' \
                 'else raise notice \'{}\'; ' \
                 'end if; end $$; '.format(num, goodnews, badnews)
        controller.msg("SQL request -> {}".format(insert))
        cursor.execute(insert)
        connect.commit()
        controller.msg(connect.notices)
        cursor.close()
        controller.disconnection(connect)





