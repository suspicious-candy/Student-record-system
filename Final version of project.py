#           A project of class 12th on
#   topic of student managment system using mysql 


import mysql.connector
mydb = mysql.connector.connect(host ="localhost",user ="root",passwd ="Shr3yansh_jain@123")
mycur = mydb.cursor()
mycur.execute("create database if not exists student_db1")
mycur.execute("use student_db1")
abc="Y"
def while_fn ():
    while abc=="Y" or abc=="y":
        if menu==1 :
            userinput()
        elif menu==2 :
            search_fn()
            menu_fn()
        elif menu == 3:
            update_fn()
        elif menu == 4:
            del_fn()
            
    while abc=="N" or abc=="n":
            menu_fn
def userinput ():
    addno=str(input("enter admission no. of the student : "))
    name=str(input("enter name of the student : "))
    dob=str(input("enter  year of birth of the student : "))
    att=str(input("enter attendence of the student P/A : "))
    cla= str(input("enter the class of the student: (eg-12) "))
    sec= str(input("enter the section of the student:  "))
    if cla == '12' or cla=='11':
        stre = str(input("enter the stream of the student: (PCM / PCB / Commerce / Humanities) "))
        opt  = str(input("enter the optional subject of the student: "))
        if stre == "PCM":
            sb1 = "Physics"
            sb2 = "Chemistry"
            sb3 = "Maths"
            sb4 = "English"
        elif stre == "PCB":
            sb1 = "Physics"
            sb2 = "Chemistry"
            sb3 = "Biology"
            sb4 = "English"
        elif stre == "Commerce":
            sb1 = "Business Studies"
            sb2 = "Economics"
            sb3 = "Accountancy"
            sb4 = "English"
        elif stre == "Humanities":
            sb1 = "Economics"
            sb2 = "History"
            sb3 = "Political Science"
            sb4 = "English"
        else:
            print(" NO  SUCH STREAM EXISTS")
    elif cla== '9' or cla=='10':
        opt  = str(input("enter the optional subject of the student: "))
        lan  = str(input("enter the 2nd language subject of the student: "))
        ma = str (input("enter the type of maths chosen by the student (basic/std) : "))
        sb1 = "Social Studies"
        sb2 = "Science"
        sb3 = "Maths "+ma
        sb4 = "English"
        
    if cla == '12' or cla == '11':
     creat_tb = "create table if not exists student1_tb ( saddno varchar(30) primary key, sname varchar(30), sdob varchar(30), satt varchar(30), sclass  varchar(20), ssec varchar(20), sstream varchar(20), ssubject1 varchar(20),ssubject2 varchar(20),ssubject3 varchar(20),ssubject4 varchar(20), soptional varchar(20))"
     mycur.execute(creat_tb)
     colum_tb = "insert into student1_tb (saddno, sname, sdob, satt, sclass, ssec, sstream,ssubject1,ssubject2,ssubject3,ssubject4,soptional) values ('"+addno+"','"+name+"','"+dob+"','"+att+"',"+cla+",'"+sec+"','"+stre+"','"+sb1+"','"+sb2+"','"+sb3+"','"+sb4+"','"+opt+"')"
     mycur.execute(colum_tb)
     mydb.commit()
     mycur.execute("select * from student1_tb")
     result = mycur.fetchall()
     print("|| addno. || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||")
     for x in result:
         print(x)
     global abc
     abc = input("do you want to continue adding student ? [y/n] : ")
     
    elif cla== '9' or cla== '10':
         creat_tb = "create table if not exists student2_tb ( saddno varchar(30) primary key, sname varchar(30), sdob varchar(30), satt varchar(30), sclass  varchar(20), ssec varchar(20), ssubject1 varchar (20),ssubject2 varchar (20),ssubject3 varchar (20),ssubject4 varchar (20),ssubject4 varchar(20), soptional varchar(20))"
         mycur.execute(creat_tb)
         colum_tb = "insert into student2_tb (saddno, sname, sdob, satt, sclass, ssec, ssubject1, ssubject2, ssubject3, ssubject4, ssubject5 , soptional) values ('"+addno+"','"+name+"','"+dob+"','"+att+"',"+cla+",'"+sec+"','"+sb1+"','"+sb2+"','"+sb3+"','"+sb4+"','"+lan+"','"+opt+"')"
         mycur.execute(colum_tb)
         mydb.commit()
         mycur.execute("select * from student2_tb")
         result = mycur.fetchall()
         print("|| addno. || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5|subject 6 (optional)||")
         for x in result:
             print(x)
         abc = input("do you want to continue adding student ? [y/n] : ")
    else :
        print ("this database is only for classes from 9th to 12th")
    

def search_fn ():
        menu2=int(input(" ================================= \n [1] search by admission no. \n [2] search by name \n [3] search by birth year \n [4] search present student \n [5] search absent student \n [6] search by class \n [7] search by section \n [8] search by stream \n [9] search by subject \n [10] main menu  \n =================================\n:"))
        if menu2==1 :
            print("==================== \n [1] search by admission no. \n====================")
            search=str(input("Enter admission no. of student :"))
            mycur.execute("select * from student1_tb where saddno='"+search+"'")
            result = mycur.fetchall()
            if mycur.rowcount != 0 :
               print("|| roll || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
               for x in result:
                 print(x)    
            else:
              mycur.execute("select * from student2_tb where saddno='"+search+"'")
              result += mycur.fetchall()
              print("|| roll || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5|subject 6 (optional)||\n=====================================\n")
              for x in result:
                 print(x)
        elif menu2==2 :
            print("==================== \n [2] search by name \n====================")
            search=str(input("Enter name of student :"))
            mycur.execute("select * from student1_tb where sname='"+search+"'")
            result = mycur.fetchall()
            print("\n|| addno || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
            for x in result:
                print(x)
            mycur.execute("select * from student2_tb where sname='"+search+"'")
            result = mycur.fetchall()
            print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
            for x in result:
               print(x)
            
        elif menu2==3 :
            print("==================== \n [3] search by birth year \n====================")
            search=str(input("Enter birth year of student :"))
            mycur.execute("select * from student1_tb where sdob='"+search+"'")
            result = mycur.fetchall()
            print("\n|| addno || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
            for x in result:
                print(x)
            mycur.execute("select * from student2_tb where sdob='"+search+"'")
            result = mycur.fetchall()
            print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5 ||subject 6 (optional)||\n=====================================\n")
            for x in result:
               print(x)
        elif menu2==4 :
            print("==================== \n [4] search present student \n====================")
            mycur.execute("select * from student1_tb where satt='P'")
            result = mycur.fetchall()
            print("\n|| addno || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
            for x in result:
                print(x)
            mycur.execute("select * from student2_tb where satt='P'")
            result = mycur.fetchall()
            print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
            for x in result:
               print(x)
        elif menu2==5 :
            print("==================== \n [5] search absent student \n====================")
            mycur.execute("select * from student1_tb where satt='A'")
            result = mycur.fetchall()
            print("\n|| addno || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
            for x in result:
                print(x)
            mycur.execute("select * from student2_tb where satt='A'")
            result = mycur.fetchall()
            print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5 ||subject 6 (optional)||\n=====================================\n")
            for x in result:
               print(x)
        elif menu2==6:
            print("==================== \n [6] search by class \n====================")
            search=str(input("Enter class (eg 12 for 12th) :"))
            if search == '11' or search == '12':
                mycur.execute("select * from student1_tb where sclass='"+search+"'")
                result = mycur.fetchall()
                print("\n|| addno || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
                for x in result:
                    print(x)
            elif search == '9' or search == '10' :
                mycur.execute("select * from student2_tb where sclass='"+search+"'")
                result = mycur.fetchall()
                print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5 ||subject 6 (optional)||\n=====================================\n")
                for x in result:
                   print(x)
            else:
                print("wrong input")
                
        elif menu2==7:
            print("==================== \n [7] search by section \n====================")
            search=str(input("Enter section of student :"))
            mycur.execute("select * from student1_tb where ssec='"+search+"'")
            result = mycur.fetchall()
            print("\n|| addno || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
            for x in result:
                print(x)
            mycur.execute("select * from student2_tb where ssec='"+search+"'")
            result = mycur.fetchall()
            print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
            for x in result:
               print(x)
            
        elif menu2==8:
            print("==================== \n [8] search by stream \n====================")
            search=str(input("Enter section of stream:"))
            mycur.execute("select * from student1_tb where sstream='"+search+"'")
            result = mycur.fetchall()
            print("\n|| addno || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
            for x in result:
                print(x)
                
        elif menu2==9:
            print("==================== \n [9] search by subject \n====================")
            search=str(input("Enter Subject of student :"))
            if search in ("Physics","Chemistry","Maths","English","Accountancy","Business Studies","Economics","Political Science","History","Biology", "Computer science" , "Physical Education ", "Entreprenuership", "Phsycology"):
                  mycur.execute("select * from student1_tb where ssubject1 ='"+search+"' || ssubject2 ='"+search+"'||ssubject3 ='"+search+"'||ssubject4 ='"+search+"'||soptional ='"+search+"' ")
                  result = mycur.fetchall()
                  print("\n|| addno || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
                  for x in result:
                        print(x)
                        
                
                
            elif search in ("Social Science","Maths basic", "Maths std.", "Science" , "English", "Sanskrit", "Hindi"): # add subjects for 10th class
                mycur.execute("select * from student2_tb where ssubject1 ='"+search+"' or ssubject2 ='"+search+"'||ssubject3 ='"+search+"'||ssubject4 ='"+search+"' || ssubject5 ='"+search+"' ||soptional ='"+search+"' ")
                result = mycur.fetchall()
                print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject4 ||subject 6 (optional)||\n=====================================\n")
                for x in result:
                    print(x)
              
        elif menu2 == 10:  
            menu_fn ()


def update_fn ():
            menu3=int(input(" ================================= \n [1] update admission no. \n [2] update name \n [3] update birth year \n [4] update attendence \n [5] update section \n [6] main menu  \n =================================\n:"))
            if menu3 == 1:
                oldadd= input("Enter the addmission number to be changed : ")
                newadd = input ("Enter the new addmission number : ")
                mycur.execute("select * from student1_tb where saddno ='"+oldadd+"'")
                result = mycur.fetchall()
                if mycur.rowcount== 1:
                    print("|| roll || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
                    for x in result:
                      print(x)
                    yn=str(input("Are you sure you want to update this record(y/n):  "))
                    if yn == 'y' or yn == 'Y':
                       query = "update student1_tb set saddno = '{}' where saddno = '{}'".format(newadd,oldadd)
                       mycur.execute(query)
                       mycur.execute("select * from student1_tb where saddno ='"+newadd+"'")
                       result1 = mycur.fetchall()
                       print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
                       for x in result1:
                          print(x)
                        
                    else: 
                        menu_fn ()
                elif mycur.rowcount== 0 :
                    mycur.execute("select * from student2_tb where saddno='"+oldadd+"'")
                    result += mycur.fetchall()
                    print("|| roll || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5||subject 6 (optional)||\n=====================================\n")
                    for x in result:
                       print(x)
                    yn=str(input("Are you sure you want to update this record(y/n):  "))
                    if yn == 'y' or yn == 'Y':
                        query = "update student2_tb set saddno = '{}' where saddno = '{}'".format(newadd,oldadd)
                        mycur.execute(query)
                        mycur.execute("select * from student2_tb where saddno='"+newadd+"'")
                        result1 = mycur.fetchall()
                        print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
                        for x in result1:
                           print(x)
                    else :
                        menu_fn()
            if menu3 == 2:
                    old = input("Enter the addmission number that has to be updated : ")
                    new = input ("Enter the updated name: ")
                    mycur.execute("select * from student1_tb where saddno ='"+old+"'")
                    result = mycur.fetchall()
                    if mycur.rowcount== 1:
                        print("|| roll || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
                        for x in result:
                          print(x)
                        yn=str(input("Are you sure you want to update this record(y/n):  "))
                        if yn == 'y' or yn == 'Y':
                            query = "update student1_tb set sname = '{}' where saddno = '{}'".format(new,old)
                            mycur.execute(query)
                            mycur.execute("select * from student1_tb where saddno ='"+old+"'")
                            result1 = mycur.fetchall()
                            print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
                            for x in result1:
                               print(x)
                        else: 
                            menu_fn ()
                    elif mycur.rowcount== 0 :
                        mycur.execute("select * from student2_tb where saddno='"+old+"'")
                        result += mycur.fetchall()
                        print("|| roll || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5||subject 6 (optional)||\n=====================================\n")
                        for x in result:
                           print(x)
                        yn=str(input("Are you sure you want to update this record(y/n):  "))
                        if yn == 'y' or yn == 'Y':
                           query = "update student2_tb set sname = '{}' where saddno = '{}'".format(new,old)
                           mycur.execute(query)
                           mycur.execute("select * from student2_tb where saddno='"+old+"'")
                           result1 = mycur.fetchall()
                           print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
                           for x in result1:
                              print(x)
                        else :
                            menu_fn()
            if menu3 == 3:
                old = input("Enter the addmission number that has to be updated : ")
                new = input ("Enter the updated birth year: ")
                mycur.execute("select * from student1_tb where saddno ='"+old+"'")
                result = mycur.fetchall()
                if mycur.rowcount== 1:
                    print("|| roll || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
                    for x in result:
                      print(x)
                    yn=str(input("Are you sure you want to update this record(y/n):  "))
                    if yn == 'y' or yn == 'Y':
                        query = "update student1_tb set sdob = '{}' where saddno = '{}'".format(new,old)
                        mycur.execute(query)
                        mycur.execute("select * from student1_tb where saddno ='"+old+"'")
                        result1 = mycur.fetchall()
                        print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
                        for x in result1:
                           print(x)
                        
                    else: 
                        menu_fn ()
                elif mycur.rowcount== 0 :
                    mycur.execute("select * from student2_tb where saddno='"+old+"'")
                    result += mycur.fetchall()
                    print("|| roll || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5||subject 6 (optional)||\n=====================================\n")
                    for x in result:
                       print(x)
                    yn=str(input("Are you sure you want to update this record(y/n):  "))
                    if yn == 'y' or yn == 'Y':
                       query = "update student2_tb set sdob = '{}' where saddno = '{}'".format(new,old)
                       mycur.execute(query)
                       mycur.execute("select * from student2_tb where saddno='"+old+"'")
                       result1 = mycur.fetchall()
                       print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
                       for x in result1:
                          print(x)
                    else :
                        menu_fn()
            if menu3 == 4:
                old = input("Enter the addmission number that has to be updated : ")
                new = input ("Enter the updated attendence: ")
                mycur.execute("select * from student1_tb where saddno ='"+old+"'")
                result = mycur.fetchall()
                if mycur.rowcount== 1:
                    print("|| roll || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
                    for x in result:
                      print(x)
                    yn=str(input("Are you sure you want to update this record(y/n):  "))
                    if yn == 'y' or yn == 'Y':
                        query = "update student1_tb set satt = '{}' where saddno = '{}'".format(new,old)
                        mycur.execute(query)
                        mycur.execute("select * from student1_tb where saddno ='"+old+"'")
                        result1 = mycur.fetchall()
                        print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
                        for x in result1:
                           print(x)
                        
                    else: 
                        menu_fn ()
                elif mycur.rowcount== 0 :
                    mycur.execute("select * from student2_tb where saddno='"+old+"'")
                    result += mycur.fetchall()
                    print("|| roll || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5||subject 6 (optional)||\n=====================================\n")
                    for x in result:
                       print(x)
                    yn=str(input("Are you sure you want to update this record(y/n):  "))
                    if yn == 'y' or yn == 'Y':
                        query = "update student2_tb set satt = '{}' where saddno = '{}'".format(new,old)
                        mycur.execute(query)
                        mycur.execute("select * from student2_tb where saddno='"+old+"'")
                        result1 = mycur.fetchall()
                        print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
                        for x in result1:
                           print(x)
                    else :
                        menu_fn()

            if menu3 == 5:
                old = input("Enter the addmission number that has to be updated : ")
                new = input ("Enter the updated section: ")
                mycur.execute("select * from student1_tb where saddno ='"+old+"'")
                result = mycur.fetchall()
                if mycur.rowcount== 1:
                    print("|| roll || name || birth y || attendence || class || section || stream || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5(optional)||\n=====================================\n")
                    for x in result:
                      print(x)
                    yn=str(input("Are you sure you want to update this record(y/n):  "))
                    if yn == 'y' or yn == 'Y':
                        query = "update student1_tb set ssec = '{}' where saddno = '{}'".format(new,old)
                        mycur.execute(query)
                        mycur.execute("select * from student1_tb where saddno ='"+old+"'")
                        result1 = mycur.fetchall()
                        print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
                        for x in result1:
                           print(x)
                        
                    else: 
                        menu_fn ()
                elif mycur.rowcount== 0 :
                    mycur.execute("select * from student2_tb where saddno='"+old+"'")
                    result += mycur.fetchall()
                    print("|| roll || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject 5||subject 6 (optional)||\n=====================================\n")
                    for x in result:
                       print(x)
                    yn=str(input("Are you sure you want to update this record(y/n):  "))
                    if yn == 'y' or yn == 'Y':
                        query = "update student2_tb set ssec = '{}' where saddno = '{}'".format(new,old)
                        mycur.execute(query)
                        mycur.execute("select * from student2_tb where saddno='"+old+"'")
                        result1 = mycur.fetchall()
                        print("|| addno || name || birth y || attendence || class || section || subject 1 || subject 2|| subject 3 ||subject 4 || subject5||subject 6 (optional)||\n=====================================\n")
                        for x in result1:
                           print(x)
                    else :
                        menu_fn()
            if menu3 == 6:
                menu_fn()




def del_fn():
    menu4 = int(input(" ================================= \n press [1] delete  student record (class 9/10) by admission no. \n press [2] delete  student record (class 11/12) by admission no.\n press [3] for main menu  \n=================================:"))
    if menu4 == 1 :
        print("================================= \n [1] delete student record of class 9/10 by admission no.\n =================================")
        delete=str(input("Enter admission no. of student: "))
        mycur.execute("delete from student2_tb where saddno='"+delete+"'")
        mydb.commit()
    elif menu4==2:
        print("================================= \n [2] delete student record of class 11/12 by admission no.\n =================================")
        delete = str(input("Enter admission no. of student: "))
        mycur.execute("delete from student1_tb where saddno='"+delete+"'")
        mydb.commit()


    elif menu4 == 3 :
            menu_fn()
    
        
def menu_fn () :
    global menu
    menu=int(input("====================================\n press [1] for entery of new student \n press [2] for searching student \n press [3] for updating a field in the record \n [4] for deleting a record====================================\n   :"))
    while_fn()
    print(abc)

menu_fn ()

