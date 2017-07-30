"""Greeting the User"""

def greeting_users():
   
    print "Welcome to our music journey about composers!!"
    print "..."
    print "..."


def two_players_game():
    """Asks user how many players"""

    print "How many players are in ? "
    players = raw_input()
    return players 


"""Ask for users information"""
def get_user_name():
    """Returns user name"""
    name = raw_input("What's your name? > ")
    return name

# Explain Game

def  ask_user(user_name):
    """Ask user if they're excited"""

    print "I'll ask you about the names of some famous composers, I hope you know about music"
    print "..."
    print "Good Luck"
    print "Are you excited? Type Y or N\n"
    ready = raw_input("> ")
    ready = ready.upper()

    if ready == "Y":
        print "Yayyy. It's so cool {}!\n".format(user_name)

    if ready == "N":
        print "Seriously?, you have to play {}!".format(user_name)
        print "..."
        print "You wont regret it"

        


q1 = {"question": 'What was the name of Mozart ?',
     "choices": ['A: Juan', 'B: Ludwig van', 'C: Wolfgang Amadeus'],
     "answer": "C",
     "details": "Mozart is so famous you can even find his head on the top of chocolates, At five years old, little Wolfgang started to compose his own piece, and he could play the piano and violin! "}

q2 = {"question": 'What was the name of Adams ?',
     "choices": ['A: John', 'B: Giussepe', 'C: Carlos'],
     "answer": "A",
     "details": "John Adams is the odd one, why ? Because he still alive! he is an american composer!."}

q3 = {"question": 'What was the name of Beethoven ?',
    "choices": ['A: Max', 'B:Luvwig van', 'C: Dmitri'],
    "answer": "B",
    "details": "The big thing Beethoven did was to have new ideas, he was quite grumpy but good at writing music"}

q4 = {"question": 'What was the name of Bernstein ?',
    "choices": ['A: Dave', 'B:Antonio', 'C: Leonard'],
    "answer": "C",
    "details": "Was an American composer, conductor, author, music lecturer, and pianist. "}

q5 = {"question": 'What was the name of Vivaldi ?',
    "choices": ['A: Antonio', 'B:Carlos', 'C: Dave'],
    "answer": "A",
    "details": "Was an Italian Baroque composer, virtuoso violinist, teacher and cleric. "}

q6 = {"question": 'What was the name of Bach ?',
    "choices": ['A: Kara', 'B:Johann Sebastian', 'C: Igor'],
    "answer": "B",
    "details": "He was a German composer and he played the organ, Bach had 20 children and he still had time to write magnificent music! "}


all_questions = [q1, q2, q3, q4, q5, q6]


def quiz_user():
    wrong = 0  
    right = 0

    for item in all_questions:
        print item["question"]
        print item["choices"]

        get_answer = raw_input("Enter your answer: ").upper() 
        if get_answer == item["answer"]:
            print "\nYay!  you guessed correctly!\n"
            right += 1
            print item['details'] + "\n"
        else:
            print '\nThat is not the answer I had in mind!\n'
            wrong += 1
        print('So far, you answered correctly to {} questions and incorrectly to {}. Good luck!\n'.format(right, wrong))
    # return right


if __name__ == '__main__':
    #call function
    # 1 player game
    greeting_users()

    count = 0

    player1 = get_user_name()

    ask_user(player1)
    # call function
    quiz_user()





# for a 2 player Game
# if __name__ == '__main__':
#     #call function


#     player_scores = {}
#     greeting_users()
#     player_count = int(two_players_game())

#     count = 0

#     while count < player_count: 
#         player1 = get_user_name()

#         ask_user(player1)
#         # call function
#         player_scores[player1] = quiz_user()
#         count = count + 1

#     print "player_scores is {}".format(player_scores)