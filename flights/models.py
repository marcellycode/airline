from django.db import models
#from flights import views 

# Modelo Airport
class Airport(models.Model):  
    code = models.CharField(max_length=3)  # Código do aeroporto
    city = models.CharField(max_length=64)  # Cidade do aeroporto

    def __str__(self):
        return f"{self.city} ({self.code})"

# Modelo Flight
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")  # Aeroporto de origem
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")  # Aeroporto de destino
    duration = models.IntegerField()  # Duração do voo

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

# Modelo Passenger
class Passenger(models.Model):
    first = models.CharField(max_length=64)  # Primeiro nome
    last = models.CharField(max_length=64)  # Sobrenome
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")  # Relacionamento com Flight

    def __str__(self):
        return f"{self.first} {self.last}"
