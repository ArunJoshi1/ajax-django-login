from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
# Create your views here.
from  django.contrib.auth.forms import UserCreationForm
def register(request):
    if request.POST:
        form=UserCreationForm(request.POST)
        print('post')
        if form.is_valid():
            print('Save')
            form.save()
            return redirect('https://google.com')
    form=UserCreationForm()
    return render(request,'index.html',{'form':form})
def process(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    status=True
    try:
        User.objects.get(username=username)
    except Exception:
        status=False
    if status:
        return JsonResponse("User Already Exsist",safe=False)
    else:
        user=User.objects.create_user(username=username)
        user.set_password(password)
        user.save()
        return JsonResponse("success",safe=False)