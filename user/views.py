from contextlib import redirect_stderr
import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .forms import CreateUserForm

# Create your views here.
def register(request):
    print(request.POST)
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        
        messages.success(request, f"User created successfully. Please log in :")
        return redirect('dashboard-index')
    else:
        form=CreateUserForm()

    # form=CreateUserForm
    context = {
        'form': form
    }
    return render(request, 'user/register.html',context)