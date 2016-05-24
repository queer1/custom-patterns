from django.http import HttpResponse
import dress_form
from bs4 import BeautifulSoup
import cgi
import cgitb; cgitb.enable()
from .models import measurements
from .forms import measurements_form
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
	measurements_QuerySet = measurements.objects.all()
	return render(request, 'pattern_generator/index.html', {'measurements_QuerySet': measurements_QuerySet})

	
def new_measurements(request):
	form = measurements_form()
	if request.method == "POST":
		form = measurements_form(request.POST)
		if form.is_valid():
			measurements = form.save(commit=False)
			measurements.save()
			return redirect('index')
	else:
		form = measurements_form()
	return render(request, 'pattern_generator/measurements_page.html', {'form': form});