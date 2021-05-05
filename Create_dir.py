import os
import time

authorization = input("Do you want to make new directories y, n, mois: ")

def spliter(string_input):
	output = string_input.split(',')
	return output

def define_Path(auth):
	if auth == "y":
		input_folders = input("What folder do you want to create (separate with \",\" and no space: ")
			
	elif auth == "mois":
		path = str("Janvier,Février,Mars,Avril,Mai,Juin,Juillet,Août,Septembre,Octobre,Novembre,Décembre")

	else :
		return "No file was created"
	
	
	return spliter(path)



def create_Dir(auth):
	path = define_Path(auth)
	for i in range(len(path)):
			if not os.path.exists(path[i]):
				os.mkdir(path[i])
				print(f"{path[i]} has been created.")
			else:
				print(f"{path[i]} already exists.")


create_Dir(authorization)

time.sleep(5)