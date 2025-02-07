import random
item_list = ["ROCK", "PAPER", "SCISSOR"]

user_choice = input("Enter your move :ROCK, PAPER, SCISSOR : ")
comp_choice = random.choice(item_list)

print(f"User choice : {user_choice}, Computer choice : {comp_choice} ")

if user_choice == comp_choice:
    print("Both chooses same : Match Tie")

elif user_choice == "ROCK":
    if comp_choice == "PAPER":
        print("Paper covers Rock : Computer Win")
    else:
        print("Rock smashes Scissor = You Win")

elif user_choice == "PAPER":
    if comp_choice == "ROCK":
        print("Paper covers Rock : You Win")
    else:
        print("Scissor cuts Paper : Computer Win")

elif user_choice == "SCISSOR":
    if comp_choice == "PAPER":
        print("Scissor cuts Paper : You Win")
    else:
        print("Rock smashes Scissor : Computer Win")