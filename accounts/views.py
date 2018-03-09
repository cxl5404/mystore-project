from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #TODO Need to route to homepage
    # and dont' forget logout :)
    return render(request, 'accounts/logout.html')
