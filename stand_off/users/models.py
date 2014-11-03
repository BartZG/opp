from django.db import models
from locations.models import Event

class User(models.Model):
	class Meta:
		verbose_name = "User"
		verbose_name_plural = "Users"

	def __str__(self):
		return self.first_name + " " + self.surname

	first_name = models.CharField("First name", max_length=20, blank=False)
	surname = models.CharField("Surname",max_length=20, blank=False)
	dob = models.DateField(blank=False)
	oib_user = models.CharField("User OIB",max_length=11, blank=False)
	email = models.EmailField("Email", blank=False)
	password = models.CharField("Password", max_length=50, blank=False)
	trade_name = models.CharField("Trade name", max_length=256, blank=True)
	oib_trade = models.CharField("Trade OIB", max_length=11, blank=True)
	phone = models.CharField("Phone", max_length=15, blank=True)
	mobile = models.CharField("Mobile", max_length=15, blank=True)
	cc_number = models.CharField("Credit Card Number", max_length=16, blank=True)
	grade_received_sum = models.IntegerField()
	grade_received_number = models.IntegerField()
	grade_given_sum = models.IntegerField()
	grade_given_number = models.IntegerField()

class Reservation(models.Model):
	class Meta:
		verbose_name = "Reservation"
		verbose_name_plural = "Reservations"

	def __str__(self):
		return str(self.user) + " " + str(self.event)

	date_start = models.DateTimeField("Reservation start")
	date_end = models.DateTimeField("Reservation end")
	small_stand_count = models.IntegerField(blank=True,null=True)
	medium_stand_count = models.IntegerField(blank=True, null=True)
	large_stand_count = models.IntegerField(blank=True, null=True)
	user = models.ForeignKey(User)
	event = models.ForeignKey(Event)

class Comment(models.Model):
	class Meta:
		verbose_name= "Comment"
		verbose_name_plural = "Comments"

	def __str__(self):
		return str(self.owner) + " " + str(self.target_user) + " " + str(self.target_event)

	text = models.TextField(blank=False, null=False)
	owner = models.ForeignKey(User, null=False, related_name='owner',)
	target_user = models.ForeignKey(User, related_name='target_user', null=True, blank=True)
	target_event = models.ForeignKey(Event, null=True, blank=True)
