from my_module.Functions import *

def test_my_name():
    assert callable(my_name)
    
def test_Quiz():
    assert question_prompts == [
    "What is my favorite color?\n(a) Blue\n(b) Red\n(c) Black",
    "What is my favorite sport?\n(a) Football \n(b) Basketball \n(c) Tennis",
    "Do I like to code? \n(a) Definitely \n(b) No \n(c) (-_-)ゞ゛Maybe?",
    "Will I get an A in my python class? \n(a) Yes \n(b) Of Course\n(c) Yessss but longer\n(d) All of them above",
    "True or False? Pineapple belongs on pizza. \n(a) HAHAHAHA \n(b) ◔̯◔ \n(c) I thought this was a T/F question?",
    "Do you have any questions for me? \n(a) yes\n(b) Pls no",
]
