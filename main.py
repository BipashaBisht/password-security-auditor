
import tkinter as tk
from tkinter import messagebox
import re
import secrets
import string


# Function to check password strength
def analyze_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password!")
        return

    score = 0
    feedback = []

    # Password length
    if len(password) >= 8:
        score += 1
        feedback.append("✓ At least 8 characters")
    else:
        feedback.append("✗ At least 8 characters required")

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Add uppercase letters (A-Z)")

    # Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Add lowercase letters (a-z)")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Add numbers (0-9)")

    # Special characters
    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Add special characters (@, #, $)")

    # Check uniqueness
    if len(set(password)) >= len(password) * 0.5:
        score += 1
        feedback.append("✓ Good character variety")
    else:
        feedback.append("✗ Too many repeated characters")

    # Determine strength
    if score <= 2:
        strength = "WEAK"
        color = "#e74c3c"
    elif score <= 4:
        strength = "MEDIUM"
        color = "#f39c12"
    else:
        strength = "STRONG"
        color = "#27ae60"

    # Display result
    strength_label.config(text=f"Password Strength: {strength}",
                          fg=color)

    progress_label.config(text=f"Score: {score}/6")

    # Display checklist
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)

    for item in feedback:
        result_text.insert(tk.END, item + "\n")

    result_text.config(state="disabled")


# Generate a stronger password suggestion
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%&*"
    password = "".join(secrets.choice(characters) for _ in range(14))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    analyze_password()


# Show or hide password
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show")


# Clear everything
def clear_fields():
    password_entry.delete(0, tk.END)
    strength_label.config(text="Password Strength: Not Checked",
                          fg="#333333")
    progress_label.config(text="Score: 0/6")

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.config(state="disabled")


# Main window
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("480x570")
root.resizable(False, False)
root.configure(bg="#f4f6f9")


# Heading
heading = tk.Label(
    root,
    text="Password Strength Analyzer",
    font=("Arial", 19, "bold"),
    bg="#f4f6f9",
    fg="#1f3c88"
)
heading.pack(pady=20)


# Description
description = tk.Label(
    root,
    text="Check how secure your password is",
    font=("Arial", 11),
    bg="#f4f6f9"
)
description.pack(pady=5)


# Password input
password_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25,
    show="*",
    bd=2,
    relief="groove"
)
password_entry.pack(pady=15)


# Show/Hide button
show_button = tk.Button(
    root,
    text="Show",
    command=toggle_password,
    bg="#dddddd"
)
show_button.pack()


# Analyze button
analyze_button = tk.Button(
    root,
    text="Analyze Password",
    command=analyze_password,
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    width=22,
    pady=8
)
analyze_button.pack(pady=15)


# Strength result
strength_label = tk.Label(
    root,
    text="Password Strength: Not Checked",
    font=("Arial", 13, "bold"),
    bg="#f4f6f9"
)
strength_label.pack(pady=5)


# Score
progress_label = tk.Label(
    root,
    text="Score: 0/6",
    font=("Arial", 11),
    bg="#f4f6f9"
)
progress_label.pack(pady=5)


# Checklist heading
check_heading = tk.Label(
    root,
    text="Security Checklist",
    font=("Arial", 12, "bold"),
    bg="#f4f6f9",
    fg="#1f3c88"
)
check_heading.pack(pady=8)


# Results box
result_text = tk.Text(
    root,
    height=7,
    width=43,
    font=("Arial", 10),
    bd=1,
    relief="solid"
)
result_text.pack(pady=5)
result_text.config(state="disabled")


# Generate password button
generate_button = tk.Button(
    root,
    text="Generate Strong Password",
    command=generate_password,
    bg="#16a085",
    fg="white",
    font=("Arial", 10, "bold"),
    width=25,
    pady=7
)
generate_button.pack(pady=8)


# Clear button
clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    bg="#e5e7eb",
    font=("Arial", 10),
    width=15
)
clear_button.pack(pady=5)


# Footer
footer = tk.Label(
    root,
    text="Password Security Awareness Project",
    font=("Arial", 9),
    bg="#f4f6f9",
    fg="gray"
)
footer.pack(pady=10)


# Run application
root.mainloop()
