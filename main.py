# Source code for collge-managment system

# REGISTRATION CLASS
import random
from datetime import datetime
import mysql.connector

connector=mysql.connector.connect(host="localhost",user="root",passwd="!6969!!Msg",database="college")
cursor=connector.cursor()

class Registration:

	 def __init__(self):
	 	pass
	 def Student(self):
	 	print("--STUDENT REGISTRATION--")

	 	stu_name=input("ENTER NAME : ")
	 	stu_age=int(input("ENTER AGE : "))
	 	stu_phone=int(input("ENTER PHONE NUMBER : "))
	 	stu_email=input("ENTER EMAIL :")
	 	stu_semester=int(input("ENTER YOUR SEMESTER : "))
	 	stu_address=input("ENTER YOUR ADDRESS : ")
	 	stu_city=input("ENTER YOU CITY : ")
	 	stu_state=input("ENTER YOUR STATE : ")
	 	stu_course=input("ENTER COURSE : ")
	 	stu_parents=input("ENTER PARENTS?GUARDIAN NAME : ")
	 	fees_reciet_no=int(input("ENTER FEES RECIET NUMBER : "))
	 	date=datetime.today().strftime('%Y-%m-%d')

	 	cursor.execute(f'''insert into student_rec
	 	(name,age,phone,email,address,city,state,course,parents,registered_on,semester) values 
	 	('{stu_name}',{stu_age},'{stu_phone}','{stu_email}','{stu_address}','{stu_city}','{stu_state}','{stu_course}','{stu_parents}','{date}',{stu_semester});''')


	 	connector.commit()
	 	cursor.execute(f"select roll_no from student_rec where name='{stu_name}' and phone='{stu_phone}';")
	 	stu_roll_no=cursor.fetchone()[0]

	 	print(f'''\
##############################################################################
#                                                                            
#  STUDENT NAME : {stu_name}                                                 
#  STUDENT AGE  : {stu_age}                                                  
#  COURSE APPLIED : {stu_course}                                             
#  PARENTS/GUARDIAN NAME : {stu_parents}
#  PHONE NO. : {stu_phone}   
#  EMAIL : {stu_email}
#  ADDRESS : {stu_address}   
#  CITY : {stu_city} 
#  STATE : {stu_state}                         
#  ROLL_NO : {stu_roll_no}
#
############################################################################## 
''')

	 	print("\nREGISTERED SUCCESSFULLY")
stu2=Registration().Student()

class Attendence:
	def __init__(self,stu_name,stu_roll_no):

		self.stu_name=stu_name
		self.stu_roll_no=stu_roll_no






