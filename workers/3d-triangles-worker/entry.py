from js import Response, Headers
from create import generateHTML

def on_fetch(request):
    html = generateHTML(500, 100, 20, 3, 20, 2)

    headers = Headers.new({"content-type": "text/html;charset=UTF-8"}.items())
    return Response.new(html, headers=headers)
