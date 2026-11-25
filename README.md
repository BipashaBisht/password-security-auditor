# Password Strength Analyzer

## 1. Introduction

The Password Strength Analyzer is a Python-based application that checks the strength and security of user-entered passwords. It helps users understand whether their passwords are weak, medium, or strong.

The main purpose of this project is to promote password security awareness and encourage users to create strong and secure passwords.

## 2. Objectives

- To evaluate the strength of user-entered passwords.
- To check password length and complexity.
- To identify uppercase letters, lowercase letters, numbers, and special characters.
- To check character repetition and uniqueness.
- To suggest stronger password alternatives.
- To understand basic password security concepts.

## 3. Technologies Used

The following technologies and tools are used in this project:

- **Programming Language:** Python
- **IDE:** Visual Studio Code (VS Code)
- **GUI Library:** Tkinter
- **Regular Expression Module:** re
- **Password Generation Module:** secrets
- **String Module:** string

## 4. Features

1. **Password Length Check:** Checks whether the password contains at least 8 characters.
2. **Complexity Check:** Identifies uppercase letters, lowercase letters, numbers, and special characters.
3. **Uniqueness Check:** Checks whether the password contains sufficient character variety.
4. **Strength Evaluation:** Classifies passwords as Weak, Medium, or Strong.
5. **Password Generator:** Generates a random and stronger password suggestion.
6. **Show/Hide Password:** Allows users to view or hide their entered password.
7. **Clear Option:** Clears the entered password and previous results.

## 5. Working of the Project

The application works in the following steps:

1. The user enters a password in the input field.
2. The user clicks the Analyze Password button.
3. The program checks the password using different conditions.
4. It calculates a score based on the six security checks.
5. The application displays the password strength.
6. It provides a checklist showing which security requirements are satisfied and which need improvement.
7. The user can also generate a stronger password using the password generator.

## 6. Password Strength Criteria

The project evaluates passwords using six criteria:

- Minimum 8 characters.
- At least one uppercase letter.
- At least one lowercase letter.
- At least one number.
- At least one special character.
- Sufficient character uniqueness.

**Strength Classification:**

- 0–2 points: Weak
- 3–4 points: Medium
- 5–6 points: Strong

## 7. Installation and Execution

Follow these steps to run the project:

1. Install Python on your computer.
2. Install Visual Studio Code.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

```bash
python main.py
```

6. The Password Strength Analyzer application will open.

## 8. Requirements

- Python 3.x
- Visual Studio Code
- Tkinter (usually included with standard Python installations)

No additional external Python packages are required.

## 9. Future Enhancements

The project can be improved by adding:

- Database integration to maintain password history securely.
- Prevention of password reuse.
- Advanced password security analysis.
- Password strength measurement based on entropy.
- A more attractive and user-friendly interface.

## 10. Conclusion

The Password Strength Analyzer is a useful Python-based project that helps users understand the importance of creating strong passwords. It evaluates passwords based on different security criteria and provides suggestions for improvement.

Through this project, we learn about Python programming, GUI development, regular expressions, secure random password generation, and basic cybersecurity concepts.

---

**Project Name:** Password Strength Analyzer

**Programming Language:** Python

**IDE:** Visual Studio Code

**Project Type:** Python GUI Application
