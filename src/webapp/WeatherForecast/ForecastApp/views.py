from django.shortcuts import render
from django.http import HttpResponse
from .models import Forecast

# Create your views here.
def index(request):
	if request.method == 'POST':
		city = request.POST.get('city', '')
		forecasts = Forecast.objects.order_by('pub_date').filter(place=city)
		context = {'forecast' : forecasts}
		return render(request, "index.html", context)
	else:
		forecasts = Forecast.objects.order_by('pub_date').filter(place="London")
		context = {'forecast' : forecasts}
		return render(request, "index.html", context)

def visual(request):
	return render(request, "contact.html")