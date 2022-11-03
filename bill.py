import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'hoteldb')
mycursor = mydb.cursor()
total=0
item=[]
while(True):
    print("select an option")
    print("1 Tea-----10rs")
    print("2 coffee----15rs")
    print("3 burger----50rs")
    print("4 mandhi----180rs")
    print("5 sandwitch--60")
    print("6 generate bill")
    print("7 exit")
    choice=int(input("enter the choice"))
    if(choice==1):

        print("Added tea")
        qty=int(input("enter the quantity"))
        total+=10*qty
        item.append("tea x"+str(qty))
        print("quantity",qty)
        print("total",total)
    elif(choice==2):
        print("added coffee")
    elif(choice==3):
        print("added burger")
    elif(choice==4):
        print("added mandhi")
    elif(choice==5):
        print("added sandwitch")
    elif(choice==6):
        print("generate bill")
    elif(choice==7):
        break
        

       