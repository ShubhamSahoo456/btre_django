from django.shortcuts import render, redirect
from .models import Contacts, Listings
# Create your views here.


def contact(request):
    if (request.method == "POST"):
        listing = request.POST['listingId']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contacts.objects.create(listing_id=listing,
                                          name=name, email=email, phone=phone, message=message)
        contact.save()
    return redirect('listings')
