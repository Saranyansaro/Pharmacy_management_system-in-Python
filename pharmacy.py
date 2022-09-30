import os
import platform
import csv
import pandas as pd
from csv import writer

def logins():
	x = "#" * 30
	y = "=" * 28
	global bye  # Making Bye As Super Global Variable
	bye = "\n {}\n# {} #\n# ===> Tataaa Bubyeeee <===  #\n# ===> TAKECARE <===  #\n# {} #\n {}".format(x, y, y, x)

	print(" 1) Customer 2) Admin")
	admin = int(input("Select your option: "))
	if admin==1:
		username = 'customer'
		password = 'customer'

		userInput = input("What is your username?\n")

		if userInput == username:
			a = input("Enter Password?\n")
			if a == password:
				print("Welcome!")

				def medicine():
					x = "#" * 30
					y = "=" * 28
					global bye  # Making Bye As Super Global Variable
					bye = "\n {}\n# {} #\n# ===> Tataaa Bubyeeee <===  #\n# ===> TAKECARE <===  #\n# {} #\n {}".format(
						x, y, y, x)  # Will Print GoodBye Message

					print(""" 

				  ------------------------------------------------------
				 |======================================================| 
				 |======= Welcome To Pharmacy Management System	========|
				 |======================================================|
				  ------------------------------------------------------

				Enter 1 : List of Medicine 
				Enter 2 : List of Symptoms
				Enter 3 : Expiry Check  
				Enter 4 : Strength(mg) & Category
				Enter 5 : Whole table
				
						->LOGOUT<-

						""")

					try:  # Using Exceptions For Validation
						userInput = int(input("Please Select An Above Option: "))  # Will Take Input From User
					except ValueError:
						exit("\nHy! That's Not A Number")  # Error Message
					else:
						print("\n")  # Print New Line

					# Checking Using Option
					if (userInput == 1):  # This Option Will Print List Of Students
						data = pd.read_csv("Medicine_list.csv", encoding="ISO-8859-1")
						df = pd.DataFrame(data)
						print(df[['MEDICINE_NAMES']])
						print("----------------------")
						runAgn = input("\nwant To Run Again Y/n: ")
						if (runAgn.lower() == 'y'):
							if (platform.system() == "Windows"):
								print(os.system('cls'))
								medicine()
							else:
								print(os.system('clear'))
						else:
							quit(bye)  # Print GoodBye Message And Exit The Program

					elif (userInput == 2):  # This Option Will Add New Student In The List
						data = pd.read_csv("Medicine_list.csv", encoding="ISO-8859-1")
						df = pd.DataFrame(data)
						print(df[['SYMPTOMS']])
						print("----------------------")
						runAgn = input("\nwant To Run Again Y/n: ")
						if (runAgn.lower() == 'y'):
							if (platform.system() == "Windows"):
								print(os.system('cls'))
								medicine()
							else:
								print(os.system('clear'))
						else:
							quit(bye)

					elif (userInput == 3):  # This Option Will Search Student From The List
						data = pd.read_csv("Medicine_list.csv", encoding="ISO-8859-1")
						df = pd.DataFrame(data)
						print(df[['MEDICINE_NAMES', 'EXPIRY_DATE']])
						print("--------------------------------------")
						runAgn = input("\nwant To Run Again Y/n: ")
						if (runAgn.lower() == 'y'):
							if (platform.system() == "Windows"):
								print(os.system('cls'))
								medicine()
							else:
								print(os.system('clear'))
						else:
							quit(bye)

					elif (userInput == 4):
						data = pd.read_csv("Medicine_list.csv", encoding="ISO-8859-1")
						df = pd.DataFrame(data)
						print(df[['MEDICINE_NAMES', 'STRENGTH', 'FORM', 'CATEGORY']])
						print("-------------------------------------------------------")
						runAgn = input("\nwant To Run Again Y/n: ")
						if (runAgn.lower() == 'y'):
							if (platform.system() == "Windows"):
								print(os.system('cls'))
								medicine()
							else:
								print(os.system('clear'))
						else:
							quit(bye)

					elif (userInput == 5):
						data = pd.read_csv("Medicine_list.csv", encoding="ISO-8859-1")
						df = pd.DataFrame(data)
						print(df[['MEDICINE_NAMES', 'STRENGTH', 'FORM', 'CATEGORY', 'CORE_LIST', 'INNOVATOR',
								  'MOST_SOLD_GENERIC', 'SYMPTOMS', 'EXPIRY_DATE']])
						print(
							"--------------------------------------------------------------------------------------------------------------------------------")
						runAgn = input("\nwant To Run Again Y/n: ")
						if (runAgn.lower() == 'y'):
							if (platform.system() == "Windows"):
								print(os.system('cls'))
								medicine()
							else:
								print(os.system('clear'))
						else:
							quit(bye)
					elif (userInput == logout):
						exit()
					elif (userInput < 1 or userInput > 4):
						print("Please Enter Valid Option")
						runAgn = input("\nwant To Run Again Y/n: ")
						if (runAgn.lower() == 'y'):
							if (platform.system() == "Windows"):
								print(os.system('cls'))
								medicine()
							else:
								print(os.system('clear'))
						else:
							quit(bye)
				medicine()

			else:
				print("That is the wrong password.")
				runAgn = input("\nwant To Run Again Y/n: ")
				if (runAgn.lower() == 'y'):
					if (platform.system() == "Windows"):
						print(os.system('cls'))
						logins()
					else:
						print(os.system('clear'))
				else:
					quit(bye)
		else:
			print("That is the wrong username.")
			runAgn = input("\nwant To Run Again Y/n: ")
			if (runAgn.lower() == 'y'):
				if (platform.system() == "Windows"):
					print(os.system('cls'))
					logins()
				else:
					print(os.system('clear'))
			else:
				quit(bye)
	elif admin==2:
		username = 'admin'
		password = 'admin'

		userInput = input("What is your username?\n")

		if userInput == username:
			a = input("Enter Password?\n")
			if a == password:
				print("Welcome! to Admin Page")
			else:
				print("That is the wrong password.")
				runAgn = input("\nwant To Run Again Y/n: ")
				if (runAgn.lower() == 'y'):
					if (platform.system() == "Windows"):
						print(os.system('cls'))
						logins()
					else:
						print(os.system('clear'))
				else:
					quit(bye)
		else:
			print("That is the wrong username.")
			runAgn = input("\nwant To Run Again Y/n: ")
			if (runAgn.lower() == 'y'):
				if (platform.system() == "Windows"):
					print(os.system('cls'))
					logins()
				else:
					print(os.system('clear'))
			else:
				quit(bye)
	elif (admin==0 or admin<0 or admin>2):
		print("Invalid number")
		runAgn = input("\nwant To Run Again Y/n: ")
		if (runAgn.lower() == 'y'):
			if (platform.system() == "Windows"):
				print(os.system('cls'))
				logins()
			else:
				print(os.system('clear'))
		else:
			quit(bye)
logins()
def validation():
		try:
			print("1) Stock available "
				  "2) Add Product to Stock "
				  "3) Add Users"
				  )
			stock = int(input("Enter your choice: "))
			if stock == 1:
				data = pd.read_csv("Medicine_list.csv", encoding="ISO-8859-1")
				df = pd.DataFrame(data)
				print("Available stock: ",len(df))
				runAgn = input("\nwant To Run Again Y/n: ")
				if (runAgn.lower() == 'y'):
					if (platform.system() == "Windows"):
						print(os.system('cls'))
						validation()
					else:
						print(os.system('clear'))
				else:
					quit(bye)
			elif stock == 2:
				# x = list(map(str, input("Enter multiple strings: ").split()))
				x = [str(x) for x in input("Enter multiple strings: ").split()]
				print("Number of list is: ", x)
				with open('Medicine_list.csv', 'a') as f_object:
					writer_object = writer(f_object)
					writer_object.writerow(x)
					f_object.close()
					print("Row added Successfully")
					runAgn = input("\nwant To Run Again Y/n: ")
					if (runAgn.lower() == 'y'):
						if (platform.system() == "Windows"):
							print(os.system('cls'))
							validation()
						else:
							print(os.system('clear'))
					else:
						quit(bye)
			elif stock == 3:
				print("\t\t	USER DATABASE")
				print("------------------------------------------------------------------------")

				cond = input("Do you want to enter users details (Y/N) : ")
				cond.lower()

				if cond == "y":
					user_id = input(" Enter User_ID : ")
					user_name = input(" Enter User_name : ")
					user_dob = input(" Enter User_dob : ")
					user_number = input(" Enter User_number : ")
					user_password = input(" Enter User_password : ")

					with open("user_data.txt", 'a', encoding='utf-8') as f:
						f.write(user_id)
						f.write("\t\t")
						f.write(user_name)
						f.write("\t\t")
						f.write(user_dob)
						f.write("\t\t")
						f.write(user_number)
						f.write("\t\t")
						f.write(user_password)
						f.write("\n")
					print("Data Saved!")
				with open("user_data.txt", "r+") as file1:
					print(file1.read())

		except ValueError:
			exit("\nHy! That's Not A Number")
			runAgn = input("\nTry Again: ")
			if (runAgn.lower() == 'y'):
				if (platform.system() == "Windows"):
					print(os.system('cls'))
					medicine()
				else:
					print(os.system('clear'))
			else:
				quit(bye)
		else:
			print("\n")

validation()

def runAgain():
	runAgn = input("\nwant To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"):
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		validation()
		runAgain()
	else:
		quit(bye)
runAgain()