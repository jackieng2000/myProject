from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
from datetime import datetime
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello World</h1>")
    
    # ! get all data from listing database 
    listings = Listing.objects.all().values()


    #for listing in listings:
    #   d = clisting['list_date']
    #   diff_day = (datetime.now().date() - d.date())
    #    clisting['day_ago'] = diff_day.days

    # ! pass database records into listings context
    context ={'listings':listings, }

    # !Calculate the start and end of the last day
    
    return render(request, 'listings/listings.html', context)

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
