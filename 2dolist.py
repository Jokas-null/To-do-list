#To do list
#Made by Jokas

from os import system, name

def clearTerminal():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def saveTask():
    temp = input("Add a task now: ")
    f = open ('tasks.txt','a')
    f.write(temp)
    f.write("\n")
    f.close()

def displayTasks():
    f = open ('tasks.txt','r')
    kien = f.readlines() 
    f.close()
    cont = 1
    for todo in kien:
        print(f"{cont}. {todo.strip()}")
        cont+=1

def deleteTask():
    displayTasks()
    taskIndexToDelete = int(input("Select a task to delete: ")) - 1
    cont = 0

    f = open ('tasks.txt','r')
    kien = f.readlines() 

    for todo in kien:
        if(cont == taskIndexToDelete):
            kien.pop(taskIndexToDelete)
        cont+=1

    f.close()

    with open("tasks.txt", 'w') as file:
        file.writelines(kien)

def main():
    
    print(r'''
 _____ ___  ____   ___    _     ___ ____ _____
|_   _/ _ \|  _ \ / _ \  | |   |_ _/ ___|_   _|
  | || | | | | | | | | | | |    | |\___ \ | |
  | || |_| | |_| | |_| | | |___ | | ___) || |
  |_| \___/|____/ \___/  |_____|___|____/ |_|
''')

    print("Created by Jokas\n")
    print("1. Add a task")
    print("2. Display tasks")
    print("3. Delete a task")
    print("4. Exit")

    try:
        option = int(input("Select an option: "))
        
        if(option == 1):
            clearTerminal()
            saveTask()
            clearTerminal()
            main()
        elif(option == 2):
            clearTerminal()
            displayTasks()
            input()
            clearTerminal()
            main()
        elif(option == 3):
            clearTerminal()
            deleteTask()
            clearTerminal()
            main()
        elif(option == 4):
            clearTerminal()
            print("Bye")   
    except:
        print("Invalid Data")

main()