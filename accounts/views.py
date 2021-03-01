from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def signup_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request,user)
           return redirect('dastan:list')
    else:
        form=UserCreationForm()

    return render(request,'accountu/signup.html',{'form1':form})
def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('dastan:list')
    else:
        form=AuthenticationForm()
    return render(request,'accountu/login.html',{'form1':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('dastan:list')