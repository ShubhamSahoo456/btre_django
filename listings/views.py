from django.shortcuts import render, get_object_or_404
from .models import Listings
from django.core.paginator import Paginator
from .choices import bedroom_choices, price_choices, state_choices

# Create your views here.


def index(request):
    listings = Listings.objects.order_by(
        '-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, "listings/index.html", context)


def listing(request, listing_id):
    listings = get_object_or_404(Listings, pk=listing_id)
    context = {
        'listings': listings
    }
    return render(request, "listings/listing.html", context)


def search(request):
    listings = Listings.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET.get('city')
        if city:
            listings = listings.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET.get('state')
        if state:
            listings = listings.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET.get('price')
        if price:
            listings = listings.filter(price__lte=price)

    context = {
        "listings": listings,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
        "values": request.GET
    }
    return render(request, "listings/search.html", context)
