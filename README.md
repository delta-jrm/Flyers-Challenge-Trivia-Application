# Flyers-Challenge-Trivia-Application
Application to solve questions in an efficient manor. Made for the purpose of the Flyer Challenge at Lewis University.

# Instructions to Use
1. Assure you have a working version of Python 3. Use python --version to check.
2. The following libraries must be installed for Trivial Killer to work. Input the commands as follows.
    - pip install requests
    - pip install bs4
    - pip install pyfiglet
    - pip install wikipedia
3. Run "python trivialkiller.py"
4. The user will be prompted for key words. Take the example question: What is the largest planet in our Solar System?. The user would input "solar system"
5. The user must select the correct webpage option. Keep in mind arrays start at 0, so the correct index to put in owuld be 0 in the solar system case.
6. The user may start putting in more key words or answers. If the user puts in "largest planet", jupiter is revealed to be the correct answer.




# Version 1: 12/1/2019
- Added feature to input searches for keywords
- Added feature to select wikipedia page by inputting index of correct term
- Added feature to print out wikipedia page
- Added feature to search for answers individually (done through for loop)
- Added feature to see if page contains answer, and outprinting 300 characters before and after the answer.

- ToDo: Capitalize the answer when outprinted for easier reference
- ToDo: Assure all occurances of the answer are checked on the page
- ToDo: Iron out kinks in wikipedia search function, create escape or restart command if needed
- ToDo: Create answer object to have all answers run in a multithreaded fashion to speed up the process
- ToDo: Add menu to either select Wikipedia Scraping or Database Comparison until both are functional.
- ToDo: Once both are functional, run both processes in paralell to maximize chances of finding answer in quick fashion
- ToDo: Add functionality to crosscheck with the database of questions and answers
- ToDo: Start building GUI interface for inputting key terms and questions if possible.

- Goal: Implement more object oriented design strategy and investigate multithreading both methods of checking answers.
- Goal: Optimize search through with use of key terms, but make sure valid questions are not being ignored