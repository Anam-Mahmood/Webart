# Create your views here.
from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Paintings

from django.views.generic.base import TemplateView
# from .forms import *
from django.shortcuts import render, redirect
# from django.contrib.auth.views import login, AuthenticationForm
# from django.contrib.auth import authenticate


from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import requests
from app.models import Paintings
from .forms import LoginForm, SignUpForm


class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        data = Paintings.objects.all()
        for d in data:
            print("Paintings:", d.name)
        args = {'user': request.user, 'data': data}
        return render(request, self.template_name, args)


class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        signup = int(kwargs['signup'])
        form = LoginForm()
        signupform = SignUpForm()
        args = {'form': form, 'signupform': signupform, 'signup': signup}
        return render(request, self.template_name, args)

    def post(self, request, **kwargs):
        if "email" in request.POST:
            signupform = SignUpForm(request.POST)
            if signupform.is_valid():
                print("signup form is valid")
                signupform.save()
                form = LoginForm()
                args = {'signupform': signupform, 'form': form, 'signup': 0}
                return render(request, self.template_name, args)
            else:
                form = LoginForm()
                args = {'signupform': signupform, 'form': form, 'error': signupform.errors.as_data(),
                        'signup': 1}
                print(signupform.errors.as_data())
                return render(request, self.template_name, args)

        else:
            form = LoginForm(request.POST, request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                return redirect('home')
            else:
                signupform = SignUpForm()
                args = {'signupform': signupform, 'form': form, 'error': form.errors.as_data(), 'signup': 0}
                print(form.errors.as_data())
                return render(request, self.template_name, args)



# def index(request):
#     return render(request, 'index.html')
#
#


def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


# def handler404(request):
#     return render(request, '404.html', status=404)
#
#
# def handler500(request):
#     return render(request, '500.html', status=500)


class Home(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        data = Paintings.objects.all()
        print("The paintings are:", data)
        args = {'user': request.user, 'data': data}
        return render(request, self.template_name, args)


class Inspo(TemplateView):
    template_name = 'inspo.html'

    def get(self, request):
        data = Paintings.objects.all()
        print("The paintings are:", data)
        args = {'user': request.user, 'data': data}
        return render(request, self.template_name, args)


class InspoLoginView(TemplateView):
    template_name = 'inspo-login.html'

    def get(self, request):
        data = Paintings.objects.all()
        print("The paintings are:", data)
        args = {'user': request.user, 'data': data}
        return render(request, self.template_name, args)

