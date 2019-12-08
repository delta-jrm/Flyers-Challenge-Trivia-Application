import sys
import requests
import bs4
import pyfiglet
import wikipedia
import json

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

# Establish Database, not necessary unless multithreading implemented
json_file = open('trivia-questions.json', encoding="utf8")
trivia_question_bank = json.load(json_file)
json_file.close()

# Answer checker, each answer is run through and compared against the page. If answer exists, print 300 char before and after the index to display information.
def wiki_page_search(index_number, question, index, a, b, c, d):
    
    # Retrieves Wikipedia Page object through API
    answer_page = str(wikipedia.page(reference_pages[int(index_number)]).content).lower()

    # Creates Reference dictionary for possible answers.
    answer_list = []
    answer_list.insert(0, a.lower())
    answer_list.insert(1, b.lower())
    answer_list.insert(2, c.lower())
    answer_list.insert(3, d.lower())
    print(answer_list)

    # Checks if answer is contained in page, prints true or false.
    for answer in answer_list:
        print("Answer " + answer.upper() + " contained in page: " +  str(answer in answer_page))

        # If answer is in page, print 100 characters before and after answer occurance, capitalize answer.
        if answer in answer_page:
            answer_location = find_all(answer_page, answer)
            for location in answer_location:
                temp = answer_page[location - 100 : location + 100]
                part_1 = temp[0:99]
                part_2 = temp[100 : 100 + len(answer)]
                part_2 =  "--->" + part_2.upper() + "<---"
                part_3 = temp[len(answer) + 100 : 200]
                answer_print = "\n" + part_1 + " " + part_2 + part_3

                # If the question term is within 100 characters of the answer, print the full answer line.
                for q in question:
                    if q in answer_print:
                        print("\n" + answer_print + "\n")


# Database searching, not currently implemented with multithreading. 
def database_search(question_search_term_data, z, y , x, w):

    # Creates Reference dictionary for possible answers.
    answer_list = []
    answer_list.insert(0, z.lower())
    answer_list.insert(1, y.lower())
    answer_list.insert(2, x.lower())
    answer_list.insert(3, w.lower())
    
    trivia_question_bank_string = str(trivia_question_bank).lower()

    # Checks if answer is contained in page, prints true or false.
    if (str(question_search_term_data) in trivia_question_bank_string):
        question_location = find_all(trivia_question_bank_string, question_search_term_data.lower())
        print(question_location)
        for question in question_location:
            temp = trivia_question_bank_string[question - 100 : question + 100]
            part_a = temp[0:99]
            part_b = temp[100 : 100 + len(question_search_term_data)]
            part_b =  "--->" + part_b.upper() + "<---"
            part_c = temp[len(question_search_term_data) + 100 : 200]
            question_print = "\n" + part_a + " " + part_b + part_c

            # If the question term is within 100 characters of the answer, print the full answer line.
            for q in question_search_term_data:
                    if q in question_print:
                        print("\n" + question_print + "\n")

# Keyword input for wikipedia scraping search.
question_search_term = input ("Please input key words from question :")
question_search_term = question_search_term.split(", ")
print(question_search_term)

index_search_term = input ("Please input wiki page search term :")
print(index_search_term)

# Answer input for wikipedia scraping search.
answer_search_term_a = input ("Please input potential answer a :")
print(answer_search_term_a)
answer_search_term_b = input ("Please input potential answer b :")
print(answer_search_term_b)
answer_search_term_c = input ("Please input potential answer c :")
print(answer_search_term_c)
answer_search_term_d = input ("Please input potential answer d :")
print(answer_search_term_d)

# Implement this line to run the search in a multithreaded fashion if possible
# database_search(question_search_term, answer_search_term_a, answer_search_term_b, answer_search_term_c, answer_search_term_d)

 # Creates and prints list of possible matching pages for the search term.
reference_pages = wikipedia.search(index_search_term)
print(reference_pages)

#Option selection and printing of the answer page.
input_search = input ("Type index number to select option: ")

wiki_page_search(input_search, question_search_term, index_search_term, answer_search_term_a, answer_search_term_b, answer_search_term_c, answer_search_term_d)








# Segment of code for searching wikipedia without the use of wikipedia library. 
#res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))
#res.raise_for_status()
#wiki = bs4.BeautifulSoup(res.text,"lxml")
#elems = wiki.select('p')
#for i in range(len(elems)):
#    print(elems[i].getText())