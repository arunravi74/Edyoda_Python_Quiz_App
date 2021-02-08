import sqlite3
from IPython.display import clear_output
"""connection=sqlite3.connect("Info.db")

sql=\"""CREATE TABLE if not EXISTS questions(
        Question VARCHAR(50),
        Topic     VARCHAR(20),
        difficulty_level VARCHAR(20),
        Option_A  VARCHAR(20),
        Option_B  VARCHAR(20),
        Option_C  VARCHAR(20),
        Option_D  VARCHAR(20),
        Corr_Ans  VARCHAR(1));\"""
my_cursor=connection.cursor()
my_cursor.execute(sql)
connection.commit()
connection.close()"""

#Adding some questions

"""questions=[('what is capital of India?','General','easy','delhi','bangalore','punjab','hyderabad','A'),
           ('what is 2/2 = ?','Maths','easy','2','1','3','0','B'),
           ('What is National bird of India?','General','easy','Eagle','Peigon','peacock','hummingbird','C'),
           ('where is TajMahal located in india?','General','easy','Agra','Pune','Jaipur','none of the above','A'),
           ('what is the national sports of India?','Sports','easy','Cricket','Hockey','FootBall','VolleyBall','B'),
           ('OS computer abbreviation ?','Computer Science','medium','Order of Significance','Open Software','Operating System','Optical Sensor','C')]
sql=\"""INSERT INTO questions (Question,Topic,difficulty_level,Option_A,Option_B,Option_C,Option_D,Corr_Ans)
                 VALUES(?,?,?,?,?,?,?,?);\"""
conn=sqlite3.connect('Info.db')
my_cursor=conn.cursor()
my_cursor.executemany(sql,questions)
my_cursor.execute("SELECT * FROM questions")
result=my_cursor.fetchall()
for x in result:
    print(x)
conn.commit()
conn.close()"""

"""conn=sqlite3.connect('Info.db')
my_cursor=conn.cursor()
my_cursor.execute(\"""CREATE TABLE IF NOT EXISTS Admin(
            User_id INTEGER PRIMARY KEY,
            Name  VARCHAR(30),
            Password VARCHAR(20))
             \""")

my_cursor.fetchall()
conn.commit()
conn.close()"""

"""conn=sqlite3.connect('Info.db')
my_cursor=conn.cursor()
my_cursor.execute("insert into Admin values(1,'Arun','Arun@123');")
my_cursor.fetchall()
conn.commit()
conn.close()"""

"""conn=sqlite3.connect('Info.db')
my_cursor=conn.cursor()
my_cursor.execute(\"""CREATE TABLE IF NOT EXISTS Members(
            Name  VARCHAR(30),
            Date DATE,
            Score INTEGER DEFAULT 0);
              \""")

my_cursor.fetchall()
conn.commit()
conn.close()"""