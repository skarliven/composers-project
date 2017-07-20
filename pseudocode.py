"""Greeting the User"""

def greeting_users():
    print "Welcome to our music journey about composers!!"
    print "I'll ask you about the names of some famous composers"
    print "How about we start with your name??"

#call function

greeting_users()

"""Ask for users information"""

def get_user_name():
    """Returns user name"""
    name = raw_input("What's your name: ")
    return "Welcomeclear {}!".format(name)

# call function
player1 = get_user_name()
print player1

def  ask_user():
    """Ask and return if ready"""
    ready = raw_input("Are you ready? Y/N ")
        
    if ready == "Y"
        print "Awesome"
    if ready == "N"
        print "Too late you're in" 

    return ready


def names_of_composers():
    """Ask for the first name of composers"""
    copland_name = raw_input("Can you tell me the name of Copland? ")

    if copland_name == "Aaron"
        print "Yep, that's correc"

def input_with_timeout(x):    

def time_up():
    answer= None
    print 'time up...'

t = Timer(x,time_up) # x is amount of time in seconds
t.start()
try:
    answer = input("enter answer : ")
except Exception:
    print 'pass\n'
    answer = None

if answer != True:   # it means if variable have somthing 
    t.cancel()       # time_up will not execute(so, no skip)

input_with_timeout(5) # try this for five seconds










    