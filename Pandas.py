import pandas as pd

myData = {
    'Patient Name': [],
    'Patient attendance': []
}

try:
    while(True):
        print("Select: add, delete, search, exit")
        option = input("Enter one of the options above: ")

        if(option.lower() == "add"):
            while(True):
                name = input("Enter the name of the patient: ")
                attend = int(input("Enter the attendance amount: "))

                myData["Patient Name"].append(name)
                myData["Patient attendance"].append(attend)


                print(f"{name} has been added to the list \n")
                choose = input("Would you like to add another one (y/n): ")

                if(choose.lower() == "n"):
                    break
                
        elif (option.lower() == "delete"):
            while(True):
                removeName = input("Enter the name you want to delete: ")
                
                if removeName in myData["Patient Name"]:
                    idx = myData["Patient Name"].index(removeName)
                    myData["Patient Name"].pop(idx)
                    myData["Patient attendance"].pop(idx)

                    print(f"{removeName} has been deleted for the list")

                    choose = input("Would you like to delete another one (y/n): ")

                    if(choose.lower() == "n"):
                        break
                else:
                    print(f"{removeName} does not exist in the list")
            
        elif (option.lower() == "search"):
            searchName = input("Enter the name you are searching for: ")
            
            if searchName in myData["Patient Name"]:
                indx = myData["Patient Name"].index(searchName)

                data = pd.DataFrame(myData)

                print(data.loc[indx])
            else:
                print("This person does not exist")
                

        elif (option.lower() == "exit"):
            break

except:
    print("There is an error in the code \n" + ValueError)

new = pd.DataFrame(myData)

print(new)
