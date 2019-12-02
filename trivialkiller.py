import sys
import requests
import bs4
import pyfiglet
import wikipedia

# Print Introductory Trivial Killer Banner.
ascii_banner = pyfiglet.figlet_format("Trivial Killer V1.0")
print(ascii_banner) 

# Keyword input for wikipedia scraping search.
question_search_term = input ("Please input key words from question :")
print(question_search_term)

# Creates and prints list of possible matching pages for the search term.
reference_pages = wikipedia.search(question_search_term)
print(reference_pages)

#Option selection and printing of the answer page.
input_search = input ("Type index number to select option: ")
answer_page = str(wikipedia.page(reference_pages[int(input_search)]).content)
print(answer_page)

# Answer checker, each answer is run through and compared against the page. If answer exists, print 300 char before and after the index to display information.
for x in range (1,5):
    potential_answer = input ("Answer " + str(x) + " :" )
    potential_answer = potential_answer.lower()
    answer_page = answer_page.lower()
    print(potential_answer in answer_page)
    if potential_answer in answer_page:
        answer_location = answer_page.find(potential_answer)
        print(answer_location)
        print(answer_page[answer_location - 300 : answer_location + 300])

# Segment of code for searching wikipedia without the use of wikipedia library. 
res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))
res.raise_for_status()
wiki = bs4.BeautifulSoup(res.text,"lxml")
elems = wiki.select('p')
for i in range(len(elems)):
    print(elems[i].getText())