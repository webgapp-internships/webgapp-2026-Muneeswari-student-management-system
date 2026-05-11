from django.shortcuts import render

# Create your views here.

def index(request):
    muneesh="FULL stack devop"
    return render(request, "index.html",{'muneesh': muneesh})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def table(request):
    return render(request, 'table.html')

def testing(request):
    return render(request, 'testing.html')

def main(request):
    return render(request, 'main.html')
