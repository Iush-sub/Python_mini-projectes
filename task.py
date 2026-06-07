from operator import index
import json
import os
from textwrap import indent

todo_list = []

if os.path.exists("todo.json"):
    with open("todo.json", "r") as file:
        todo_list = json.load(file)
else:
    todo_list = []


def save():
    with open("todo.json", "w") as file:
        json.dump(todo_list, file, indent=4)


def menu():
    # this is how u create a function unlike in C or C++
    print("****Welcome to my todo application****")
    print("ENTER 1 to add new sets tasks")
    print("ENTER 2 to open the pending tasks and upgrade")
    print("ENTER 3 to delete your task list")
    print("ENTER 5 to Exit")
    print("\n")
    x = int(input("Value required: "))
    if x == 1:
        add_task()

    elif x == 2:
        view_task()

    elif x == 3:
        delete_task()


    elif x== 4:
        print("***thank you***")
    else:
        menu()


def add_task(s=None):
    print("***Type your task accordingly***")
    while s != "0":
        task = input("Enter your task: ")
        todo_list.append({"task": task, "status": "pending"})
        save()
        s = input("Press 0 to exit OR Press any key to continue listing: ")
        print("\n")
    menu()


def view_task():
    print("***task list***")
    for i, t in enumerate(todo_list):
        print(f"{i + 1}. {t['task']} [{t['status']}]")

    print("\n")
    s = input("to upgrade press 1: ")
    if s == "1":
        w = int(input("***task no. to be upgraded*** \n"))
        if 1 <= w <= len(todo_list):
            todo_list[w - 1]["status"] = "done"
            save()

        print("***task updated successfully*** ")
        menu()
        print("\n")


def delete_task():
    print("***task list***")
    for i, t in enumerate(todo_list):
        print(f"{i + 1}. {t['task']} [{t['status']}]")
    print("\n")
    e = int(input("***select the task number to delete***"))
    if 1 <= e <= len(todo_list):
        task = todo_list[e - 1]
        todo_list.remove(task)
        save()

    else:
        menu()

    menu()




if __name__ == '__main__':
    menu()
