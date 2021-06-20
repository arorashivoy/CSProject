import mysql.connector as sqltor
from sys import exit

mycon = sqltor.connect(host= "localhost",user="root",database="test")
cursor=mycon.cursor()
try:
    cursor.execute("Create table EMPLOYEE (\
                    ID     int(3)    primary key,\
                    Ename  char(20),\
                    Cntno  bigint(10),\
                    Age    int(3));")
except:
    pass
try:
    cursor.execute("Create table DEPARTMENT (\
                    ID     int(3)    primary key,\
                    DEPT   varchar(6),\
                    City   varchar(20),\
                    Salary int(9));")
except:
    pass
try:
    cursor.execute("Create table WDATA (\
                    ID     int(3)    primary key,\
                    WH     decimal(10,2),\
                    LD     int(3),\
                    PRJ    int(3),\
                    CPRJ   int(3),\
                    ICPRJ  int(3));")
except:
    pass

mycon.commit()
try:
    cursor.execute("INSERT INTO EMPLOYEE \
                    VALUES(101, 'eshaan', 7394065702, 50);")
except:
    pass
try:
    cursor.execute("INSERT INTO EMPLOYEE \
                    VALUES (102, 'ashwin', 9875647354, 45);")
except:
    pass
try:
    cursor.execute("INSERT INTO EMPLOYEE \
                    VALUES (103,'ISHRIT', 9453892340, 30);")
except:
    pass
try:
    cursor.execute("INSERT INTO DEPARTMENT \
                    VALUES(101,'sales', 'delhi', 9000);")
except:
    pass
try:
    cursor.execute("INSERT INTO DEPARTMENT \
                    VALUES(102,'tally','delhi', 42069);")
except:
    pass
try:
    cursor.execute("INSERT INTO DEPARTMENT \
                    VALUES(103,'it','delhi', 9000000);")
except:
    pass
try:
    cursor.execute("INSERT INTO WDATA \
                    VALUES(101,69,30,2,1,1);")
except:
    pass
try:
    cursor.execute("INSERT INTO WDATA \
                    VALUES(102,65.5,6,5,4,1);")
except:
    pass
try:
    cursor.execute("INSERT INTO WDATA \
                    VALUES(103,60.2,5,5,1,4);")
except:
    pass

mycon.commit()

def add():
    flag = True

    while flag:
        print("PRESS 1: to add data to Employee table")
        print("PRESS 2: to add data to Department table")
        print("PRESS 3: to add data to WData table")
        print("PRESS 4: to return to the main menu ")

        flag = False
        choice = int(input())

        if choice == 1:
            addEmployee()
        elif choice == 2:
            addDepartment()
        elif choice == 3:
            addWdata()
        elif choice == 4:
            return None
        else:
            print("Enter a valid choice ")
            flag  = True

def addEmployee():
    id = int(input("Enter id: "))
    ename = input("Enter Ename: ")
    cntNo = int(input("Enter Cnt No.: "))
    age = int(input("Enter Age: "))

    cursor.execute("INSERT INTO EMPLOYEE \
                    VALUES ({},'{}', {}, {});".format(id,ename,cntNo,age))
    print("\nRecord successfully added \n")

def addDepartment():
    id = int(input("Enter id: "))
    dept = input("Enter Department: ")
    city = input("Enter city: ")
    salary = int(input("Enter salary: "))

    cursor.execute("INSERT INTO DEPARTMENT \
                    VALUES ({},'{}','{}',{});".format(id, dept,city,salary))
    print("\nRecord successfully added \n")

def addWdata():
    id = int(input("Enter id: "))
    wh = float(input("Enter work hours: "))
    ld = int(input("Enter leave days: "))
    prj = int(input("Enter number of projects: "))
    cprj = int(input("Enter completed projects: "))
    icprj = int(input("Enter incompleted projects: "))

    cursor.execute("INSERT INTO WDATA \
                    VALUES ({},{},{},{},{},{});".format(id,wh,ld,prj,cprj,icprj))
    print("\nRecord successfully added \n")

def delete():
    flag = True

    while flag == True:
        print("PRESS 1: to delete record from Employee")
        print("PRESS 2: to delete record from Department")
        print("PRESS 3: to delete record from WData")
        print("PRESS 4: to return to the main menu ")

        tableNo = int(input())
        print("\n")

        flag = False
        
        if tableNo == 1:
            table = "EMPLOYEE"
        elif tableNo == 2:
            table = "DEPARTMENT"
        elif tableNo == 3:
            table = "WDATA"
        elif tableNo == 4:
            return None
        else:
            print("Please enter a valid choice")
            flag = True

    id = int(input("Enter id whose record you wan to delete: "))

    cursor.execute("DELETE FROM  {} \
                    WHERE id = {} ;".format(table,id))
    print("\nRecord successfully deleted")

def update():
    flag = True

    while flag:
        print("PRESS 1: to update table Employee")
        print("PRESS 2: to update table Department")
        print("PRESS 3: to update table WData ")
        print("PRESS 4: to return to the main menu ")

        flag = False
        choice = int(input())

        if choice == 1:
            updateEmployee()
        elif choice == 2:
            updateDepartment()
        elif choice == 3:
            updateWData()
        elif choice == 4:
            return None
        else:
            print("Enter a valid choice ")
            flag  = True

def updateEmployee():
    id = int(input("Enter id of the record you want to update: "))
    flag = True

    while flag == True:

        print("PRESS 1: to update ename ")
        print("PRESS 2: to update CntNo ")
        print("PRESS 3: to update Age ")

        flag = False

        columnNo = int(input())
        print("\n")

        if columnNo == 1:
            column = "ename"
            data = input("Enter the new Ename: ")
        elif columnNo == 2:
            column = "cntno"
            data = int(input("Enter the new CntNo: "))
        elif columnNo == 3:
            column = "age"
            data = int(input("Enter the new Age: "))
        else:
            print("Enter a valid choice")
            flag = True

    cursor.execute("UPDATE EMPLOYEE \
                    SET {} = {}  \
                    WHERE id = {};".format(column,data,id))

    print("\nData updated successfully ")

def updateDepartment():
    id = int(input("Enter id of the record you want to update: "))
    flag = True

    while flag == True:

        print("PRESS 1: to update Dept ")
        print("PRESS 2: to update city ")
        print("PRESS 3: to update salary ")

        flag = False

        columnNo = int(input())
        print("\n")

        if columnNo == 1:
            column = "Dept"
            data = input("Enter the new dept: ")
        elif columnNo == 2:
            column = "city"
            data = int(input("Enter the new city "))
        elif columnNo == 3:
            column = "salary"
            data = int(input("Enter the new salary: "))
        else:
            print("Enter a valid choice")
            flag = True

    cursor.execute("UPDATE DEPARTMENT \
                    SET {} = {} \
                    WHERE id = {} ;".format(column,data,id))

    print("\nData updated successfully ")

def updateWData():
    id = int(input("Enter id of the record you want to update: "))
    flag = True

    while flag == True:

        print("PRESS 1: to update work hours ")
        print("PRESS 2: to update leave days")
        print("PRESS 3: to update projects ")
        print("PRESS 4: to update completed projects ")
        print("PRESS 5: to update incomplete projects ")

        flag = False

        columnNo = int(input())
        print("\n")

        if columnNo == 1:
            column = "wh"
            data = float(input("Enter the new work hours: "))
        elif columnNo == 2:
            column = "ld"
            data = int(input("Enter the new leave days: "))
        elif columnNo == 3:
            column = "prj"
            data = int(input("Enter the new number of projects: "))
        elif columnNo == 4:
            column = "cprj"
            data = int(input("Enter the new number of complete projects: "))
        elif columnNo == 5:
            column = "icprj"
            data = int(input("Enter the new number of  incompleted projects: "))

        else:
            print("Enter a valid choice")
            flag = True

    cursor.execute("UPDATE WDATA \
                    SET {} = {} \
                    WHERE id = {} ;".format(column,data,id))

    print("\nData updated successfully ")

def display():

    col = ["ID","EName","CntNo","Age","Dept","City","Salary","WH","LD","Prj","CPrj","ICPrj"]

    id = int(input("Enter the id whose record you want to see: "))

    cursor.execute("Select e.id,e.ename,e.cntno,e.age,d.dept,d.city,d.salary,w.wh,w.ld,w.prj,w.cprj,w.icprj \
                    from EMPLOYEE e, DEPARTMENT d, WDATA w \
                    WHERE e.id = d.id && e.id = w.id && e.id ={} ; ".format(id))
    
    result = cursor.fetchall()

    for i in result:
        n = len(i)
        for j in range(0,n):
           print(col[j],"\t",i[j])
        print()


#main program starts
print("Welcome to database created by Ishrit and Ashwin\n")

while True:
    print("\n\n")
    print("PRESS 1: to display data from the tables ")
    print("PRESS 2: to add data to a table")
    print("PRESS 3: to delete data from a table ")
    print("PRESS 4: to update data in a table")
    print("PRESS 5: to exit the program ")

    choice = int(input())
    print("\n")

    if choice == 1:
        display()
    elif choice == 2:
        add()
    elif choice == 3:
        delete()
    elif choice == 4:
        update()
    elif choice == 5:
        exit()
    else:
        print("\n Please enter a valid choice")
        continue

    mycon.commit()

