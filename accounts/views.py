from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dastan:list')
    else:
        form=UserCreationForm()

    return render(request,'accountu/signup.html',{'form1':form})
def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('dastan:list')
    else:
        form=AuthenticationForm()
    return render(request,'accountu/login.html',{'form1':form})