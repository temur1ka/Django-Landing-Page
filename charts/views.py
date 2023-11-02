from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import ReactJs, Django, Salary
from .forms import Form, UserForm, regauth
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib import messages


class ClubView(LoginRequiredMixin,TemplateView ):
    template_name = 'charts/home.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = ReactJs.objects.all()
        context['dj'] = Django.objects.all()
        context['sl'] = Salary.objects.all()
        context["forms"] = Form() # add a form instance to context here

        return context


def get_contact(request):
    forms = Form
    if request.method == 'POST':
        forms = Form(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
    
        return render(request, 'charts/home.html',{'forms':forms} )

def registerPage(request):
    form = regauth()
    

    if request.method == 'POST':
        form = regauth(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Profile has successfuly Created.")

            return redirect('login')
        
    context = {'form': form}
    return render(request, 'charts/register.html', context)
    
def loginPage(request):

    if request.method == 'POST':
       password = request.POST.get('password') 
       username = request.POST.get('username')

       user = authenticate(request, username=username, password=password)

       if user is not None:
           login(request, user)
           return redirect('index')
       
       else:        
           messages.info(request, "Username or Password is Incorrect")
    context = {}

    return render(request, 'charts/login.html', context)


def logOutPage(request):
    logout(request)
    return redirect('login')