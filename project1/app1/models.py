from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    marks = models.FloatField()

    def __str__(self) -> str:
        return f'{self.id},{self.name},{self.roll},{self.marks}'
 