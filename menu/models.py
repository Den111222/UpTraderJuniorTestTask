from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    url = models.CharField(max_length=255, null=True, blank=True)
    named_url = models.CharField(max_length=255, null=True, blank=True)
    menu_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title