import sqlite3

class User():
    def __init__(self,name):
        self.name=name

class Super_user(User):
    def __init__(self,name,user_id,password):
        super.__init__(name)
        self.user_id = user_id
        self.password = password
        val=(self.user_id,self.name,self.password)
        sql="""INSERT INTO Admin(User_id,Name,Password)
                VALUES(?,?,?)"""
        conn=sqlite3.connect('Info.db')
        my_cursor=conn.cursor()
        my_cursor.execute(sql,val)
        conn.commit()
        conn.close()

class Member(User):
      def __init__(self,name,date,score=0):
        super().__init__(name)
        self.score = score
        self.date = date
        val=(self.name,self.date,self.score)
        sql="""INSERT INTO Members (Name,date,Score)
                VALUES(?,?,?)"""
        conn=sqlite3.connect('Info.db')
        crsr=conn.cursor()
        crsr.execute(sql,val)
        conn.commit()
        conn.close() 