#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('todo.db')                   # Load the todo database

def add_task():

    t = input("Please enter the task: ")

    p = int(input("Please enter the priority (Enter 0 of no priority): "))

    dd = input("Please enter due date (YYYY-MM-DD): ")

    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO todo VALUES(?, ?, ?);", (p, t, dd)) # insert values in to the todo table


def display_tasks():

    with con:
        cur = con.cursor()    
        cur.execute("SELECT * FROM todo")

        rows = cur.fetchall()

        for row in rows:
            print(row)


def complete_task():
    # Todo:
    # list all tasks with numbers 
    # put todays date next to completed task
    
    with con:
        cur = con.cursor()    
        cur.execute("SELECT task FROM todo")

        rows = cur.fetchall()

#        i = 1
        for i, row in enumerate(rows):
#        for row in rows:
            print(i+1, row)
#            print(str(i) + ' ' + str(row))
#            i+=1
            
        choice = int(input("Please enter choice: "))
        print(rows[choice-1])

        cur.execute("DELETE FROM todo WHERE task=rows[choice-1];")               # Deletes the task
       
        choice = 0



# Main program
exit_status = 1                 # Intialize exit status to true, for program loop 

while exit_status:         # Program loop
    choice = 0                  # Intialize int for menu choice

    print("Menu:")
    print("1) Add task.")
    print("2) Veiw tasks.")
    print("3) Mark a task as complete.")
    print("4) Exit.")
    choice = int(input("Please enter choice: "))

    if choice == 1:
        choice = 0
        add_task()

    elif choice == 2:
        choice = 0
        display_tasks()
       
    elif choice == 3:
        choice = 0
        complete_task()
 
    elif choice == 4:
        exit_status = 0                # Make exit status false to exit program

    else:
        choice = int(input("Unknown input please enter another: "))

