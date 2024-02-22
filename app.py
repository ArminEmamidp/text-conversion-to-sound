from tkinter import *
import pyttsx3

# Fonts
font_1 = ('Arial', 20)
font_2 = ('Boulder', 15, 'bold')

# Initializing the pyttsx3 and create a object
sound = pyttsx3.init()
sound.setProperty('rate', 110)

class App(Tk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.title('Text Conversion To Sound')
        self.config(bg='lightgreen')
        self.geometry('600x550')

        header = Label(self, text='Welcome to the text-conversion-to-sound app', fg='lime', bg='darkblue', font=font_1, width=100, borderwidth=12)
        header.pack(side='top', fill='x')

        # Frame of button and text-box
        app_frame = Frame(self, bg='#eee')
        app_frame.pack(side='top', fill='x', padx=22, pady=40, ipadx=10, ipady=10)
        
        # Button of Conversion 
        conversion_btn = Button(app_frame, text='Play Sound', fg='black', bg='lightpink', font=font_2, width=20, borderwidth=4, command=self.saySound)
        conversion_btn.pack(side='bottom', padx=10, pady=10, ipady=8, fill='x')

        # user input box
        self.user_text = Text(app_frame, bg='lightgray', fg='black', font=font_1)
        self.user_text.pack(side='top', fill='x', padx=10, pady=10)

    def saySound(self):
        sound.say(self.user_text.get(1.0, END))
        sound.runAndWait()


if __name__ == "__main__":
    app = App()
    app.mainloop()
