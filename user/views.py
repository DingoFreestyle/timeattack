from django.shortcuts import render, redirect
from .models import UserModel

def Sign_up(request):
    if request.method == 'GET':
        return render(request, 'user/sighup.html')
    elif request.method == 'POST':
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)

        new_user = UserModel()
        new_user.email = email
        new_user.password = password
        new_user.save()

    return redirect('')



