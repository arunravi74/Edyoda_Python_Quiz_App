from database import *
from User import Super_user,Member
from IPython.display import clear_output
def addQuestionToDb():
    l=['Question','Topic','difficulty_level','Option_A','Option_B','Option_C','Option_D','Corr_Ans']
    val=(tuple([input(f'Enter {x}: ') for x in l]))
    print(val)
    sql="""INSERT INTO questions (Question,Topic,difficulty_level,Option_A,Option_B,Option_C,Option_D,Corr_Ans)
                    VALUES(?,?,?,?,?,?,?,?)"""
    conn=sqlite3.connect('Info.db')
    my_cursor=conn.cursor()
    my_cursor.execute(sql,val)
    conn.commit()
    conn.close()
    print('Question has been added successfully!')

   
def takeQuiz():
    Score=0
    conn=sqlite3.connect("Info.db")
    my_cursor=conn.cursor()
    sql = "SELECT * FROM questions ORDER BY random() limit 5"
    my_cursor.execute(sql)    
    result=my_cursor.fetchall()
    conn.close()
    for x in result:
        clear_output()
        print(f'Question:{x[0]}')
        print(f'A:{x[3]}')
        print(f'B:{x[4]}')
        print(f'C:{x[5]}')
        print(f'D:{x[6]}')
        answer=(input('Enter the option: '))
        if answer==x[7]:
            Score+=1
    clear_output()
    for x in result:
        print(f'Question:{x[0]}')
        print(f'Correct Answer:{x[7]}')
    print("You got: {} Out of 5".format(Score))
    return Score

def updateScore(name,Score):
    sql="UPDATE Members SET Score=? WHERE Name=?"
    conn=sqlite3.connect("Info.db")
    my_cursor=conn.cursor()
    my_cursor.execute(sql,(Score,name))
    conn.commit()
    conn.close()
    return ('Score has been updated successfully!')

def displayScores():
    conn=sqlite3.connect('Info.db')    
    sql = 'select * from Members;'
    my_cursor=conn.cursor()
    my_cursor.execute(sql)
    results=my_cursor.fetchall()
    conn.commit()
    conn.close()
    print ("{:<30} {:<30} {:<30}".format('Name','Date','Score')) 
    for x in results:
        print ("{:<30} {:<30} {:<30}".format(x[0],x[1],x[2])) 
    print('\n')

def verifyLogin(name,password):
    sql="SELECT Password from Admin WHERE Name=?"
    conn=sqlite3.connect("Info.db")
    my_cursor=conn.cursor()
    my_cursor.execute(sql,(name,))
    result=my_cursor.fetchall()
    return result[0][0]==password