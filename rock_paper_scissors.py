import random
import time
sing = ["✌️", "👊" , "🖐️"]

def intro():
    global best_of
    print("hello wanna play Rock Paper Scissors? \n let's play")
    best_of = int(input("do you want to play best of 3 or best of 5 or another? \n type with number: "))
    if best_of % 2 == 0:
        print("please type odd number")
        return intro()
    else:
        pass

i = 0

def win_draw_lose():
    global result, i
    if player == "✌️":
        if bot_answer == "✌️":
            result = "draw"
        elif bot_answer == "👊" :
            result = "lose"
        else:
            result = "win"
            i = i+1
    elif player == "👊":
        if bot_answer == "✌️":
            result = "win"
            i = i+1
        elif bot_answer == "👊" :
            result = "draw"
        else:
            result = "lose"
    else:
        if bot_answer == "✌️":
            result = "lose"
        elif bot_answer == "👊" :
            result = "win"
            i = i+1
        else:
            result = "draw"

def play():
    global player
    player_choice = int(input("What do you want to choose? ✌️ = 1 / 👊 = 2 / 🖐️ = 3: "))
    if player_choice in [1, 2, 3]:
        choices = {1: "✌️", 2: "👊", 3: "🖐️"}
        player = choices[player_choice]
    else:
        print("you cheat nuh ah")
        return
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("bot answer : ", bot_answer)
    print("you answer : ", player)
    win_draw_lose()
    print("oh you ", result)
    time.sleep(1)
#------------------------------------------------------------------------------------------------------------------------------------------------
#out put
intro()
bestof_int = int(best_of)
bot_score = 0
for o in range(bestof_int):
    bot_answer = random.choice(sing)
    play()
    if result == "lose":
        bot_score = bot_score+1
    else:
        pass
    print(f"Score: You {i}, Bot {bot_score}")


    if i > bestof_int // 2:
        print("Congratulations! You won the series.")
        exit()
if i < bestof_int // 2:
    print("Sorry, the bot won the series.")
elif i == bot_score:
    print("oh you draw this series.")
else:
    pass
