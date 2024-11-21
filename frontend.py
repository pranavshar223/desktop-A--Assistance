import tkinter as tk
from tkinter import Scrollbar
from gemini import GeminiAi
from main import mainai
from welcome import print_csv_text

def send_message():
    # Get the user's input from the entry field
    user_input = user_entry.get().strip()
    if user_input:
        # Enable the text widget temporarily
        chat_display.config(state=tk.NORMAL)

        # Display the user's message
        chat_display.insert(tk.END, f"You: {user_input}\n")
        
        # Call the chatbot backend here to get the response
        bot_response = get_bot_response(user_input)  # Placeholder function
        
        # Display the bot's response
        chat_display.insert(tk.END, f"NOVA: {bot_response}\n")
        
        # Disable the text widget to prevent editing
        chat_display.config(state=tk.DISABLED)

        # Scroll to the end of the chat
        chat_display.yview(tk.END)

        # Clear the input field
        user_entry.delete(0, tk.END)

# Placeholder chatbot backend function
def get_bot_response(user_input):
   
    text=GeminiAi(user_input)
    
    

    return text
    
    # return "This is a placeholder response."

# Initialize the main window
root = tk.Tk()
root.title("Chatbot")
root.geometry("800x900")

# Chat display area
chat_frame = tk.Frame(root, bg="white")
chat_frame.pack(pady=10)

chat_display = tk.Text(chat_frame, height=40, width=60, wrap=tk.WORD, state=tk.DISABLED, bg="white")
chat_display.pack(side=tk.LEFT)

scrollbar = Scrollbar(chat_frame, command=chat_display.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_display.config(yscrollcommand=scrollbar.set)

# Entry box for user input
user_entry = tk.Entry(root, width=50, font=("Arial", 14), bg="white")
user_entry.pack(pady=10)

# Button frame
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

# Buttons
send_button = tk.Button(button_frame, text="Send", command=send_message, width=10, bg="lightblue")
send_button.grid(row=0, column=0, padx=5)

speak_button = tk.Button(button_frame, text="Speak", width=10, bg="lightgreen")  # Add functionality later
speak_button.grid(row=0, column=1, padx=5)

mic_button = tk.Button(button_frame, text="Mic", width=10, bg="lightyellow")  # Add functionality later
mic_button.grid(row=0, column=2, padx=5)

# Run the app
root.mainloop()
