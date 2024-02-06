from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

logger = logging.getLogger(__name__)

def about(request):
     context = { 'title': 'About Us' }
     return render(request, 'djangoapp/about.html', context)

def contact(request):
    context = { 'title': 'Contact Us' }
    return render(request, 'djangoapp/contact_us.html', context)

def login_request(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
    
    return redirect("djangoapp:about")

def logout_request(request):
    logout(request)
    return redirect("djangoapp:about")

def registration_request(request):

    context = { 'title': 'Registration' }

    if request.method == 'POST':

        user_name = request.POST.get('username')
        first_name = request.POST.get('firstname')  
        last_name = request.POST.get('lastname')
        pwd = request.POST.get('password')

        user_exist = False

        try:
            User.objects.get(username=user_name)
            user_exist = True
        except:
            pass
        
        if not user_exist:

            user = User.objects.create_user(username=user_name, password=pwd, first_name=first_name, last_name=last_name)
            login(request, user)
            return redirect('djangoapp:about')
            
        context['user_exists'] = 'User already exist. Try again!'
        
    return render(request, 'djangoapp/registration.html', context)



# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = { 'title': 'This is the title' }
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

