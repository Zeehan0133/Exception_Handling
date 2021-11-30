"""
@Author: Zeehan 
@Date: 2021-29-11 19:00:30
@Title :  Exception handling in csv file
"""

import csv 
try:
    def create():
        """
        Description: create() function for write something in csv file
        Parameter: newline=, obj
        Return: True
        """
        with open("details.csv","w",newline="") as obj:
            fobj=csv.writer(obj)
            fobj.writerow(['Roll','Name',"Total"])
            while True:
                Roll= int(input("Enter a Roll no: "))
                Name=input("Enter name :")
                Total= int(input("Enter total marks :"))
                record=[Roll, Name, Total]
                record.count([Roll, Name, Total])
                fobj.writerow(record)

            
                ch=int(input("press 1 for more \n press 2 for exit \n enter your choice :"))
                if ch==2:
                    break
    def count():
        """
        Description: create a function to count the rows inside the csv file 
        Parameter: obj
        Return: 
        """
    
        with open("details.csv","r") as obj:
            fobj = csv.reader(obj,delimiter = ",")
            next(fobj)
            data = list(fobj)
            row_count = len(data)
            print("Number of rows",row_count)


    def getheader():
        """
        Description: create a function to print header of the file 
        Parameter: obj
        Return: 
        """
        with open("details.csv", 'r') as obj:
            fobj = csv.DictReader(obj)
            fieldnames = fobj.fieldnames
            print("this is header of the file",fieldnames)

    def display():
        """
        Description: create a function to display the contant of the file 
        Parameter: obj
        Return: 
        """
        with open("details.csv","r") as obj:
            fobj=csv.reader(obj)
            for i in fobj:
            # fob=row=row+i
            # print("no of rows :",fobj)
                print(i)

    def search():
        """
        Description: create a function search the items in list 
        Parameter: obj
        Return: 
        """
    
        with open("details.csv","r") as obj:

            fobj=csv.reader(obj)
            next(fobj)
            for i in fobj:
            #if i.len(<1)
                if int(i[2])>=60:
                    print("marks greater then 60:",i)
    
                    





    if __name__=='__main__': 
        create()
        count()
        getheader()
        display()
        search()
    
except Exception as e:
    print(e)
finally:
    print("End of the program")  
