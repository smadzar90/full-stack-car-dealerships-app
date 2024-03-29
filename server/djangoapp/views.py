from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .restapis import *
from django.contrib.auth import login, logout, authenticate


# Redirect to the home page
def redirect_to_home(request):
    return redirect("djangoapp:index")


# Render a home page
def home(request):
    context = { 'title': 'Home' }
    return render(request, 'djangoapp/index.html', context)


# Render a about page
def about(request):
     context = { 'title': 'About Us' }
     return render(request, 'djangoapp/about.html', context)


# Render a contact page
def contact(request):
    context = { 'title': 'Contact Us' }
    return render(request, 'djangoapp/contact_us.html', context)


# Authenticate and login user, then redirect to the home page
def login_request(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
    
    return redirect("djangoapp:index")


# Logour user
def logout_request(request):
    logout(request)
    return redirect("djangoapp:index")


# Register the user
# if user-name doesn't exist --> register and redirect to the home page
# if user-name exists --> render the page again
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


# Send get request to NodeJS app that will retreive dealerships
# Render a dealership page with list of dealership objects retrieved from the database
def get_dealerships(request):
    if request.method == "GET":
        url = "http://localhost:3000/dealerships/get"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        context = { 'title': 'Dealerships', 'dealerships': dealerships }
        # Return a list of dealer short name
        return render(request, 'djangoapp/dealerships.html', context)


# Send get request to Flask app that will retreive reviews by dealer_id
# Render a dealer details page with reviews retreived from the database
def get_dealer_details(request, dealer_id):
    url = "http://localhost:5001/api/get_reviews"
    url2 = "http://localhost:3000/dealerships/get?id=" + str(dealer_id)

    reviews = get_dealer_reviews_from_cf(url, dealer_id)
    dealership = get_dealers_from_cf(url2)

    if not dealership: 
        return HttpResponse("Dealer not found")
    
    sorted_reviews = sorted(reviews, key=lambda x: x.id)
    context = { 'title': dealership[0].short_name, 
                'dealership': dealership[0],
                'reviews': sorted_reviews
    }

    return render(request, 'djangoapp/dealer_details.html', context)


# GET --> Render a review page
# POST --> Send post request to the Flask app that will add review to the database
def add_review(request, dealer_id, dealer_name):

    if request.method == 'POST':
        review = dict()
        review['purchase_date'] = request.POST.get('purchase_date')
        review['dealership'] = dealer_id
        review['review'] = request.POST.get('review')
        review['name'] = request.user.get_full_name()
        purchase = request.POST.get('purchase')

        if purchase:
            review['purchase'] = True
            review['purchase_date'] = request.POST.get('purchase_date')
        else:
            review['purchase'] = False
        
        review['car_make'] = request.POST.get('car_make')
        review['car_model'] = request.POST.get('car_model')
        review['car_year'] = request.POST.get('car_year')

        url = "http://localhost:5001/api/post_review"
        response = requests.post(url, json=review)
        return redirect('djangoapp:dealer_details', dealer_id)
    
    url = "http://localhost:3000/dealerships/get?id=" + str(dealer_id)
    dealership = get_dealers_from_cf(url)

    if not dealership:
        return HttpResponse("Dealer not found")
    
    if not dealership[0].full_name == dealer_name:
         return HttpResponse("Dealer not found")

    context = {
        'title': 'Add Review',
        'id': dealer_id,
        'name': dealer_name
    }

    return render(request, 'djangoapp/add_review.html', context)

    



