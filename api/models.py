from django.db import models
import datetime


class City(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            default="Trabzon", blank=False)

    def __str__(self):
        return "{}".format(self.name)


class Panel(models.Model):
    icon = models.ImageField(upload_to='panel_icon', blank=True)
    title = models.CharField(max_length=100, default='')
    video = models.FileField(
        upload_to='videos', blank=False, verbose_name="Video (mp4)")
    weather_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='weather_city', to_field='name')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.icon, self.title, self.video, self.weather_city)


class SlidingText(models.Model):
    text = models.TextField(blank=False)
    panel = models.ForeignKey(
        Panel, on_delete=models.CASCADE, related_name='sliding_texts')

    def __str__(self):
        return "{}".format(self.text)

class BaseActivity(models.Model):
    title = models.CharField(max_length=50, default='')
    owner = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')

    class Meta:
        abstract=True

class Activity(BaseActivity):
    date = models.DateTimeField(blank=False)
    panel = models.ForeignKey(
        Panel, on_delete=models.CASCADE, related_name='activities')

    def __str__(super):
        return "{} - {} - {} - {}".format(super.title, super.owner, super.date, super.address,)

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

DAYS = (
        ('Pazartesi', 'Pazartesi'),
        ('Salı', 'Salı'),
        ('Çarşamba', 'Çarşamba'),
        ('Perşembe', 'Perşembe'),
        ('Cuma', 'Cuma'),
    )

class Class(BaseActivity):
    day = models.CharField(max_length=10, choices=DAYS, default='Pazartesi')
    start_time = models.TimeField(blank=False, default=datetime.time(10, 00))
    end_time = models.TimeField(blank=False, default=datetime.time(12, 00))
    panel = models.ForeignKey(
        Panel, on_delete=models.CASCADE, related_name='classes')
        

    def __str__(super):
        return "{} - {} - {} - {} - {}".format(super.title, super.owner, super.day, super.start_time, super.end_time, super.address,)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        
Class._meta.get_field('title').verbose_name = 'Name'
Class._meta.get_field('owner').verbose_name = 'Professor'
Class._meta.get_field('address').verbose_name = 'Classroom'
