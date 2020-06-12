import mysql.connector as con

mydb=con.connect(
    host="localhost",
    user="root",
    passwd="<Your Password>",
    database="Contacts"
)

cur=mydb.cursor()
sql1="insert into Contacts(name, phone1,phone2,address,email) values(%s,%s,%s,%s,%s)"

cur.execute("create table if not exists Contacts(name varchar(50) not null,phone1 varchar(20) not null,phone2 varchar(20), address varchar(255),email varchar(20),primary key(phone1)")
print("What do you wish to do today?\n1.Enter a new contact\n2.Update existing contact\n3.Delete contact\n4.View All contacts")
choice = int(input("Enter your choice:"))
if choice == 1:
    name=input("Enter contact name:")
    num=input("Enter phone number:")
    ch=int(input("Do you wish to enter alternate phone number?\n1.Yes\n2.No"))
    if ch==1:
        num2=input("Enter alternate number:")
    else:
        num2="-"

    ch=int(input("Do you wish to enter email id?\n1.Yes\n2.No"))
    if ch==1:
        email=input("Enter email id:")
    else:
        email="-"

    ch=int(input("Do you wish to enter address?\n1.Yes\n2.No"))
    if ch==1:
        add=input("Enter address:")
    else:
        add="-"

    val=(name,num,num2,add,email)
cur.execute(sql1,val)

if choice==2:
    print("select * from Contacts")
    nm=input("Enter contact name whose details you want to update:")
    c=int(input("Which of the following details you want to update:\n1.Name\n2.Phone No.1\n3.Phone No.2\n4.Email ID\n5.Address"))
    if c==1:
       # n1=input("Enter previous name stored:")
        n2=input("Enter updated name:")
        v=(n2,nm)
        cur.execute("update Contacts set name= %s where name=%s",v)

    if c==2:
        #n1=input("Enter previously stored mobile number:")
        n2=input("Enter updated mobile number:")
        v=(n2,nm)
        cur.execute("update Contacts set phone1=%s where name=%s",v)

    if c==3:
        #n1=input("Enter previous phone number:")
        n2=input("Enter updated phone number:")
        v=(n2,nm)
        cur.execute("update Contacts set phone2=%s where name=%s",v)

    if c==4:
        #n1=input("Enter previous email id:")
        n2=input("Enter new email id:")
        v=(n2,nm)
        cur.execute("update Contacts set email=%s where name=%s")

    if c==5:
        #n1=input("Enter previous address:")
        n2=input("Enter updated address:")
        v=(n2,nm)
        cur.execute("update Contacts set address=%s where name=%s",v)

if choice==3:
    print("select * from Contacts")
    delnm=input("Enter contact name you wish to delete:")
    sure=int(input("Are you sure you want to delete this?\n1.Yes\n2.No"))
    if sure==1:
        cur.execute("delete from Contacts where name=%s",delnm)
        print("Contact deleted:",delnm)


if choice==4:
 print("select * from Contacts")



 mydb.commit() 
