from django.db import models

class Tracker(models.Model):
    STATUS = (
        ('Y', 'yes'),
        ('N', 'no')
    )
    id = models.PositiveIntegerField(primary_key = True)
    date = models.DateField(unique = True)
    daily_status = models.CharField(max_length = 1, choices = STATUS)

    def __str__(self):
        return '{}, {}'.format(self.date, self.daily_status)

