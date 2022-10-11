from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Images(models.Model):
    image = models.ImageField(upload_to='Images')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title