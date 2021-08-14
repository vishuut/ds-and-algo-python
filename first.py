#First Python code file can be used for demo codes

myArray = ["Dhurub", "Ata", "Ana", "Vishal", "Sakshi", "Tarun", "Suhel",
            "PK", "Shubham"]

print(len(myArray))

def findVishal(arr):
    foundAt = 'not Found'
    for i in range(0, len(arr)):
        print("running")
        if arr[i] == "Vishal":
            foundAt = "at " + str(i)
            break

    return foundAt

print("Found Vishal : ", findVishal(myArray))
