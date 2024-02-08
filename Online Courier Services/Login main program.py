import mysql.connector as sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'admin123',auth_plugin="mysql_native_password",database="OnlineCourierServices" )

if conn.is_connected():
        print('successfully connected')
c1=conn.cursor()
print('')
print('')
print('          DOOR To DOOR COURIER SERVICES')
print('          Welcome To Our Service Portal')
print('')

o=input('    Press enter to begin your courier surfing')
print('1.Customer Login')
print('2.Store Login')
choose=int(input('ENTER (1) FOR Customer Login OR (2) Store Login  :'))
if choose==1:
    print('1.New Customer')
    print('2.Existing Customer')
    choose3=int(input('ENTER (1) FOR New Customer  OR (2) Existing Customer   :'))
    if choose3==1:
        name=input('Enter your user-name:')
        passwd=input('Set your password here:')
        passwd1=input('Confirm password:')
        c1.execute("INSERT INTO customerlogin VALUES(' "+name+" ',' "+passwd+" ')")
        conn.commit()
        print('ACCOUNT CREATED CONGRATULATIONS')
        move_in=input('press enter to login:')
        import Customer_Courier_Menu
    elif choose3==2:
         email=input('Enter your user_name:')
         passd=input('Enter your Pass_word:')
         c1.execute('select * from customerlogin where user_name=" '+email+' " and pass_word=" '+passd+' " ')
         if c1.fetchone() is None:
             print(' sorry your password in wrong')
         else:
                 import Customer_Courier_Menu
if choose==2:
    print('1.New Employee')
    print('2.Existing Employee')
    choose5=int(input('ENTER (1) FOR New Employee  OR (2) Existing Employee   :'))
    if choose5==1:
        name=input('Enter your user-name:')
        passwd=input('Set your password here:')
        passwd1=input('Confirm password:')
        c1.execute("INSERT INTO employeelogin VALUES(' "+name+" ',' "+passwd+" ')")
        conn.commit()
        print('ACCOUNT CREATED CONGRATULATIONS')
        move_in=input('press enter to login:')
        import Store_Courier_Menu
    elif choose5==2:
        email=input('Enter your user_name:')
        passd=input('Enter your Pass_word:')
        c1.execute('select * from employeelogin where user_name=" '+email+' " and pass_word=" '+passd+' " ')
        if c1.fetchone() is None:
            print(' sorry your password in wrong')
        else:
                import Store_Courier_Menu
        
     
    
    
        
    
             
         

         
        
       
     
         

         
        
         
          
