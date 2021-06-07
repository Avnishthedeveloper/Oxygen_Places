from django.db import models

# Create your models here.

# Address, Business Name, Person Name (optional), Contact, Verified Status, TimeStamp

class Place(models.Model):
	Address = models.CharField(max_length = 100, blank= True)
	BusinessName = models.CharField(max_length = 100, blank= True)
	Person = models.CharField(max_length = 100, blank= True)
	Contact = models.CharField(max_length = 100, blank= True)
	VerifiedStatus = models.BooleanField(default = True)
	TimeStamp = models.DateTimeField(auto_now_add = True)

	class meta:
		ordering = ['TimeStamp']