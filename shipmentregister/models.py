import datetime
from django.db import models

class ModeOfTransportModel(models.Model):
    mode_of_transport = models.CharField(max_length=50)

    def __str__(self):
        return str(self.mode_of_transport)

    


class ShipmentDetailsModel(models.Model):

    
    MOT_OPTIONS = [
        ('Bike', 'Bike'),
        ('Car', 'Car'),
        ('Drone', 'Drone'),
        ('Starship robot', 'Starship robot'),
        ('Truck', 'Truck'),        
        ('Van', 'Van')   
    ]

    tracking_number = models.IntegerField(primary_key=True, unique=True )
    origin = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    expected_delivery_date = models.DateField(default= datetime.date.today)
    mode_of_transport = models.ForeignKey(ModeOfTransportModel, on_delete=models.SET_NULL, null=True)
    
    
    def __str__(self):
        return str(self.tracking_number)

    
