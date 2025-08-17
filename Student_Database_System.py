import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="Tarun@123",database="Student_Database_System")
if con.is_connected():
    print("Connected Successfully")
    def insert_Data():
        while True:
            cursor=con.cursor()
            n=input("Enter Name:\n")
            a=int(input("Enter age:\n"))
            e=input("Enter mail:\n")
            g=input("Enter gender:\n")
            st_id=int(input("Enter Studnt id:\n"))
            c=int(input("Enter class:\n"))
            query="insert into Students value('{}',{},'{}','{}',{},{})".format(n,a,e,g,st_id,c)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("Data Inserted")
            choice=int(input("1->>> To insert more Data\n2->>>> No more Data\n"))
            if choice!=1:
                break
    def update_Data():
        cursor=con.cursor()
        n=input("Enter Student name:\n")
        while True:
            choice=int(input("1->Age\n2->Mail\n3->Student Id\n4->Clase\n5->Name:\n6->>Exit:\n"))
            if choice==1:
                a=int(input("Enter Updated Age:\n"))
                query="update Students set Age={} where name='{}'".format(a,n)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("Data Updated")
                else:
                    print(f"Record Name = {n} not prsent")
            elif choice==2:
                m=input("Enter Updated Mail:\n")
                query="update Students set Email='{}' where name='{}'".format(m,n)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("Data Updated")
                else:
                    print(f"Record Name = {n} not prsent")
            elif choice==3:
                Std_id=int(input("Enter Updated Student_id:\n"))
                query="update Students set Student_id={} where name='{}'".format(Std_id,n)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("Data Updated")
                else:
                    print(f"Record Name = {n} not prsent")
            elif choice==4:
                c=int(input("Enter Updated Class:\n"))
                query="update Students set class={} where name='{}'".format(c,n)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("Data Updated")
                else:
                    print(f"Record Name = {n} not prsent")
            elif choice==5:
                id=int(input("Enter Student_id:\n"))
                New_n=input("Enter Updated Name:\n")
                query="update Students set Name='{}' where Student_id={}".format(New_n,id)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("Data Updated")
                else:
                    print(f"Record Student_id = {id} not prsent")
            else:
                break
    def Delete_Data():
        cursor=con.cursor()
        print("Select Your choice")
        print("NOTE This will delete all record like name age etc for your choice")
        while True:
            choice=int(input("1->Age\n2->Mail\n3->Student Id\n4->Clase\n5->Name:\n6->>Exit:\n"))
            if choice==1:
                a=int(input("Enter age To delete record\n"))
                query="Delete from Students where Age={}".format(a)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("All Record deleted for this age")
                else:
                    print(f"{a} not prsent in table ")
            elif choice==2:
                m=input("Enter Email To delete record\n")
                query="Delete from Students where Email='{}'".format(m)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("All Record deleted for this mail")
                else:
                    print(f"{m} not prsent in table ")
            elif choice==3:
                id=int(input("Enter Student Id To delete record\n"))
                query="Delete from Students where Student_id={}".format(id)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("All Record deleted for this Student_id")
                else:
                    print(f"{id} not prsent in table ")
            elif choice==4:
                c=int(input("Enter Class To delete all record\n"))
                query="Delete from Students where Class={}".format(c)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("All Record deleted for this class")
                else:
                    print(f"{c} not prsent in table ")
            elif choice==5:
                name=input("Enter Name To delete record\n")
                query="Delete from Students where Name='{}'".format(name)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("All Record deleted for this Name")
                else:
                    print(f"{name} not prsent in table ")
            else:
                break
    def Stucture_table():
        cursor=con.cursor()
        query="desc Students"
        cursor.execute(query)
        data=cursor.fetchall()
        print(data)
        con.commit()
    def show_data():
        cursor=con.cursor()
        while True:
            choice=int(input("1->> for only record\n2--> Selected Record\n3--> for all record\n"
            "4--> for exit\n"))
            if choice==1:
                query="Select*from Students"
                cursor.execute(query)
                data=cursor.fetchone()
                print(data)
            elif choice==2:
                n=int(input("Enter No. of record\n"))
                query="Select*from Students"
                cursor.execute(query)
                data=cursor.fetchmany(n)
                print(data)
            elif choice==3:
                query="Select*from Students"
                cursor.execute(query)
                data=cursor.fetchall()
                print(data)
            else:
                break
    def show_tables():
        cursor=con.cursor()
        query="Show tables"
        cursor.execute(query)
        data=cursor.fetchall()
        print(data)
    def create_table():
        print("Open Mysql command line\n Type command Create table table_name ('field name ') ")
    #insert_Data()
    #update_Data()
    #Delete_Data()
    #Stucture_table()
    #show_data()
    #show_tables()
    #create_table()
    while True:
        choice=int(input("1->>To Stuctur of the Table\n2->>To Insert Data\n3->>To Update Data\4->>To Delete Record\n" \
        "5->>To show Data\n6->>To show Tables\7-->Create Table\n8->>To exit:\n"))
        if choice==1:
            Stucture_table()
        elif choice==2:
            insert_Data()
        elif choice==3:
            update_Data()
        elif choice==4:
            Delete_Data()
        elif choice==5:
            show_data()
        elif choice==6:
            show_tables()
        elif choice==7:
            create_table()
        else:
            break
        