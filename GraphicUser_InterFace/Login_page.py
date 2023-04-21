import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage

customtkinter.set_appearance_mode("dark")

class Login(customtkinter.CTk):
    width = 1950
    height = 1200

    def __init__(self):
        super().__init__()

        self.title("Login Page")
        self.geometry(f"{1700}x{580}")
        self.bg_image = customtkinter.CTkImage(Image.open("Image/Background_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Welcome To\nUnified-Travelling-and-Transport-System",
                                                  font=customtkinter.CTkFont(size=50, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.login_label_2 = customtkinter.CTkLabel(self.login_frame, text="Login Page",font=customtkinter.CTkFont(size=40, weight="bold"))
        self.login_label_2.grid(row=1, column=0, padx=30, pady=(50, 15))
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=500, placeholder_text="Username")
        self.username_entry.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="Password")
        self.password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=4, column=0, padx=30, pady=(15, 15))


    # def write_to_file(self):
        
    def login_event(self):

        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
                
        file = open("LocalDATA//password.txt", "w")
        file.write(entered_password)
        file.close()

        file = open("LocalDATA//username.txt", "w")
        file.write(entered_username)
        file.close()

        print("Login pressed - username:", entered_username, "password:",entered_password)
        self.destroy()            
        import StartPageGUI
        StartPageGUI.Main().mainloop()

if __name__ == "__main__":
    app9 = Login()
    app9.mainloop()