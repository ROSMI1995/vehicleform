from django.db import models

# Create your models here.

class VehicleData(models.Model):

	STATUS =(
		('Two wheeler', 'Two wheeler'),
		('Three wheeler', 'Three wheeler'),
		('Four wheeler', 'Four wheeler')

		)
	Vehicle_Number = models.CharField(max_length=25)
	Vehicle_Type = models.CharField(max_length=255, null=True, choices=STATUS)
	Vehicle_Model = models.CharField(max_length=255)
	Description = models.TextField()
	date_added = models.DateTimeField(auto_now= True)


	class Meta:
		ordering=('-date_added',)

	def __str__(self):
		return str(self.Vehicle_Number)

    