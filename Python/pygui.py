import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    proposal = proposal_text.get("1.0", "end")

    # Validate if all fields are filled
    if name == '' or proposal.strip() == '':
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        # Here you can write code to handle the submission, such as displaying a message box
        messagebox.showinfo("Proposal Submitted", f"Dear {name},\n\n{proposal}\n\nYour proposal has been submitted successfully!")

# Create main application window
root = tk.Tk()
root.title("Heart in Love Proposal")

# Create labels and entry fields
name_label = tk.Label(root, text="Recipient's Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

proposal_label = tk.Label(root, text="Your Proposal:")
proposal_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
proposal_text = tk.Text(root, height=5, width=30)
proposal_text.grid(row=1, column=1, padx=10, pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit Proposal", command=submit)
submit_button.grid(row=2, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
