from django.db import models

# Create your models here.

class SlidingText(models.Model):
	text = models.CharField(max_length=255, null=False)

class Main(models.Model):
	# slide = models.CharField(max_length=255, null=False)
	# icon = models.CharField(max_length=255, null=False)
	title = models.CharField(max_length=255, null=False)
	sliding = models.ForeignKey(SlidingText, on_delete=models.CASCADE)
	date = models.DateField(null=False)
	time = models.TimeField(null=False)

	def __str__(self):
		return "{} - {}".format(self.title, self.sliding, self.date, self.time)