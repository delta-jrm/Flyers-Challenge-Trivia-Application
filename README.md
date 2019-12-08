# Flyers-Challenge-Trivia-Application
Application to solve questions in an efficient manor. Made for the purpose of the Flyer Challenge at Lewis University.

# Instructions to Use
1. Assure you have a working version of Python 3. Use python --version to check.
2. The following libraries must be installed for Trivial Killer to work. Input the commands as follows.
    - pip install requests
    - pip install bs4
    - pip install pyfiglet
    - pip install wikipedia
    - pip install json
3. Run "python trivialkiller.py" for database search.
4. The user will be prompted for key words. 
    * Take the example question: What is the largest planet in our Solar System?. The user would input "largest planet"
5. The database will output the occurances of largest planet. If there is not an occurance, the program will give a message that it was not contained.
6. Run "python scraper.py" for wikipedia API search.
7. On run, it will first ask for key words from the question. Terms are seperated by commas if there are multiple search questions.
    * Take the example question: What was the band Oasis' debut album? The user would input "debut album". 
8. The user must input a search term for the wikipedia webpage option. 
    * The user may input "Oasis" for the example, as the debut album would be on the band's article page.
9. The user must then input the multiple choice options available for the answer.
    * For our example, the potential answers may be: Morning Glory, Definitely Maybe, Dark Side of the Moon, Madman Across the Water
10. The user must then seleect the wikipedia page by inputting the index of the proper webpage. Keep in mind arrays start at 0.
    * For our example, type 1 to select Oasis(band)
11. All of the answers are output with a true or false statement saying they are contained within the page. if the answer and the question term are within the 100 character range, it will outprint the answer to the console with 100 characters before and after




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

# Version 2: 12/5/2019
- Split up the wikipedia scraper and database search into two different programs to run.
- scraper.py is the wikipedia scraper, triviakiller.py is the database search
- Capitalized the answer when outprinted for easier reference.
- Cut down answer output to 100 characters before and after
- Created find_all method to find all occurances of answer on page.
- Added feature to input all answers at the same time
- Added feature to seperate question keywords and index search in scraper.py
- Check done for keyword in the answer string, now only outputs answer if within 100 chars before or after
- Goal Achieved: Optimize search through with use of key terms, but make sure valid questions are not being ignored 

- ToDo: Create functions to open functionality.
- ToDo: Implement answerchecking with database search.
- ToDo: Create answer object to have all answers run in a multithreaded fashion to speed up the process
- ToDo: Add menu to either select Wikipedia Scraping or Database Comparison until both are functional.
- ToDo: Start building GUI interface for inputting key terms and questions if possible.

- Goal: Implement more object oriented design strategy and investigate multithreading both methods of checking answers.
