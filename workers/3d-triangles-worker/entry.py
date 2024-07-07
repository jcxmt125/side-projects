from js import Response, Headers
from create import generateHTML
import random

def on_fetch(request):
    numTrig = random.randrange(500, 1000)

    rad = random.randrange(100, 200)

    sineOff = random.random()*4

    html = generateHTML(numTrig, rad, 20, 3, 20, rad/50, sineOff)

    headers = Headers.new({"content-type": "text/html;charset=UTF-8"}.items())
    return Response.new(html, headers=headers)
