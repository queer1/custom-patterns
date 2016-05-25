from django.http import HttpResponse
import dress_form
from bs4 import BeautifulSoup
import cgi
import cgitb; cgitb.enable()
from .models import measurements
from .forms import measurements_form
from .models import pattern
from .forms import pattern_form
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
	#measurements_QuerySet = measurements.objects.all(){'measurements_QuerySet': measurements_QuerySet}, 
	pattern_QuerySet = pattern.objects.all()
	return render(request, 'pattern_generator/index.html', {'pattern_QuerySet': pattern_QuerySet})

	
def new_measurements(request):
	form = pattern_form()
	if request.method == "POST":
		form = pattern_form(request.POST)
		if form.is_valid():
			pattern = form.save(commit=False)
			pattern.save()
			return redirect('index')
	else:
		form = pattern_form()
	return render(request, 'pattern_generator/measurements_page.html', {'form': form});