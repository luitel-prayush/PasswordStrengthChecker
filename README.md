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

