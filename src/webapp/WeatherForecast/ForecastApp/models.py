from django.db import models

# Create your models here.
class Forecast(models.Model):
	place = models.CharField(max_length=200)
	pub_date = models.DateTimeField()
	temperature = models.BigIntegerField()
	wind = models.CharField(max_length=200)
	humidity = models.DecimalField(max_digits=5, decimal_places=2)
	wind_speed = models.BigIntegerField()

	def __str__(self):
		return self.place