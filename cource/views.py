from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

from .models import Cource

# Create your views here.

def home(request):
    data = Cource.objects.all()
    paginator = Paginator(data,5)
    page = request.GET.get('page')
    paged_data = paginator.get_page(page)

    context = {'course':paged_data}
    return render(request, 'home.html',context)

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request,'register.html')

def register_data(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username,email,password)
            user.save()
            return redirect('cource:index')
        except:
            return render(request,'register.html') 
    else:
        return render(request,'register.html')
    
def login_data(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('cource:home')
        else:
            return render(request,'index.html')
    else:
        return render(request,'index.html')

def logout_user(request):
    logout(request)
    return render(request,'index.html') 
  


def add_cource(request):
    return render(request,'addcource.html')

def cource_data(request):
    if request.method == 'POST':
        
        title =       request.POST['title']
        description = request.POST['description']
        instructor =  request.POST['instructor']
        startdate =   request.POST['startdate']
        enddate =     request.POST['enddate']
        capacity =    request.POST['capacity']
        try:
            cource = Cource.objects.create(
                title = title,
                description = description,
                instructor = instructor,
                start_date = startdate,
                end_date = enddate,
                capacity = capacity
            )

            cource.save()
            return redirect('cource:home')
        except:
            return render(request,'addcource.html')
    else:
        return render(request,'addcource.html')

def search(request):
    if request.method == 'POST':
        title = request.POST['title_search']

        try:
            course = Cource.objects.filter(title__icontains = title)
        except:
            return redirect('cource:home')
        context = {'course':course}

        return render(request,'home.html',context)
    else:
        return redirect('cource:home')
    

def update_cource(request):
    data = Cource.objects.all()

    context = {'course':data}
    return render(request,'updatecource.html',context)

def update_value(request,id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        instructor = request.POST['instructor']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        capacity = request.POST['capacity']

        try:
            data = Cource.objects.get(id=id)

            data.title = title
            data.description = description
            data.instructor = instructor
            data.start_date = startdate
            data.end_date = enddate
            data.capacity = capacity
            data.save(update_fields=['title','description','instructor','start_date','end_date','capacity'])
            return redirect('cource:update_cource')

        except:
            return redirect('cource:update_cource')
    else:
        return redirect('cource:update_cource')

def delete_cource(request,id):
    try:
        cource = Cource.objects.get(id=id)
        print(cource)
        cource.delete()
        return redirect('cource:update_cource')
    except:
        return redirect('cource:update_cource')
        
