from django.db import models

# Create your models here.

class Panel(models.Model):
    icon = models.CharField(max_length=1000, default='')
    title = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "{} - {} - {}".format(self.icon, self.title, self.created)


class SlidingText(models.Model):
    text = models.CharField(max_length=500, default='')
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE, related_name='sliding_texts')

    def __str__(self):
        return "{}".format(self.text)