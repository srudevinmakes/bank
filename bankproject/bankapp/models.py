from django.db import models



# Create your models here.
class branches(models.Model):
    name=models.CharField(max_length=100)
    address = models.TextField()




    def __str__(self):
        # return self.name
        return self.name