import sqlite3

conn = sqlite3.connect('UserData.db')
print("\nOpened database successfully")
cursor_obj = conn.cursor()

def signup_user():
    val1 = input("Create a username ")
    val2 = input("Create a password ")
    conn.execute("Insert into LoginData values(?,?)",(val1,val2))
    conn.commit()
    print("\nUser Registration is successful")

def login_user():
    uname = input("Enter your username ")
    pwd = input("Enter the password ")
    cursor_obj.execute("Select * from LoginData where Username=? and Password=?",(uname,pwd))
    dataset = conn.execute("Select * from LoginData where Username=? and Password=?",(uname,pwd))
    
    if(len(cursor_obj.fetchall()) > 0):
        for row in dataset:
            if(row[0] == uname and row[1] == pwd):
                print("\nLogin Successful")
    else:
        print("\nInvalid Credentials")
        








print("\nSelect an operation")
print("\n1.Login\n2.Sign Up")
selection = int(input())
if(selection == 1):
    login_user()
elif(selection == 2):
    signup_user()
    print("\nNow please login in to continue")
    login_user()
else:
    print("\nInvalid Selection")