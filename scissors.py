import tkinter as tk
from PIL import Image, ImageTk
import random, time, threading, cv2

#  here we can give resize img and img path
rock = cv2.resize(cv2.imread(r"C:\Users\sc276\Downloads\Gemini_Generated_Image_mbvggmbvggmbvggm.png"), (250,250))
paper = cv2.resize(cv2.imread(r"C:\Users\sc276\Downloads\Gemini_Generated_Image_mbvggmbvggmbvggm (1).png"), (250,250))
scissors = cv2.resize(cv2.imread(r"C:\Users\sc276\Downloads\Gemini_Generated_Image_8bd2i98bd2i98bd2.png"), (250,250))

choices = {"rock": rock, "paper": paper, "scissors": scissors}

#  logic of winning the game
def winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player, computer) in [
        ("rock","scissors"),
        ("scissors","paper"),
        ("paper","rock")
    ]:
        return "You Win!"
    else:
        return "Computer Wins!"

#  Game will start in 3 second
def start_game(player_choice):
    lbl_result.config(text="Starting game in 3..", fg="black")
    root.update()
    for i in [2,1]:
        time.sleep(1)
        lbl_result.config(text=f"Starting game in {i}...", fg="black")
        root.update()

    time.sleep(1)
    lbl_result.config(text="Deciding...", fg="black")
    root.update()

    computer_choice = random.choice(list(choices.keys()))

    # below code line is used Show both images
    comp_img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(choices[computer_choice], cv2.COLOR_BGR2RGB)))
    lbl_comp.config(image=comp_img)
    lbl_comp.image = comp_img

    player_img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(choices[player_choice], cv2.COLOR_BGR2RGB)))
    lbl_player.config(image=player_img)
    lbl_player.image = player_img

    #  Show results
    lbl_comp_move.config(text=f"Computer: {computer_choice.upper()}")
    lbl_player_move.config(text=f"You: {player_choice.upper()}")
    lbl_result.config(text=winner(player_choice, computer_choice), fg="blue")

#  Run game in a separate thread so GUI doesn’t freeze
def play(player_choice):
    threading.Thread(target=start_game, args=(player_choice,)).start()

#  GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.attributes('-fullscreen', True)  #  Fullscreen mode

# Press ESC to exit fullscreen
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

#  Layout
frame = tk.Frame(root, bg="white")
frame.pack(expand=True, fill="both")

lbl_comp = tk.Label(frame, bg="white")
lbl_comp.place(x=200, y=100)

lbl_player = tk.Label(frame, bg="white")
lbl_player.place(x=900, y=100)

tk.Label(frame, text="Computer", font=("Arial",18,"bold"), bg="white").place(x=270, y=380)
lbl_comp_move = tk.Label(frame, text="", font=("Arial",14), bg="white")
lbl_comp_move.place(x=270, y=410)

tk.Label(frame, text="You", font=("Arial",18,"bold"), bg="white").place(x=1000, y=380)
lbl_player_move = tk.Label(frame, text="", font=("Arial",14), bg="white")
lbl_player_move.place(x=1000, y=410)

lbl_result = tk.Label(frame, text="", font=("Arial",24,"bold"), bg="white")
lbl_result.place(x=600, y=500)

#  Buttons
btn_rock = tk.Button(frame, text="Rock", font=("Arial",14,"bold"), width=10, command=lambda: play("rock"))
btn_paper = tk.Button(frame, text=" Paper", font=("Arial",14,"bold"), width=10, command=lambda: play("paper"))
btn_scissors = tk.Button(frame, text=" Scissors", font=("Arial",14,"bold"), width=10, command=lambda: play("scissors"))

btn_rock.place(x=450, y=650)
btn_paper.place(x=650, y=650)
btn_scissors.place(x=850, y=650)

root.mainloop()
