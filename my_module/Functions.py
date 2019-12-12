#Function to determine my name
def my_name(name):
    """ Determines if user input is correct name
    
    Parameters
    ----------
    name: String
        user input of name
    
    Returns
    -------
    A message telling if name is correct or not
    """ 
    
    intro = True
    
    while intro is True:
        
        if name == 'Charles':
            print('You are correct!')
            intro = False
        
        else:
            print('(︶︹︺), It is Charles!')
            intro = False
    
    while intro is False:
        print("Surprise! Pop Quiz!\n""It is time for a quiz that you probably won't ace!(Or maybe you are a good guesser)")
        break

name = input('What is my name? : ')

my_name(name)


#Contains Questions and Answers for Popquiz
class Quiz:
    
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is my favorite color?\n(a) Blue\n(b) Red\n(c) Black",
    "What is my favorite sport?\n(a) Football \n(b) Basketball \n(c) Tennis",
    "Do I like to code? \n(a) Definitely \n(b) No \n(c) (-_-)ゞ゛Maybe?",
    "Will I get an A in my python class? \n(a) Yes \n(b) Of Course\n(c) Yessss but longer\n(d) All of them above",
    "True or False? Pineapple belongs on pizza. \n(a) HAHAHAHA \n(b) ◔̯◔ \n(c) I thought this was a T/F question?",
    "Do you have any questions for me? \n(a) yes\n(b) Pls no",
]

answers = [
    Quiz(question_prompts[0], "a"),
    Quiz(question_prompts[1], "b"),
    Quiz(question_prompts[2], "c"),
    Quiz(question_prompts[3], "d"),
    Quiz(question_prompts[4], "c"),
    Quiz(question_prompts[5], "b"),
]

#Grades the quiz
def run_quiz(answers):
    """Takes your answers and records how many you got right
    
    Parameters
    ----------
    answers: String
            user input of answer
            
    Returns
    -------
    Your total score
    """
    score = 0
    
    for item in answers:
        answer = input(item.prompt)
        
        if answer == item.answer:
               score += 1
    print("you got", score, "out of", len(answers), "!")
    
    if score< 6:
        
        print("Answer Key: a b c d c b")
           
run_quiz(answers)


