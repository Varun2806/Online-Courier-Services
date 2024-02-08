import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'admin123',auth_plugin="mysql_native_password" )
if conn.is_connected():
        print('Successfully Connected')
cust1=conn.cursor()
cust1.execute('CREATE DATABASE OnlineCourierServices ')
cust1.execute('USE OnlineCourierServices ')
cust1.execute('create table courier(customer_name varchar(99) ,customer_mobile_number varchar(789),customer_address text(789),receiver_name varchar(99) ,receiver_mobile_number varchar(789),receiver_address text(789))')
cust1.execute('create table courier2(Weight_in_kgs varchar(789),Cost_in_rupees varchar(789));')
cust1.execute('create table courier3(city varchar(99),courier_boys varchar(99),courier_service_boys_mob_number varchar(99));')
cust1.execute('CREATE TABLE customerlogin(user_name VARCHAR(30),pass_word VARCHAR(30))')
cust1.execute('CREATE TABLE employeelogin(user_name VARCHAR(30),pass_word VARCHAR(30))')
cust1.execute('create table Feedback(customer_name varchar(99) ,customer_mobile_number varchar(789),rating varchar(789),feedback text(789))')
cust1.execute('create table DeliveryAgentProb(cus_name VARCHAR(100),phno BIGINT,se_name VARCHAR(100),prob VARCHAR(100))')
cust1.execute('create table DeliveryProblem(cus_name VARCHAR(100),phno1 BIGINT,sa_name VARCHAR(100),prob VARCHAR(100))')
cust1.execute('create table ServiceProblem(cus_name VARCHAR(100),phno1 BIGINT,name1 VARCHAR(100),prob VARCHAR(100))')
cust1.execute("insert into courier2 values(' 1kg' ,' 50Rs' )")
cust1.execute("insert into courier2 values('2kg','75Rs')")
cust1.execute("insert into courier2 values('3kg','100Rs')")
cust1.execute("insert into courier2 values('4kg','125Rs')")
cust1.execute("insert into courier2 values('5kg','150Rs')")
cust1.execute("insert into courier2 values('10kg','275Rs')")
cust1.execute("insert into courier2 values('20kg','525Rs')")
cust1.execute("insert into courier2 values('30kg','775Rs')")
cust1.execute("insert into courier2 values('40kg','1025Rs')")
cust1.execute("insert into courier2 values('50kg','1275Rs')")
cust1.execute("insert into courier2 values('100kg','2520Rs')")
cust1.execute("insert into courier2 values('150kg','3770Rs')")
cust1.execute("insert into courier2 values('200kg','5020Rs')")
cust1.execute("insert into courier2 values('250kg','6270Rs')")
cust1.execute("insert into courier2 values('300kg','7520Rs')")
cust1.execute("insert into courier2 values('350kg','8770Rs')")
cust1.execute("insert into courier2 values('400kg','10020Rs')")
cust1.execute("insert into courier2 values('450kg','11270Rs')")
cust1.execute("insert into courier2 values('500kg','12520Rs')")
conn.commit()
print('Database Sucessfully Created')
print('All Tables Sucessfully Created ')





          

