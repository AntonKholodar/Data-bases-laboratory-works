from sqlalchemy.orm import relationship, backref
from controller import Base, s, engine
import psycopg2
from sqlalchemy import *

metadata = MetaData()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

class Customer(Base):
    __tablename__ = 'Customer'
    CustomerID = Column(INTEGER, primary_key=True, nullable=False, unique=True)
    CustomersFullName = Column(VARCHAR, nullable=False)
    Bill = relationship("Bill")
    Car = relationship("Car")

    def __init__(self, CustomerID, CustomersFullName):
        self.CustomerID = CustomerID
        self.CustomersFullName = CustomersFullName

    def __repr__(self):
        return "<Customer(CustomerID = {}, CustomersFullName = '{}')>".format(self.CustomerID, self.CustomersFullName)

class Bill(Base):
    __tablename__ = 'Bill'
    BillID = Column(INTEGER, primary_key=True, nullable=False, unique=True)
    Date = Column(TIMESTAMP, nullable=False)
    CustomerID = Column(INTEGER, ForeignKey('Customer.CustomerID'), nullable=False)
    ManagerID = Column(INTEGER, ForeignKey('CarSalesManager.ManagerID'), nullable=False)

    def __init__(self, BillID, Date, CustomerID, ManagerID):
        self.BillID = BillID
        self.Date = Date
        self.CustomerID = CustomerID
        self.ManagerID = ManagerID

    def __repr__(self):
        return "<Bill(BillID = {}, Date = '{}', CustomerID = {}, ManagerID = {})>"\
            .format(self.BillID, self.Date, self.CustomerID, self.ManagerID)

class Car(Base):
    __tablename__ = 'Car'
    VIN = Column(VARCHAR, primary_key=True, nullable=False, unique=True)
    Model = Column(VARCHAR, nullable=False)
    CustomerID = Column(INTEGER, ForeignKey('Customer.CustomerID'), nullable=False)
    Car_CarSalesManager = relationship("Car_CarSalesManager")

    def __init__(self, VIN, Model, CustomerID):
        self.VIN = VIN
        self.Model = Model
        self.CustomerID = CustomerID

    def __repr__(self):
        return "<Car(VIN = '{}', Model = '{}', CustomerID = {})>" \
            .format(self.VIN, self.Model, self.CustomerID)

class CarSalesManager(Base):
    __tablename__ = 'CarSalesManager'
    ManagerID = Column(INTEGER, primary_key=True, nullable=False, unique=True)
    ManagersFullName = Column(VARCHAR, nullable=False)
    Bill = relationship("Bill")
    Car_CarSalesManager = relationship("Car_CarSalesManager")

    def __init__(self, ManagerID, ManagersFullName):
        self.ManagerID = ManagerID
        self.ManagersFullName = ManagersFullName

    def __repr__(self):
        return "<CarSalesManager(ManagerID = {}, ManagersFullName = '{}')>".format(self.ManagerID, self.ManagersFullName)

class Car_CarSalesManager(Base):
    __tablename__ = 'Car_CarSalesManager'
    SaleID = Column(INTEGER, primary_key=True, nullable=False, unique=True)
    VIN = Column(VARCHAR, ForeignKey('Car.VIN'), nullable=False)
    ManagerID = Column(INTEGER, ForeignKey('CarSalesManager.ManagerID'), nullable=False)

    def __init__(self, SaleID, VIN, ManagerID):
        self.SaleID = SaleID
        self.VIN = VIN
        self.ManagerID = ManagerID

    def __repr__(self):
        return "<Car_CarSalesManager(SaleID = {}, VIN = '{}', ManagerID = {})>".format(self.SaleID, self.VIN, self.ManagerID)



class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    @staticmethod
    def show_one_table(numoftable: int):
        if numoftable == 1:
            for class_instance in s.query(Customer).order_by(Customer.CustomerID.asc()).all():
                print(class_instance)
        elif numoftable == 2:
            for class_instance in s.query(Bill).order_by(Bill.BillID.asc()).all():
                print(class_instance)
        elif numoftable == 3:
            for class_instance in s.query(Car).order_by(Car.VIN.asc()).all():
                print(class_instance)
        elif numoftable == 4:
            for class_instance in s.query(CarSalesManager).order_by(CarSalesManager.ManagerID.asc()).all():
                print(class_instance)
        elif numoftable == 5:
            for class_instance in s.query(Car_CarSalesManager).order_by(Car_CarSalesManager.SaleID.asc()).all():
                print(class_instance)


    @staticmethod
    def insertToCustomer(CustomerID: INTEGER, CustomersFullName: VARCHAR) -> None:
        insert = Customer(CustomerID = CustomerID, CustomersFullName = CustomersFullName)
        s.add(insert)
        s.commit()

    @staticmethod
    def insertToBill(BillID: INTEGER, Date: TIMESTAMP, CustomerID: INTEGER, ManagerID = INTEGER):
        insert = Bill(BillID = BillID, Date = Date, CustomerID = CustomerID, ManagerID = ManagerID)
        s.add(insert)
        s.commit()

    @staticmethod
    def insertToCar(VIN: VARCHAR, Model: VARCHAR, CustomerID: INTEGER):
        insert = Car(VIN = VIN, Model = Model, CustomerID = CustomerID)
        s.add(insert)
        s.commit()

    @staticmethod
    def insertToCarSalesManager(ManagerID: INTEGER, ManagersFullName: VARCHAR):
        insert = CarSalesManager(ManagerID = ManagerID, ManagersFullName = ManagersFullName)
        s.add(insert)
        s.commit()

    @staticmethod
    def insertToCar_CarSalesManager(SaleID: INTEGER, ManagerID: INTEGER, VIN: VARCHAR):
        insert = Car_CarSalesManager(SaleID = SaleID, ManagerID = ManagerID, VIN = VIN)
        s.add(insert)
        s.commit()

    @staticmethod
    def deleteCustomer(CustomerID: INTEGER):
        s.query(Customer).filter_by(CustomerID = CustomerID).delete()
        s.commit()

    @staticmethod
    def deleteBill(BillID: INTEGER):
        s.query(Bill).filter_by(BillID = BillID).delete()
        s.commit()

    @staticmethod
    def deleteCar(VIN: VARCHAR):
        s.query(Car).filter_by(VIN = VIN).delete()
        s.commit()

    @staticmethod
    def deleteCarSalesManager(ManagerID: INTEGER):
        s.query(CarSalesManager).filter_by(ManagerID = ManagerID).delete()
        s.commit()

    @staticmethod
    def deleteCar_CarSalesManager(SaleID: INTEGER):
        s.query(Car_CarSalesManager).filter_by(SaleID = SaleID).delete()
        s.commit()

    @staticmethod
    def updateCustomer(CustomerID: INTEGER, CustomersFullName: VARCHAR):
        s.query(Customer).filter_by(CustomerID = CustomerID) \
            .update({Customer.CustomersFullName: CustomersFullName})
        s.commit()

    @staticmethod
    def updateBill(BillID: INTEGER, Date: TIMESTAMP):
        s.query(Bill).filter_by(BillID = BillID) \
            .update({Bill.Date: Date})
        s.commit()

    @staticmethod
    def updateCar(VIN: VARCHAR, Model: VARCHAR):
        s.query(Car).filter_by(VIN = VIN) \
            .update({Car.Model: Model})
        s.commit()

    @staticmethod
    def updateCarSalesManager(ManagerID: INTEGER, ManagerasFullName: VARCHAR):
        s.query(CarSalesManager).filter_by(ManagerID = ManagerID) \
            .update({CarSalesManager.ManagersFullName: ManagerasFullName})
        s.commit()