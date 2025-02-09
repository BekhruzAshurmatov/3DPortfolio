from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    smtp_server = models.CharField(max_length=255)
    smtp_email = models.CharField(max_length=255)
    smtp_password = models.CharField(max_length=255)
    smtp_port = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/')
    aboutus = models.TextField(max_length=255)
    contact = models.TextField(max_length=255)

    def __str__(self):
        return self.title