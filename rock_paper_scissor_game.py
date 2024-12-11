import random
import mysql.connector as my
from datetime import datetime

conn = None
cursor = None

def connect_to_db():
    global conn, cursor
    conn = my.connect(host='localhost',user='root',passwd='12345')
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS GAME")
    cursor.execute("USE GAME")
    cursor.execute("CREATE TABLE IF NOT EXISTS SCORE(S_NO INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(30) NOT NULL, SCORE INT NOT NULL, P_DATE_TIME DATETIME NOT NULL)")
    conn.commit()


def game():
    comp_input = random.randint(1, 3)  # Random choice for the computer (1: Rock, 2: Paper, 3: Scissors)
    print("Press:\n\t 1 for Rock\n\t 2 for Paper\n\t 3 for Scissors")
    try:
        u = int(input("Your choice: "))
        while u not in [1, 2, 3]:
            print("Invalid input. Please enter 1 for Rock, 2 for Paper, or 3 for Scissors.")
            u = int(input("Your choice: "))
        
    except ValueError as e:
        print(e)
        return game()  

    if comp_input == u:
        print("Match Draw!")
        value(comp_input)
        return "Draw"
    elif (comp_input == 1 and u == 3) or (comp_input == 2 and u == 1) or (comp_input == 3 and u == 2):
        print("Computer wins the round!")
        value(comp_input)
        return "Computer"
    else:
        print("User wins the round!")
        value(comp_input)
        return "User"

def value(data):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"Computer choice: {choices[data]}")

def main():
    count = 0
    comp_score = 0
    user_score = 0
    draw_score = 0

    while count < 5:  # Play 5 rounds
        print(f"\n****** Round {count + 1} ******")
        res = game()
        if res == "Computer":
            comp_score += 1
        elif res == "User":
            user_score += 1
        elif res == "Draw":
            draw_score += 1
        count += 1

    # Determine the final result
    timestamp = datetime.now()
    time = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    if comp_score > user_score:
        sql = "INSERT INTO SCORE (Name, Score, P_DATE_TIME) VALUES ('Computer', %s, %s);"
        cursor.execute(sql,(comp_score,time))
        conn.commit()
        print("\nResult: Computer wins the game!!")
    elif comp_score == user_score:
        print("\nResult: Match draw!! Play again.")
    else:
        sql = "INSERT INTO SCORE (Name, Score, P_DATE_TIME) VALUES ('User', %s, %s);"
        cursor.execute(sql,(user_score,time))
        conn.commit()
        print("\nResult: User wins the game!!")

    # Display the scorecard
    print("\n****** Score Card ******")
    print(f"Computer Score: {comp_score}")
    print(f"User Score:     {user_score}")
    print(f"Draw rounds:    {draw_score}")

if __name__ == "__main__":
    connect_to_db()
    main()
