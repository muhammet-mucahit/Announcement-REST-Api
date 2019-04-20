from django.db import models

# Create your models here.

class Panel(models.Model):
    icon = models.ImageField(upload_to='panel_icon', blank=True)
    title = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos', blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.icon, self.title, self.video, self.created,)


class SlidingText(models.Model):
    text = models.CharField(max_length=500, default='')
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE, related_name='sliding_texts')

    def __str__(self):
        return "{}".format(self.text)

# class SlidingText(models.Model):
#     text = models.CharField(max_length=500, default='')
#     panel = models.ForeignKey(Panel, on_delete=models.CASCADE, related_name='sliding_texts')

#     def __str__(self):
#         return "{}".format(self.text)