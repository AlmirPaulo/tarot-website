from browser import document as doc
from browser import ajax, html, console
from javascript import JSON 
import random


#variables
card_img = doc['card']
title = doc['title']
questions = doc['questions']

#Ajax call
def get_data(req):
    if req.status == 200 or req.status == 0:
        res = JSON.parse(req.response)
        pick = random.randint(0, 21)
        console.log(pick, res)
        title.innerText = res['cards'][pick]['title']
        card_img.attrs['src'] = res['cards'][pick]['picture']
        for q in res['cards'][pick]['questions']:
           questions <= html.LI(q)  
    else:
        print('error code 500')

req = ajax.Ajax()
req.bind('complete', get_data)
req.open('GET', 'https://tarotapi.almirpaulo.repl.co/', False)
req.send()


