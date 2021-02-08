from IPython.display import clear_output
from Functions import addQuestionToDb,takeQuiz,updateScore,displayScores,verifyLogin
from User import Super_user,Member
from datetime import date

#admin=Admin('1','Arun','Arun@123')
flag=True
while flag:
    clear_output()
    print('Quiz Application'.center(30,'='))
    print('1. Super_user\n2. Member\n3. Exit')
    choice=int(input('Login as :'))
    
    if choice==1:
        login=False
        while not login:
            name=input('Name: ')
            password=input('Password: ')
            login=verifyLogin(name,password)
            if login:
                break
            clear_output()
            print('Please provide correct details')
           
            
        clear_output()
        logged_in=True
        
        while logged_in:
            Option=int(input("Enter 1 to Add a Question:\nEnter 2 to Disply Scores of Members:\nEnter 3 to exit\n"))
            
            if Option==1:
                clear_output()
                addQuestionToDb()
                clear_output()
                
            elif Option==2:
                clear_output()
                displayScores()
                clear=input('Enter 1 to go back ')
                if clear==1:
                    clear_output()
                    continue
                    
            elif Option==3:
                logged_in=False

    elif choice==2:
        
        print('Enter your details to take the quiz: ')
        name=input('Name: ')
        Date = date.today()
        member=Member(name,Date)
        clear_output()
        
        test=input('Enter yes to take the test: ')
        while test.lower()=='yes':          
            clear_output()
            Score=takeQuiz()
            updateScore(name,Score)
            test=input('Do you want to take the quiz again ')
            if test.lower()=='no':
                print('thank you for taking the quiz. ')
            
            
    else:
        flag=False
        clear_output()