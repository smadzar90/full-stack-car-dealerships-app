from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .restapis import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

logger = logging.getLogger(__name__)

def home(request):
    context = { 'title': 'Home' }
    return render(request, 'djangoapp/index.html', context)


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
    
    return redirect("djangoapp:index")


def logout_request(request):
    logout(request)
    return redirect("djangoapp:index")


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
            return redirect('djangoapp:index')
            
        context['user_exists'] = 'User already exist. Try again!'
        
    return render(request, 'djangoapp/registration.html', context)


def get_dealerships(request):
    if request.method == "GET":
        url = "http://localhost:3000/dealerships/get"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        context = { 'title': 'Dealerships', 'dealerships': dealerships }
        # Return a list of dealer short name
        return render(request, 'djangoapp/dealerships.html', context)


def get_dealer_details(request, dealer_id):
    url = "http://localhost:5001/api/get_reviews"
    url2 = "http://localhost:3000/dealerships/get?id=" + str(dealer_id)

    reviews = get_dealer_reviews_from_cf(url, dealer_id)
    dealership = get_dealers_from_cf(url2)

    if not dealership: 
        return HttpResponse("Dealer not found")

    context = { 'title': dealership[0].short_name, 
                'dealership': dealership[0],
                'reviews': reviews
    }
    return render(request, 'djangoapp/dealer_details.html', context)


def add_review(request, dealer_id):
    review = dict()
    review['purchase_date'] = datetime.utcnow().isoformat()
    review['dealership'] = dealer_id
    review['review'] = request.POST.get('review')
    review['name'] = request.POST.get('name')
    review['purchase'] = request.POST.get('purchase')
    review['car_make'] = request.POST.get('car_make')
    review['car_model'] = request.POST.get('car_model')
    review['car_year'] = request.POST.get('car_year')

    url = "http://localhost:5001/api/post_review"

    response = post_request(url, review)

    



