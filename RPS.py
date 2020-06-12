import random

def compare(u, c):
    if u==c:
        return "It's a tie!"
    elif u=='r':
        if c=='p':
            counter['c']+=1
            return "Computer Wins!"
        else:
            counter['u']+=1
            return ("%s Wins!"%user)
    elif u=='p':
        if c=='r':
            counter['u']+=1
            return ("%s Wins!"%user)
        else:
            counter['c']+=1
            return "Computer Wins!"
    elif u=='s':
        if c=='r':
            counter['c']+=1
            return "Computer Wins!"
        else:
            counter['u']+=1
            return ("%s Wins!"%user)
    else:
        return "Invalid!"

user = input("Enter your name : ")
counter = {'c':0, 'u':0}
print("Computer =", counter['c'], end=" ")
print(user +" =", counter['u'])

while True:
    user_ans = input("%s, choose among the Rock(r), Paper(p) or Scissor(s) : " %user)
    if user_ans == 'q':
        break
    choices = ['r', 'p', 's']
    index = random.randint(0,100)%3
    comp_ans = choices[index]
    print("Computer =",comp_ans)
    res = compare(user_ans, comp_ans)
    print(res)
    print("Computer =", counter['c'], end=" ")
    print(user +" =", counter['u'])
