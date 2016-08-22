from __future__ import unicode_literals

from django.db import models
from datetime import datetime, date
# from ..loginreg.models import User
# Create your models here.

class UserManager(models.Manager):
	def create_trip(self, data):
		errors=[]
		if not len(data['destination']) > 1 or not len(data['description']) > 1 or data['start_date'] == "" or data['end_date'] == "":
			errors.append("No empty entries")
		if data['start_date'] == "" or data['end_date'] == "" or datetime.strptime(data['start_date'], '%Y-%m-%d') > datetime.strptime(data['end_date'], '%Y-%m-%d'):
			errors.append("'Travel Date To' should not be before the 'Travel Date From'")
		if data['start_date'] == "" or data['end_date'] == "" or datetime.strptime(data['start_date'], '%Y-%m-%d') < datetime.now() or datetime.strptime(data['end_date'], '%Y-%m-%d') < datetime.now():
			errors.append("Travel dates should be future-dated")
		if not errors:
			return(True, data)
		return(False, errors)

class Trip(models.Model):
	destination=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	start_date = models.DateField()
	end_date = models.DateField()
	user = models.ManyToManyField('loginreg.User', related_name="userstrips")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()
