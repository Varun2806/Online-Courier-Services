import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'admin123',auth_plugin="mysql_native_password", database='OnlineCourierServices' )
cust1=conn.cursor()
for i in range(0,76):
 print('WELCOME TO Store Portal:')
 print('1.Book Courier_order ')
 print('2.Billing')
 print('3.Courier Service Agents')
 print('4.Add Courier Service Agents')
 print('5.exit')
 choice=int(input('Enter The Section You Want To Access:'))
 if choice==1:
    print('1.Courier placement')
    print('2.Courier order list')
    sect=str(input('enter the section that you want to access:'))
    if sect=="1":
       print('COURIER-ORDER')
       a=(input('Enter the customer name:'))
       b=int(input('Enter the customer mobile number:'))
       c=(input('Enter the customer address:'))
       d=(input('Enter the receiver name:'))
       e=int(input('Enter the receiver mobile number:'))
       f=(input('Enter the receiver address:'))
       cust1.execute("INSERT INTO courier VALUES(' "+a+" ',"+str(b)+",' "+c+" ',' "+d+" ',"+str(e)+",' "+f+" ')")
       conn.commit()
       print(cust1.rowcount,"courier's placed")
       print('===============================================================================================================')
    elif sect=="2":
       S=str(input('Do you want to see your Courier order''(yes...\...no):'))
       if S=="yes":
         a=input('enter the customer mob number:')
         cust1.execute('select * from courier where customer_mobile_number="{}" '.format(a))
         order=cust1.fetchall()
         print('customer name,','customer mob no,','customer address,','receiver name,','receiver mob no,','receiver address:')
         for j in order:
              print(j)
         print('===============================================================================================================')
       else:
            print('Thank you')
            print('==============================================================================================================')
 elif choice==2:
      weig=input('Enter Weight Of Package:')
      print('Cost For The Package of Weight',weig,'is:')
      cust1.execute("select * from courier2 where weight_in_kgs={}".format(weig))
      bill=cust1.fetchall()
      for x in bill:
           print(x)
      print('===============================================================================================================')
 if choice==3:
      city1=input('Enter your City name:')
      cust1.execute("select * from courier3")
      boys=cust1.fetchall()
      print(' City:      Courier_Agent:       Mobile no:')
      for y in boys:
          print(y)
      print('===============================================================================================================')
 elif choice==4:
     print('Add Courier Service Agents')
     cit=(input('Enter The City Name:'))
     age=(input('Enter The Agents Name:'))
     mob=int(input('Enter the Agents Mobile No:'))
     cust1.execute("INSERT INTO courier3 VALUES(' "+cit+" ',' "+age+" ',"+str(mob)+")")
     conn.commit()
     print("Agent Sucessfully Added")
     print('===============================================================================================================')
 elif choice==5:
            quit()
