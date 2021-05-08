#QUESTION QUIZ
from question import question
qprompt=["Which anime has half-demon character as the protagonists?\n[a]Black Butler\n[b]Inuyasha\n[c]Black Clover\n\n",
          "Which animated movie rose at the top in the year 2018?\n[a]Wolf children\n[b]5 cm per second\n[c]Your Name\n\n",
          "Which anime has potrayed end game?\n[a]Digimon X-wars\n[b]Digimon Frontier\n[c]Digimon data squad\n\n"]
questions=[question(qprompt[0],"b"),
           question(qprompt[1],"c"),
           question(qprompt[2],"a")]

def runtest(questions):
    score=0
    #similar to item in list
    for question in questions:
        ans=input(question.prompt)
        if ans==question.answer:
            score +=1
    print("Your score is",str(score ),"/",str(len(questions)))

runtest(questions)