from browser import document as doc
from browser import ajax, html, console
from javascript import JSON 
import random

box = doc['box']

#Ajax call
def get_data(req):
    if req.status == 200 or req.status == 0:
        box.text = ''
        res = JSON.parse(req.response)
        cards = []
        for n in range(0,22):
           cards.append(res['cards'][n]['picture'])
           
        for i in cards:
            box  <= html.IMG(src=i, id="card", Class="m-2")

    else:
        print('error code 500')

def loading(req):
    box <= html.H3('loading...')

req = ajax.Ajax()
req.bind('complete', get_data)
req.bind('loading', loading)
req.open('GET', 'https://tarotapi.almirpaulo.repl.co/', False)
req.send()

