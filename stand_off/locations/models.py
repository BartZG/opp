from django.db import models

class Location(models.Model):
	class Meta:
		verbose_name = "Location"
		verbose_name_plural = "Locations"

	def __str__(self):
		return self.address

	address = models.CharField("Address", max_length=256, blank=False)
	capacity = models.IntegerField("Capacity", null=False)
	base_price = models.DecimalField("Base price", max_digits=10, decimal_places=2, null=False)
	spring_modifier = models.DecimalField("Spring modifier", max_digits=3, decimal_places=1, null=False)
	summer_modifier = models.DecimalField("Summer modifier", max_digits=3, decimal_places=1, null=False)
	autumn_modifier = models.DecimalField("Autumn modifier", max_digits=3, decimal_places=1, null=False)
	winter_modifier = models.DecimalField("Winter modifier", max_digits=3, decimal_places=1, null=False)

class Event(models.Model):
	class Meta:
		verbose_name = "Event"
		verbose_name_plural = "Events"

	def __str__(self):
		return self.name

	name = models.CharField("Event name", max_length=256, blank=False)
	category = models.CharField("Event type", max_length=256, blank=False)
	date_start = models.DateTimeField()
	date_end = models.DateTimeField()
	grade_received_sum = models.IntegerField()
	grade_received_count = models.IntegerField()
	location = models.ForeignKey(Location)
