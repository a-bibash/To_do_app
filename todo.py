# TO DO APP

task = []


def add_task():
    print("---------------------------------------------------------------------------")
    add = input("Enter the task you want to add: ")
    task.append(add)
    print("---------------------------------------------------------------------------")
    print(f"{add} is added to the task list")


def delete_task():
    print("---------------------------------------------------------------------------")
    if not task:
        print("There are no tasks to delete.")
    else:
        list_task()
        try:
            delete = int(input("Enter # of the task you want to delete "))
            if delete > 0 and delete < len(task):
                task.pop(delete)
                print(
                    "---------------------------------------------------------------------------")
                print(f"The #{delete} task is deleted ")
            else:
                print(
                    "---------------------------------------------------------------------------")
                print("Enter valid input")
        except ValueError:
            print(
                "---------------------------------------------------------------------------")
            print("Invalid Input")


def list_task():
    print("---------------------------------------------------------------------------")
    if not task:
        print("There are no task to list.")
        # return
    else:
        print('Current task are: ')
        for i, lis in enumerate(task):
            print(f'#{i+1}. {lis} ')


print("\n")
print("Welcome to your to do app :)")
while True:
    print("---------------------------------------------------------------------------")
    print("What do you want to do? ")
    print("1)Add task")
    print("2)Delete task")
    print("3)List task")
    print("4)Quit")
    print("---------------------------------------------------------------------------")
    choice = int(input("Enter your choice: "))
    if choice in [1, 2, 3, 4]:
        if choice == 1:
            add_task()

        elif choice == 2:
            delete_task()

        elif choice == 3:
            list_task()

        elif choice == 4:
            print(
                "---------------------------------------------------------------------------")
            print("Thank you for using the to-do app. Goodbye!")
            print(
                "---------------------------------------------------------------------------")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    else:
        print("---------------------------------------------------------------------------")
        print("Enter a valid input")
