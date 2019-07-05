from django.db import models

# Create your models here.
class Forecast(models.Model):
	place = models.CharField(max_length=200)
	pub_date = models.DateField()
	temperature = models.BigIntegerField()
	wind = models.CharField(max_length=200)
	humidity = models.DecimalField(max_digits=5, decimal_places=2)
	wind_speed = models.BigIntegerField(default=0)
	week_day = models.CharField(max_length=200, default="Monday")

	# STATES
	rain = models.BooleanField(default=False)
	thunder = models.BooleanField(default=False)
	clodly = models.BooleanField(default=False)
	more_sunny = models.BooleanField(default=False)
	snow = models.BooleanField(default=False)

	def __str__(self):
		return self.week_day + " " + self.place