import mysql.connector as ms
# for adding delay in printing messages
import time     

conn = None
cursor = None

def manageDatabase():
    global conn, cursor
    # connecting database
    conn = ms.connect(host='localhost', user='root',password='12345')
    # creating cursor
    cursor = conn.cursor()

    # creating a database
    q = "CREATE DATABASE IF NOT EXISTS TODOLIST"
    cursor.execute(q)
    cursor.execute("USE TODOLIST")

    # creating a table
    tab = "CREATE TABLE IF NOT EXISTS TASKS (TASK_ID INTEGER(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, Task VARCHAR(100), Status VARCHAR(10) DEFAULT 'No' CHECK (Status IN ('Yes', 'No')));"
    cursor.execute(tab)

    # saving changes made in database
    conn.commit()

# function for adding a new task
def addTask(task):
    global cursor
    sql = "INSERT INTO TASKS (TASK, STATUS) VALUES (%s, %s)"
    cursor.execute(sql,(task, "No"))
    conn.commit()
    print("Task added successfully...")

# function for updating the status of a task
def updateStatus(task_ID, status):
    print("Updating Status of Task: ", task_ID,"\n")
    sql = "UPDATE TASKS SET STATUS = %s WHERE TASK_ID = %s"
    cursor.execute(sql,(status,task_ID))
    conn.commit()
    print("Task updated successfully...")

# function for updating the name of task
def updateTaskName(task_ID, name):
    print("Updating Name of Task: ", task_ID,"\n")
    sql = "UPDATE TASKS SET TASK = %s WHERE TASK_ID = %s"
    cursor.execute(sql,(name, task_ID))
    conn.commit()
    print("Task updated successfully...")

# function for deleting a task
def deleteTask(task_ID):
    print("Deleting task: ",task_ID,"\n")
    sql = "DELETE FROM TASKS WHERE TASK_ID=%s"
    cursor.execute(sql, (task_ID,))
    conn.commit()
    print("Task deleted successfully...")

def deleteAllTasks():
    sql = "DELETE FROM TASKS"
    cursor.execute(sql)
    conn.commit()
    print("Deleted all tasks...\n")

# function for viewing all tasks
def viewTasks():
    sql = "SELECT * FROM TASKS"
    cursor.execute(sql)
    rows = cursor.fetchall()
    if not rows:
        print("No tasks found...\n")
    else:
        print("Viewing all tasks...\n")
        for row in rows:
            print(row)

# viewing incompleted tasks
def viewIncompletedTasks():
    sql = "SELECT * FROM TASKS WHERE STATUS = 'No' "
    cursor.execute(sql)
    rows = cursor.fetchall()
    if not rows:
        print("Your all tasks are completed...\n")
    else:
        print("Viewing incompleted tasks...\n")
        for row in rows:
            print(row)

def menu():
    while(True):
        try:
            time.sleep(1)
            print("\n1. Add a task\n2. Update a task\n3. Delete a task\n4. Delete all tasks\n5. View all tasks\n6. View incompleted tasks\n7. Exit")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    task = input("Enter the task: ")
                    addTask(task)

                case 2:
                    print("\t1. Update task status\n\t2. Update task name")
                    ch = int(input("Enter your choice: "))
                    task_ID = int(input("Enter task ID: "))
                    match ch:
                        case 1:
                            status = input("Enter status (yes/no):")
                            if status in ['Yes', 'No']:
                                updateStatus(task_ID, status)
                            else:
                                print("Invalid status. Use 'Yes' or 'No'.")
                        case 2:
                            name = input("Enter new name: ")
                            updateTaskName(task_ID, name)
                        case _:
                            print("Invalid choice")

                case 3:
                    task_ID = int(input("Enter task ID to delete: "))
                    deleteTask(task_ID)
                case 4:
                    deleteAllTasks()
                case 5:
                    viewTasks()
                case 6:
                    viewIncompletedTasks()
                case 7:
                    print("Exiting...")
                    if conn:
                        cursor.close()
                        conn.close()
                    exit()
                case _:
                    print("Invalid choice. Please choose a valid option.")
        except Exception as e:
            print(f"Error occured: {e}\nTry Again")
    


if __name__ == "__main__":
    manageDatabase()
    print("**************TO DO LIST**************")
    menu()
    


