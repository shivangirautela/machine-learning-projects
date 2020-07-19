import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
#print(res.text) 
#print(res) # response status 

soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')
#print(soup)
#print(soup.body)
#print(soup.body.contents)
#print(soup.find_all('div'))
#print(soup.find_all('a'))
#print(soup.title)
#print(soup.a)
#print(soup.find('a'))
#print(soup.select(".score"))
#print(soup.select("#votelinks"))
links = soup.select(".storylink")
subtext = soup.select(".subtext")

links2 = soup2.select(".storylink")
subtext2 = soup2.select(".subtext")

mega_links =links+links2
mega_subtext = subtext +subtext2
#print(votes[0])
#print(votes[0].get('score_23534974'))
#print(votes[0].get('id'))

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k: k['votes'] , reverse =True)

def create_custom_hn(links , subtext):
    hn =[]
    for idx , item in enumerate(links): #enumerate is used to enumerate over links lists not over subtext
        title = item.getText()
        href = links[idx].get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points =int(vote[0].getText().replace(' points',''))
            if points> 99:#print(points)
                hn.append({'title' : title , 'link' : href ,'votes': points })
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links,mega_subtext))
