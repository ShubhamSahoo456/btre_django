from django.shortcuts import render
from listings.models import Listings
from realtors.models import Realtor
from listings.choices import bedroom_choices,price_choices,state_choices

# Create your views here.
def index(request):
    listings = Listings.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        "listings":listings,
        "bedroom_choices":bedroom_choices,
        "price_choices":price_choices,
        "state_choices":state_choices
        }
    return render(request, 'pages/index.html',context)

def about(request):
    realtor_list = Realtor.objects.all()
    mvp = Realtor.objects.get(is_mvp=True)
    context = {
        "realtorsList":realtor_list,
        "mvp":mvp
    }
    return render(request, "pages/about.html",context)
