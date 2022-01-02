import random 
import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Rock, Paper, Scissors Game")
root.configure(background="#FFFF99")

user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""
winner = ""
tie = ""

def tie_or_not(tie):
	user = choice_to_number(user_choice)
	comp = choice_to_number(comp_choice)
	if(user==comp):
		tie = "Yes"
	else:
		tie = "No"
	return tie


def who_is_winner(winner):
	user = choice_to_number(user_choice)
	comp = choice_to_number(comp_choice)
	if(user==comp):
		winner = "---Nobody---"
	elif ((user-comp) %3 == 1):
		winner = "User"
	else:
		winner = "Computer"
	return winner

def choice_to_number(choice):
	rps = {'Rock':0, 'Paper':1, 'Scissor':2 }
	return rps[choice]

def number_to_choice(number):
	rps = {0:'Rock', 1:'Paper', 2:'Scissor'}
	return rps[number]

def random_comp_choice():
	return random.choice(['Rock', 'Paper', 'Scissor'])

def result(user_choice, comp_choice):
	global user_score
	global comp_score
	global winner
	global tie
	user = choice_to_number(user_choice)
	comp = choice_to_number(comp_choice)
	winner = who_is_winner(winner)
	tie = tie_or_not(tie)
	if(user==comp):
		user_score = 0
		comp_score = 0
	elif ((user-comp) %3 == 1):
		winner = "User"
		user_score += 1
	else:
		winner = "Computer"
		comp_score += 1
	text_area = tk.Text(master=root, height=15, width=50, bg="#FFFF99")
	text_area.grid(column=0, row=4)
	answer = "Your choice: {uc} \nComputer choice: {cc} \nYour score: {us} \nComputer score: {cs} \nWinner: {w} \nTie: {t}".format(uc=user_choice, cc=comp_choice, us=user_score, cs=comp_score, w=winner, t=tie)

	text_area.insert(tk.END, answer)
	text_area.configure(state='disabled')



def rock():
	global user_choice
	global comp_choice
	user_choice = 'Rock'
	comp_choice = random_comp_choice()
	result(user_choice, comp_choice)
def paper():
	global user_choice
	global comp_choice
	user_choice = 'Paper'
	comp_choice = random_comp_choice()
	result(user_choice, comp_choice)
def scissor():
	global user_choice
	global comp_choice
	user_choice = 'Scissor'
	comp_choice = random_comp_choice()
	result(user_choice, comp_choice)
button1 = tk.Button(text="       Rock       ", bg="skyblue", width=56, command=rock)
button1.grid(column=0, row=1)
button2 = tk.Button(text="       Paper       ", bg="pink", width=56, command=paper)
button2.grid(column=0, row=2)
button3 = tk.Button(text="       Scissor       ", bg="lightgreen", width=56, command=scissor)
button3.grid(column=0, row=3)

root.mainloop()
