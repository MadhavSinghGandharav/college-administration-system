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

	 def Register_student(self,stu_name,stu_age,stu_phone,stu_email,stu_address,stu_city,stu_state,stu_course,stu_parents,date,stu_semester):
	 	

	 	cursor.execute(f'''insert into student_rec
	 	(name,age,phone,email,address,city,state,course,parents,registered_on,semester) values 
	 	('{stu_name}',{stu_age},'{stu_phone}','{stu_email}','{stu_address}','{stu_city}','{stu_state}','{stu_course}','{stu_parents}','{date}',{stu_semester});''')


	 	connector.commit()
	 	cursor.execute(f"select roll_no from student_rec where name='{stu_name}' and phone='{stu_phone}';")
	 	stu_roll_no=cursor.fetchone()[0]

	 	print(f'''\n\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
STUDENT NAME : {stu_name}
ROLL NUMBER : {stu_roll_no}
PHONE NUMBER :{stu_phone}
COURSE : {stu_course} 
PARENTS NAME : {stu_parents}
ADDRESS : {stu_address} | CITY : {stu_city} | STATE : {stu_state}

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#''')


	 	print("\nREGISTERED SUCCESSFULLY (to confirm go to CHECK RECORDS )")

	 def Check_records(self,stu_roll_no):

	 	cursor.execute(f"select * from student_rec where roll_no={stu_roll_no};")

	 	info=cursor.fetchone()
	 	
	 	if info!=None:

	 		print(f'''\n\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    STUDENT NAME : {info[1]} 
    ROLL NO : {info[0]}
    COURSE : {info[8]} , SEMESTER : {info[11]}
    PARENTS : {info[9]}
    PHONE : {info[3]}
    ADDRESS : {info[5]} , CITY : {info[6]} , STATE : {info[7]}
    MAIL : {info[4]}

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#''')

	 def Update_records(self,stu_roll_no):
	 	cursor.execute(f"delete from student_rec where roll_no={stu_roll_no};")
	 	connector.commit()

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
	 	date=datetime.today().strftime('%Y-%m-%d')

	 	cursor.execute(f'''insert into student_rec
	 	(roll_no,name,age,phone,email,address,city,state,course,parents,registered_on,semester) values 
	 	({stu_roll_no},'{stu_name}',{stu_age},'{stu_phone}','{stu_email}','{stu_address}','{stu_city}','{stu_state}','{stu_course}','{stu_parents}','{date}',{stu_semester});''')

	 	connector.commit()

	 	print("\nRECORD UPDATED SUCCESSFULLY\n")



class Attendance:

	def __init__(self):

		pass

	def attendance(self,stu_name,stu_roll_no,course):
		cursor.execute(f"select roll_no from student_rec where roll_no={stu_roll_no};")
		try:
			info=cursor.fetchone()[0]
		except:
			info=None

		if info!=None and stu_roll_no not in Attendence_students_rollno:
			cursor.execute(f"insert into stu_attendance values({stu_roll_no},'{stu_name}','{course}','p');")
			connector.commit()

			Attendence_students_rollno.append(stu_roll_no)

			print("\nATTENDANCE DONE")


		elif  info==None:
			print("RECORD NOT FOUND CHECK YOUR ROLL NO.")

		else:
			print("ATTENDANCE ALREADY DONE!")

	def Check_total_attendance(self,stu_roll_no):
		cursor.execute(f"select count(attendance) from stu_attendance where roll_no={stu_roll_no};")
		count=cursor.fetchone()
		cursor.execute(f"select name  from student_rec where roll_no={stu_roll_no};")
		name=cursor.fetchone()

		print(f"STUDENT NAME : {name[0]} | TOTAL ATTENDANCE : {count[0]}")

Attendence_students_rollno=[]
while True:

	
	
	print('''\n\n -----------------K.R. MANGALAM UNIVERSITY ADMISNISTRATION SYSTEM-------------------\n\n
1. STUDENT ATTENDANCE 
2. ADMINISTRATION TASKS (only for admins)''')

	ch=input("ENTER CHOICE : ")

	if ch=="1":

		print("\nSTUDENT ATTENDANCE\n")

		stu_name=input("\nENTER STUDENT NAME : ")
		stu_roll_no=input("ENTER ROLL NO. : ")
		course=input("ENTER YOUR COURSE (BBA/MBA/BSC/BTECH) :")

		try :

			Attendance().attendance(stu_name,int(stu_roll_no),course)
		except:

			print("ENTER VALID ROLL NUMBER")
	elif ch=="2":

		print("\nADMINISTRATION")
		passwd=input("ENTER ADMIN PASSWORD : ")

		if passwd=="123admin":


			while True:
				print('''\n\n ------------------K.R. MANGALAM UNIVERSITY ADMISNISTRATION SYSTEM( ADMINS ONLY)-------------------\n
1.STUDENT REGISTRATION
2.CHECK STUDENT RECORD
3.UPDATE RECORD
4.CHECK TOTAL ATTENDANCE
5.MAIN MENU\n''')
				ch2=input("ENTER CHOICE : ")
				if ch2=="1":
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

				
					Registration().Register_student(stu_name,stu_age,stu_phone,stu_email,stu_address,stu_city,stu_state,stu_course,stu_parents,date,stu_semester)

				elif ch2=="2":

					print("\n--RECORD CHECKING--\n")
					stu_roll_no=input("ENTER STUDENT ROLL NO. : ")

					try :
						Registration().Check_records(int(stu_roll_no))
					except:
						print("ENTER VALID ROLL NUMBER")

				elif ch2=="3":
					print("\n--UPDATE RECORD--\n")

					stu_roll_no=input("ENTER STUDENT ROLL NO. : ")

					try :
						Registration().Update_records(int(stu_roll_no))
					except:
						print("ENTER VALID ROLL NUMBER")

				elif ch2=="4":
					print("\n--TOTAL ATTENDANCE-\n")

					stu_roll_no=input("ENTER STUDENT ROLL NO. : ")

					try :
						Attendance().Check_total_attendance(int(stu_roll_no))
					except:
						print("ENTER VALID ROLL NUMBER")



				else:
					break


		else:
			print("\nWRONG PASSWORD!")

	 	            
				


	else:
		break
