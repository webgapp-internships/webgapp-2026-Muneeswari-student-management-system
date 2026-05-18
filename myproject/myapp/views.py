from django.shortcuts import render,redirect
from .models import Forms
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

def service(request):
    return render(request, 'service.html')

def sample(request):
    return render(request, 'sample.html')

def new(request):
    return render(request, 'new.html')

def newabout(request):
    return render(request, 'newabout.html')

def newservices(request):
    return render(request, 'newservices.html')

def form(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        dob=request.POST.get('dob')
        regno = request.POST.get('regno')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        skills = request.POST.get('skills')
        year = request.POST.get('year')
        Forms.objects.create(name = name,age = age,dob = dob,regno = regno,password = password,  email = email,phone =phone,gender =gender, skills= skills, year =year)
        
    return render(request, 'form.html')
    
def form_result(request):
    result = Forms.objects.all()
    return render(request,'form_result.html',{"result":result})

def form_edit(request,id):
    edit = Forms.objects.filter(id=id)

    if request.method == "POST":

        name = request.POST.get('name')
        regno = request.POST.get('regno')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Forms.objects.filter(id=id).update(
            name=name,
            regno=regno,
            age=age,
            dob=dob,
            email=email,
            phone=phone
        )

    return render(request,'form_edit.html',{"edit":edit})

def form_delete(request,id):
    delete = Forms.objects.filter(id=id)
    delete.delete()
    return redirect("form_result")

def web(request):
    return render(request, 'web.html')

def collections(request):
    return render(request,'collections.html')


def gallery(request):
    return render(request,'gallery.html')

def contactin(request):
    return render(request,'contactin.html')
