from django.db import models


class Log(models.Model):
    name = models.CharField(max_length=100)

    choices = (
        ("High", "High"), 
        ("Medium", "Medium"),
        ("Low", "Low"),
    )

    productivity =  models.CharField(max_length=50, choices=choices)
    certainty = models.CharField(max_length=50, choices=choices)
    health =  models.CharField(max_length=50, choices=choices)
    task = models.TextField()
    date = models.DateTimeField()
    

    def __str__(self):
        return f'{self.name} - {self.task} - {self.date}'
