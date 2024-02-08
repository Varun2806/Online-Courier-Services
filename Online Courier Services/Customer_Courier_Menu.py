import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'admin123',auth_plugin="mysql_native_password", database='OnlineCourierServices' )
cust1=conn.cursor()
for i in range(0,76):
 print('WELCOME TO Customer Portal:')
 print('1.Book Courier Order')
 print('2.Track Consignment')
 print('3.Calculate Postage')
 print('4.Give Feedback')
 print('5.Register Complain')
 print('6.exit')
 choice=int(input('Enter the section you want to access:'))
 if choice==1:
      print('COURIER-ORDER')
      a=(input("Enter Sender's NAME:"))
      b=int(input("Enter Sender's Mobile Number:"))
      c=(input("Enter Sender's Address:"))
      d=(input("Enter Receiver's NAME:"))
      e=int(input("Enter Receiver's mobile number:"))
      f=(input("Enter Receiver's Address:"))
      g=(input("Enter Package Weight:"))
      cust1.execute("INSERT INTO courier VALUES(' "+a+" ',"+str(b)+",' "+c+" ',' "+d+" ',"+str(e)+",' "+f+" ')")
      conn.commit()
      print('Courier (s) Placed')
      print('Please Use Your Mobile Number To Track  Consignment')
      print('===================================Thanks For Choosing US===================================')
 elif choice==2:
     print("Please Enter The Following Details")
     Track=(input("Enter Consignment(Mobile) Number:"))
     Track1=(input("Enter The Destination City:"))
     print('')
     print('')
     print('Searching Where Is Your Package')
     print('')
     print('')
     print('Its On The Way')
     print('It will reach you in 2-3 Days ')
     print('==============================================================================================')
     
 elif choice==3:
      weig=input('Enter Weight Of Package:')
      print('Cost For The Package of Weight',weig,'is')
      cust1.execute("select * from courier2 where weight_in_kgs={}".format(weig))
      bill=cust1.fetchall()
      for x in bill:
           print(x)
      print('==============================================================================================')
 elif choice==4:
     print('Feedback Form')
     a=(input("Enter Your NAME:"))
     b=int(input("Enter Your Mobile Number:"))
     c=int(input("Enter Rating(1 to 5):"))
     d=(input("Enter Your Feedback:"))
     cust1.execute("INSERT INTO Feedback VALUES(' "+a+" ',"+str(b)+","+str(c)+",' "+d+" ')")
     conn.commit()
     print('Form Sucessfully Submitted')
     print('===================================Thanks For Your Feedback ===================================')
 elif choice==5:
     print('')
     print('       Problem With Our Courier Facility')
     print('')
     print('')
     print('1.Problem with Delivery')
     print('2.Problem with Service')
     print('3.Problem with Door delivery boy')
     print('')
     a=int(input('Please enter your choice:'))
     print('')
     if a==1:
         cus_name=str(input('Please enter your name:'))
         phno1=int(input('Please enter your phone no:'))
         sa_name=str(input('Please enter the name of the agent whom you dealed with:'))
         prob=str(input('Please enter your problem:'))
         print('')
         print('      Sorry for the problem sir/madam we will ensure that this does not happen again. Thank you')
         insert2="insert into DeliveryProblem values('"+cus_name+"',"+str(phno1)+",'"+sa_name+"','"+prob+"')"
         cust1.execute(insert2)
         conn.commit()
     if a==2:
         cus_name=str(input('Please enter your name:'))
         phno1=int(input('Please enter your phone no:'))
         se_name=str(input('Please enter the name of the agent you dealed with:'))
         prob=str(input('Please enter the problem you face:'))
         print('')
         print('       Sorry for the problem sir/madam we will ensure that this does not happen again.  Thank you')
         insert3="insert into serviceproblem Values('"+cus_name+"',"+str(phno1)+",'"+se_name+"','"+prob+"')"
         cust1.execute(insert3)
         conn.commit
     if a==3:
         cus_name=str(input('Please enter your name:'))
         phno1=int(input('Please enter your phone no:'))
         name1=str(input('Please enter the agent name:'))
         prob=str(input('Please enter the problem you have faced:'))
         insert4="insert into DeliveryAgentProb values('"+cus_name+"',"+str(phno1)+",'"+name1+"','"+prob+"')"
         cust1.execute(insert4)
         conn.commit()
         print('')
         print('        Sorry for the problem sir/madam we see to it that the agent gets penalized severely. Thank you')
         print('')
         print('==============================================================================================')
         
 elif choice==6:
     quit()
            



                   


  
      

