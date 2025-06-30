import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")  # Optional: dark mode
ctk.set_default_color_theme("blue")

class ChatApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTk Chat Box")
        self.geometry("400x500")

        # Chat display (read-only)
        self.chat_display = ctk.CTkTextbox(self, width=380, height=350, corner_radius=13)
        self.chat_display.pack(padx=10, pady=(10, 5))
        self.chat_display.configure(state="disabled")  # Make it read-only

        # Message input
        self.msg_input = tk.Text(self, height=3, wrap="word", font=("Arial", 15))
        self.msg_input.pack(padx=10, pady=5, fill="x")

        # Send button
        self.send_btn = ctk.CTkButton(self, text="Send", command=self.send_msg)
        self.send_btn.pack(padx= (12, 20),pady=(12, 20))

    def send_msg(self):
        msg = self.msg_input.get("1.0", ctk.END).strip()
        if msg:
            self.chat_display.configure(state="normal")
            self.chat_display.insert(ctk.END, f"You: {msg}\n")
            self.chat_display.configure(state="disabled")
            self.chat_display.see("end")
            self.msg_input.delete("1.0", "end")

app = ChatApp()
app.mainloop()
