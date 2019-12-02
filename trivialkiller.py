import sys
import requests
import bs4
import pyfiglet
import wikipedia

ascii_banner = pyfiglet.figlet_format("Trivial Killer V1.0")
print(ascii_banner)

question_search_term = input ("Please input key words from question :")
print(question_search_term)
reference_pages = wikipedia.search(question_search_term)
print(reference_pages)
input_search = input ("Type index number to select option: ")
answer_page = str(wikipedia.page(reference_pages[int(input_search)]).content)
print(answer_page)
for x in range (1,5):
    potential_answer = input ("Answer " + str(x) + " :" )
    potential_answer = potential_answer.lower()
    answer_page = answer_page.lower()
    print(potential_answer in answer_page)
    if potential_answer in answer_page:
        answer_location = answer_page.find(potential_answer)
        print(answer_location)
        print(answer_page[answer_location - 300 : answer_location + 300])
    
    


    


res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))

res.raise_for_status()
wiki = bs4.BeautifulSoup(res.text,"lxml")
elems = wiki.select('p')
for i in range(len(elems)):
    print(elems[i].getText())