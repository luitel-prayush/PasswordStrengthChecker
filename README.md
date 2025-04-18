# 🔐 Password Strength Checker and Suggested Secure Password

This simple python and flask project is intended to take in a sample password from a user and check for the overall strength of the password, entropy in bits, and how many times this password has been part of a data breach

This project has also been enhanced to suggest a randomly generated secure password based on the length that the user specifies(min 12 char, max 64 chars)

## 📁 File Structure
<img width="205" alt="image" src="https://github.com/user-attachments/assets/1f4c8a51-ede6-4ed6-b826-a32890f6c0e8" />


## passwordChecker.py 
A standalone python file that takes in a sample password from the CLI and checks for the following conditions(length, if password contains a digit, contains an upper case character, contains a lower case character, and contains a symbol character.

Return: Strong password if all conditions are met | error message for each condition that is not met

To run the python file 
- Run the application through an IDE
- Bash command in terminal: python passwordchecker.py

## entropyCalculation.py
A standalone python file that takes in a sample password from the CLI and calculates the entropy of the password in bits.

Return: entropy of the password in bits

To run the python file
- Run the application through an IDE
- Bash command in terminal: python entropyCalculation.py

## knownBreaches.py
A standalone python file that takes in a sample password from the CLI and checks the haveIBeenPwned database for the number of times the password has been part of a data breach.

Return: Number of times the password has been part of a data breach

To run the python file
- Run the application through an IDE
- Bash command in terminal: python knownBreaches.py

## Main GUI application
A python and flask based application that creates an input form where the user can type in a password and check the strength of the password based on the logic from passwordChecker.py, entropy of the password based on the logic from entropyCalculation.py, and the number of times the password has been part of a data breach based on the logic from entropyCalculation.py. The GUI also offers a form where the user can input a length value(min 12, max 64) for a password and ask the applicaiton to suggest a strong password.

To run the GUI:
- Run app.py through an IDE
- Bash command in terminal: python app.py

### Strong password check:

<img width="477" alt="image" src="https://github.com/user-attachments/assets/f2f18e02-645b-4acc-a654-0bf1d73f86e8" />

### Weak password check:

<img width="477" alt="image" src="https://github.com/user-attachments/assets/46c2a07a-2019-4263-925b-ebbc34ae2f22" />

### Suggest strong password(length=16):

<img width="477" alt="image" src="https://github.com/user-attachments/assets/9c64c7a5-cda8-4041-98fe-36cfc88f5546" />




