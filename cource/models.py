from django.db import models

# Create your models here.


class Cource(models.Model):
    title = models.CharField(max_length=50,null=True)
    description = models.TextField()
    instructor = models.CharField(max_length=100,null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.title


