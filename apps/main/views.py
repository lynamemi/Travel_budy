from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Trip
from ..loginreg.models import User
from django.contrib import messages
# from .models import

# Create your views here.
def index(request):
	return render(request, 'loginreg/loginreg.html')
def travels(request):
	context = {
		'trips':Trip.objects.all(),
		'users':User.objects.all(),
		'trip_joiners':Trip.objects.filter(trip_joiner=request.session['user'])
		}
	return render(request, 'main/travels.html', context)
def destination(request, id):
	trip = Trip.objects.get(id=id)
	context = {
		'trip':Trip.objects.get(id=id),
		'trip_joiners': trip.trip_joiner.exclude(id=request.session['user']),
	}
	return render(request, 'main/destination.html', context)

def add_trip(request):
	created_trip = Trip.userManager.create_trip(request.POST)
	if created_trip[0] == False:
		for error in created_trip[1]:
			messages.add_message(request, messages.INFO, error)
		return redirect('/travels/add')
	if created_trip[0] == True:
		trip = Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], start_date=request.POST['start_date'], end_date=request.POST['end_date'], trip_creator=User.objects.get(id=request.session['user']))
	return redirect('/travels')
def add(request):
	return render(request, 'main/add.html')

def join_trip(request):
	trip = Trip.objects.get(id=request.POST['trip_id'])
	trip.trip_joiner.add(User.objects.get(id=request.session['user']))
	trip.save()
	return redirect('/travels')