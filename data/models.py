from django.db import models

# Create your models here.

class DATA(models.Model):
    date_of_drow = models.CharField(max_length=400)
    ball1 = models.IntegerField()
    ball2 = models.IntegerField()
    ball3 = models.IntegerField()
    ball4 = models.IntegerField()
    ball5 = models.IntegerField()
    lucky1 = models.IntegerField()
    lucky2 = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.date_of_drow, self.ball1, self.ball2, self.ball3, self.ball4, self.ball5, self.lucky1, self.lucky2}'