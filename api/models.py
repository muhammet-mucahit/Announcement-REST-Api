from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "{}".format(self.name)


class Panel(models.Model):
    icon = models.ImageField(upload_to='panel_icon')
    title = models.CharField(max_length=100, default='')
    video = models.FileField(upload_to='videos', blank=True)
    weather_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='weather_city', to_field='name')

    def __str__(self):
        return "{} - {} - {} - {}".format(self.icon, self.title, self.video, self.weather_city)


class SlidingText(models.Model):
    text = models.CharField(max_length=500, default='')
    panel = models.ForeignKey(
        Panel, on_delete=models.CASCADE, related_name='sliding_texts')

    def __str__(self):
        return "{}".format(self.text)


class Activity(models.Model):
    title = models.CharField(max_length=50, default='')
    owner = models.CharField(max_length=100, default='')
    date = models.DateTimeField(blank=False)
    address = models.CharField(max_length=100, default='')
    panel = models.ForeignKey(
        Panel, on_delete=models.CASCADE, related_name='activities')

    def __str__(self):
        return "{} - {} - {} - {}".format(self.title, self.owner, self.date, self.address,)
