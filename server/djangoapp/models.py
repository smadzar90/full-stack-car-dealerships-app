from django.db import models
from django.utils.timezone import now

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name + ', ' + self.description

class CarModel(models.Model):

    type_choices = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
    ]

    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(null=False)
    name = models.CharField(null=False, max_length=30)
    type = models.CharField(null=False, max_length=10, choices=type_choices)
    date = models.DateField(null=False)

    def __str__(self):
        return self.name + ', ' + self.type + ', ' + self.date

#Information about dealer
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

#Information about review posted
class DealerReview:

    def __init__(self, review):
        self.id = review.get('id')
        self.name = review.get('name')
        self.dealership = review.get('dealership')
        self.review = review.get('review')
        self.purchase = review.get('purchase')
        self.purchase_date = review.get('purchase_date')
        self.car_make = review.get('car_make')
        self.car_model = review.get('car_model')
        self.car_year = review.get('car_year')
        self.another = review.get('another')
        self.sentiment = review.get('sentiment')
    
    def __str__(self):
        return self.name + ', ' + self.review

