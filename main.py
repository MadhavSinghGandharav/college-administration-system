# Source code for collge-managment system

# REGISTRATION CLASS
import random

class Registration:

	 def __init__(self):
	 	pass

	 def Student(self):
	 	print("--STUDENT REGISTRATION--")

	 	stu_name=input("ENTER NAME : ")
	 	stu_age=int(input("ENTER AGE : "))
	 	stu_course=input("ENTER COURSE : ")
	 	stu_parents=input("ENTER PARENTS?GUARDIAN NAME : ")
	 	fees_reciet_no=int(input("ENTER FEES RECIET NUMBER : "))

	 	application_no="KRMU"+str(random.randint(100000,999999))

	 	print(f'''\
##############################################################################
#                                                                            
#  STUDENT NAME : {stu_name}                                                 
#  STUDENT AGE  : {stu_age}                                                  
#  COURSE APPLIED : {stu_course}                                             
#  PARENTS/GUARDIAN NAME : {stu_parents}                                     
#  APPLICATION NO : {application_no}
#
############################################################################## 
''')

	 	print("\nREGISTERED SUCCESSFULLY")



