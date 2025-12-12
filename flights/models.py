from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    airline = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.flight_number} - {self.airline}"


class Booking(models.Model):
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.flight.airline}"

