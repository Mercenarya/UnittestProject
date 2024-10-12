import unittest
import datetime
import MelliaSQLite
from MelliaSQLite import mycursor,Setbill

class bill():
    '''Create table Bill '''
    def setupbill():
        try:
            mycursor.execute(Setbill)
            return "Bill setup"
        except Exception as error:
            return error
    
    '''Insert all records into Table'''
    def insertform():
        time = '17/10/2024'
        print(time)
        form = ["1",50000,time,"Banking",15000]
        insert = '''
            INSERT INTO Mellia_bill (tb,total,settime,method,coupon) 
            VALUES (?,?,?,?,?)
        '''
        try:
            mycursor.execute(insert,form)
            return 'New record inserted'
        except Exception as error:
            return error
        
    '''Query total money'''
    def querybilltotal():
        tb = "1"
        queries = f'SELECT total FROM Mellia_bill WHERE tb = {tb}'
        try:
            mycursor.execute(queries)
            for obj in mycursor.fetchall():
                return f"{obj[0]}"
        except Exception as error:
            return error
        
    '''Query settime'''
    def querybillsettime():
        tb = "1"
        queries = f'SELECT settime FROM Mellia_bill WHERE tb = {tb}'
        try:
            mycursor.execute(queries)
            for obj in mycursor.fetchall():
                return f"{obj[0]}"
        except Exception as error:
            return error 
        
    '''Query payment method'''
    def querybillmethod():
        tb = "1"
        queries = f'SELECT method FROM Mellia_bill WHERE tb = {tb}'
        try:
            mycursor.execute(queries)
            for obj in mycursor.fetchall():
                return f"{obj[0]}"
        except Exception as error:
            return error 
        
    '''Query coupon'''
    def querybillcoupon():
        tb = "1"
        queries = f'SELECT coupon FROM Mellia_bill WHERE tb = {tb}'
        try:
            mycursor.execute(queries)
            for obj in mycursor.fetchall():
                return f"{obj[0]}"
        except Exception as error:
            return error 
        
        
    def deletetable():
        tb = '1'
        quit = f"DELETE FROM Mellia_bill WHERE tb = '{tb}'"
        try:
            mycursor.execute(quit)
            return 'Delete record'
        except Exception as error:
            return error


class TestBill(unittest.TestCase):
    '''Total Money'''
    def testtotal(self):
        self.expected = 50000
        self.assertEqual(self.expected,bill.querybilltotal())

    '''Settime'''
    def testtime(self):
        self.expected = '17/10/2024'
        self.assertEqual(self.expected,bill.querybillsettime())

    '''Payment method'''
    def testmethod(self):
        self.expected = 'Banking'
        self.assertEqual(self.expected,bill.querybillmethod())

    '''Coupon'''
    def testcoupon(self):
        self.expected = 15000
        self.assertEqual(self.expected,bill.querybillcoupon())



if __name__ == "__main__":

    '''Running Test functions'''

    print(bill.setupbill())
    print(bill.insertform())
    print(bill.querybilltotal())
    print(bill.querybillsettime())
    unittest.main()
   
