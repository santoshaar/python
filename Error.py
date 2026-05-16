#This will read the file sample.txt file and it will display if the file is having errors and it will list out the errors. 

file_path = r"C:\Users\sanguest555\AppData\Local\Programs\Python\Python314\All programs\sample.txt"

error_found = False
#We are using open file path read only
try:
    with open(file_path, "r") as file:
        for line in file:
            # Check if line contains the word "error"
            if "error" in line.lower():
                print(line.strip())
                error_found = True
#using if else statement if errors found or no errors found. 
    if not error_found:
        print("No errors found")

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("An error occurred:", e)