from django.shortcuts import render,redirect, HttpResponse
from .forms import RegisterForm, StudentCreate
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Student


# Create your views here.
@login_required(login_url='login')
def home(request):
    upload = StudentCreate()
    if request.method == 'POST':
        upload = StudentCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('/')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/'}}">reload</a>""")
    else:
        return render(request, 'login_register/main.html', {'upload_form':upload})
    return render(request,'login_register/home.html')

@csrf_exempt
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form=RegisterForm()
        if request.method=='POST':
            form=RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'login_register/register.html',context)
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            username=request.POST.get('usernamep')
            password=request.POST.get('passwordp')
            userp=authenticate(request,username=username,password=password)
            if userp is not None:
                login(request,userp)
                return redirect('/')
            else:
                messages.info(request,'the username or password is incorrect')

        context={}
        return render(request,'login_register/login.html',context)
def logoutpage(request):
    logout(request)
    return redirect('/')





def upload(request):
    upload = StudentCreate()
    if request.method == 'POST':
        upload = StudentCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('/')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/'}}">reload</a>""")
    else:
        return render(request, 'login_register/main.html', {'upload_form':upload})

# def update_book(request, book_id):
#     book_id = int(book_id)
#     try:
#         book_sel = Book.objects.get(id = book_id)
#     except Book.DoesNotExist:
#         return redirect('index')
#     book_form = StudentCreate(request.POST or None, instance = book_sel)
#     if book_form.is_valid():
#        book_form.save()
#        return redirect('/')
#     return render(request, 'login_register/main.html', {'upload_form':book_form})

# def delete_book(request, book_id):
#     book_id = int(book_id)
#     try:
#         book_sel = Book.objects.get(id = book_id)
#     except Book.DoesNotExist:
#         return redirect('index')
#     book_sel.delete()
#     return redirect('index')
