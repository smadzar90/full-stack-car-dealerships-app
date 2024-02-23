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

