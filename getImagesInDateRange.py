import os
import time
import datetime
import time

def walk(dir):
	file_list = []
	for root, _, filenames in os.walk(dir):
		for f in filenames:	
			file_path = root + "/" + f
			created = os.path.getmtime(file_path)
			file = [file_path, datetime.datetime.strptime(time.ctime(created), "%a %b %d %H:%M:%S %Y").strftime("%m/%d/%Y %H:%M:%S")]
			file_list.append(file)
	return file_list

def get_images_only(file_list):
	valid = ["jpg", "gif", "png"]
	new_list = []
	for file in file_list:
		f = file[0].split(".")
		if f[-1].lower() not in valid:
			continue
		new_list.append(file)
	return new_list

def compare_time(t1, t2):
	t1 = time.strptime(t1, "%m/%d/%Y %H:%M:%S")
	t2 = time.strptime(t2, "%m/%d/%Y %H:%M:%S")
	if t1 > t2:
		return True
	return False

def get_specific_range(file_list, lower, higher):
	new_list = []
	for file in file_list:
		if compare_time(file[1], lower) == False or compare_time(file[1], higher) == True:
			continue
		new_list.append(file)
	return new_list

def print_list(file_list):
	with open("output.txt", "w") as f:
		for file in file_list:
			f.write(file[0] + "\n")

def main():
	try:
		folder = input("Enter the path of your file: ")
		assert os.path.exists(folder), "Path does not exist"
	except:
		print("Path does not exist.")
		os.system("pause")
		exit()
	dateold = input("Please input the lower date range (MM/DD/YYYY): ")
	timeold = input("Please input the lower time range (HH:MM:SS): ")
	datenew = input("Please input the higher date range (MM/DD/YYYY): ")
	timenew = input("Please input the higher time range (HH:MM:SS): ")
	old = dateold + " " + timeold
	new = datenew + " " + timenew
	file_list = walk(folder)
	file_list = get_specific_range(file_list, old, new)
	file_list = get_images_only(file_list)
	print_list(file_list)

main()