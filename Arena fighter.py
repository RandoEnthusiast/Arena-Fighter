from tkinter import Entry, ttk, Text, Event, Tk, Label, Button
import tkinter as tk
import pickle
from time import sleep, time

#i'm sorry

Game_Window = tk.Tk()
Game_Window.geometry("900x500")
Game_Window.title("Crap v.0.0.0")

Main_Label_Text = tk.StringVar()
Main_Label_Text.set("Select Action")
Main_Label = tk.Label(Game_Window, textvariable = Main_Label_Text, font = (16), anchor = tk.CENTER)
Main_Label.pack(pady = 20)
Main_Label2_text = tk.StringVar()
Main_Label2 = tk.Label(Game_Window, textvariable = Main_Label2_text, font = ("Arial", 14))
Main_Label2.pack(side = "top")

Button_Proceed = tk.Button()
Button_Proceed2 = tk.Button()

Player_Name_StringVar = tk.StringVar()
Player_Name = Player_Name_StringVar.get()

def Menu_2():
    Main_Label_Text.set("This should be readable")
    Main_Label2_text.set("")
    Button_Proceed.pack_forget()

def New_Game():
    

    Main_Label_Text.set("Name yourself")

    Button_New_Game.pack_forget()
    Button_Load_Game.pack_forget()

    Player_Name_Entry = tk.Entry(Game_Window, text = "Your name here", font = ("Arial", 14), textvariable = Player_Name_StringVar)
    Player_Name_Entry.pack(side = "top", padx = 15)

    def Done_Naming():

        def Menu_2():
            Main_Label_Text.set("This should be readable")
            Main_Label2_text.set("")
            Button_Proceed.pack_forget()
            Button_Proceed2.pack_forget()
            Button_Load_Game.pack()

        Player_Name = Player_Name_StringVar.get()

        with open("Savefile.pkl", "wb") as file:
            pickle.dump({"PlayerName" : Player_Name}, file)

            Main_Label_Text.set("Saved!")

            Button_Proceed.pack_forget()
            Player_Name_Entry.pack_forget()

            Button_Proceed2 = tk.Button(Game_Window, text = "Proceed", command = Menu_2)
            Button_Proceed2.pack()

    Button_Proceed = tk.Button(Game_Window, text = "Proceed", command = Done_Naming)
    Button_Proceed.pack(side = "top")

def Load_Game():
    with open("Savefile.pkl", "rb") as file:
        Saved_data = pickle.load(file)
        PlayerName_loaded = Saved_data["PlayerName"]
        Main_Label_Text.set("Loaded!")
        Main_Label2_text.set("Welcome back " + PlayerName_loaded)

        Button_Load_Game.pack_forget()
        Button_New_Game.pack_forget()

    def Menu_2():
        Main_Label_Text.set("This should be readable")
        Main_Label2_text.set("")
        Button_Proceed.pack_forget()

    Button_Proceed = tk.Button(Game_Window, text = "Continue", command = Menu_2)
    Button_Proceed.pack()

Button_New_Game = tk.Button(Game_Window, text = "New Game", command = New_Game)
Button_New_Game.pack(side = "top", pady = 30)

Button_Load_Game = tk.Button(Game_Window, text = "Load Game", command = Load_Game)
Button_Load_Game.pack(side = "top")

Game_Window.mainloop()