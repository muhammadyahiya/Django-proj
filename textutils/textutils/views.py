# I have created this file - Yahya
from django.http import HttpResponse




def about(request):
    return HttpResponse('''<h1>Hello</h1> <a href = "https://www.youtube.com" > Django code with yahya</a>''')


# def index(request):
#     return HttpResponse("<h1>Hello, world this is my first django app</h1>")

def index(request):
    #return HttpResponse("about , this is my first django app")
    return HttpResponse("about , this is my first django app")

# def doc_web(request):
#     file = open("textutils/doc_web.txt", "r")
#     return HttpResponse(file.read())


