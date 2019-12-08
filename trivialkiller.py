import sys
import requests
import bs4
import pyfiglet
import wikipedia
import json

# Print Introductory Trivial Killer Banner.
ascii_banner = pyfiglet.figlet_format("Trivial Killer V1.0")
print(ascii_banner) 

# Function to find all occurances of a substring in a string. Returns the index locaiton of said substring.
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

# Load Trivia Database
json_file = open('trivia-questions.json', encoding="utf8")
trivia_question_bank = json.load(json_file)
json_file.close()

# Select Search Method to use or debug, remove this when both run in paralell.
process_type = 2 #input ("Type 1 to select Wikipedia Scraping, Type 2 to select Database Search. Database is default search.")

# Run Wikipedia Scraper if 1: TRIVIAKILLER IS CONFIGURED TO RUN DATABASE SEARCH
if process_type == "1":
    # Keyword input for wikipedia scraping search.
    question_search_term = input ("Please input key words from question :")
    print(question_search_term)

    # Creates and prints list of possible matching pages for the search term.
    reference_pages = wikipedia.search(question_search_term)
    print(reference_pages)

    #Option selection and printing of the answer page.
    input_search = input ("Type index number to select option: ")
    answer_page = str(wikipedia.page(reference_pages[int(input_search)]).content)
    #print(answer_page)

    # Answer checker, each answer is run through and compared against the page. If answer exists, print 300 char before and after the index to display information.
    for x in range (1,5):

        # Take input of potential answer from user and out print answer location
        potential_answer = input ("Answer " + str(x) + " :" )
        potential_answer = potential_answer.lower()
        answer_page = answer_page.lower()
        print(potential_answer in answer_page)

        # If answer is in page, print 100 characters before and after answer occurance, capitalize answer.
        if potential_answer in answer_page:
            answer_location = find_all(answer_page, potential_answer)
            print(answer_location)
            for answer in answer_location:
                temp = answer_page[answer - 100 : answer + 100]
                part_1 = temp[0:99]
                part_2 = temp[100 : 100 + len(potential_answer)]
                part_2 =  "--->" + part_2.upper() + "<---"
                part_3 = temp[len(potential_answer) + 100 : 200]
                answer_print = "\n" + part_1 + " " + part_2 + part_3
                print(answer_print)


# Runs database search and looks for key words, capitalizes, and prints.
else:
    question_search_term = input ("Please input key words from question :")
    print(question_search_term)
    trivia_question_bank_string = str(trivia_question_bank).lower()
    if (question_search_term.lower() in trivia_question_bank_string):
        question_location = find_all(trivia_question_bank_string, question_search_term.lower())
        print(question_location)
        for question in question_location:
            temp = trivia_question_bank_string[question - 100 : question + 100]
            part_a = temp[0:99]
            part_b = temp[100 : 100 + len(question_search_term)]
            part_b =  "--->" + part_b.upper() + "<---"
            part_c = temp[len(question_search_term) + 100 : 200] 
            question_print = "\n" + part_a + " " + part_b + part_c
            print(question_print)
    else:
        print("There is no occurance of " + question_search_term + " within the database. Please try again or consult scraper.py")
                



# Segment of code for searching wikipedia without the use of wikipedia library. 
#res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))
#res.raise_for_status()
#wiki = bs4.BeautifulSoup(res.text,"lxml")
#elems = wiki.select('p')
#for i in range(len(elems)):
#    print(elems[i].getText())