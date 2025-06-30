# Importing Classes
from Api_calls import task_reminder as tr
import customtkinter as ctk

# Making the windows appearance
ctk.set_appearance_mode("black")

# Making the Gui class
class Brave_GUI(ctk.CTk):
    def __init__(self):
        # Inhereting the CTK class for gui
        super().__init__()
        self.title("Brave the AI Assistant") # Title
        self.geometry("800x600") # Size of the window

        # Label f
        self.Label = ctk.CTkLabel(self, width=600, height=30, text="Brave, you'r smart AI companian!!!", text_color="white", font=("Arial", 34))
        self.Label.pack(padx= 10,pady= (8, 10))
        # For displaying Chat
        self.chat_display = ctk.CTkTextbox(self, width=600, height=370, corner_radius= 16)
        self.chat_display.pack(padx=10, pady=(5, 2), expand= True) # positioning the chats
        self.chat_display.configure(state = "disable") # Making the windows not ediatble

        # Making the text box for user to get input
        self.input_chat = ctk.CTkTextbox(self, width=500, height= 5, corner_radius= 20, font=("Calibri", 15), border_spacing= 4, border_width=2)
        self.input_chat.insert("0.0", "Ask anything")
        self.input_chat.pack(padx=2, pady=(10, 5))
        
        # Making button for sending msg
        self.button = ctk.CTkButton(self, text="Submit", command=self.send_msg, corner_radius= 5, border_spacing= 3, fg_color="black",border_color="cyan", hover_color="white", text_color="dark gray")
        self.button.pack(pady=(0,10))

    # Sending the msg on the display
    def send_msg(self):
        msg = self.input_chat.get("1.0", ctk.END).strip()
        if msg:
            self.chat_display.configure(state= "normal")
            user_input = msg
            self.chat_display.insert(ctk.END, f"\n➡️User: {user_input}")
            self.input_chat.delete("1.0", ctk.END)
            self.chat_display.configure(state="disable")
            self.chat_display.see(ctk.END)

            self.chat_display.insert(ctk.END, f"\n➡️Brave: {tr.apiCalls(user_input)}")
            self.chat_display.configure(state="disable")
            self.chat_display.see(ctk.END)

if __name__ == "__main__":
    app = Brave_GUI()
    app.mainloop()