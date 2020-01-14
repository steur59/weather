from django.db import models

# Create your models here.
class Ville(models.Model):
	nom = models.CharField(max_length=100)

class Echeance(models.Model):
	ville = models.ForeignKey(Ville, related_name='echeances' ,on_delete=models.CASCADE)
	date = models.CharField(max_length=100)
	heure = models.CharField(max_length=100)
	temp_2m = models.CharField(max_length=100)
	temp_sol = models.CharField(max_length=100)
	temp_850hPa = models.CharField(max_length=100)
	temp_500hPa = models.CharField(max_length=100)
	pression_niveau_de_la_mer = models.CharField(max_length=100)
	pluie_interval_3h = models.CharField(max_length=100)  
	pluie_convective_interval_3h = models.CharField(max_length=100)
	humidité_2m = models.CharField(max_length=100)
	vent_moyen_10m = models.CharField(max_length=100)
	vent_rafales_10m = models.CharField(max_length=100)
	vent_direction_10m = models.CharField(max_length=100)
	iSO_zero = models.CharField(max_length=100)
	risque_neige = models.CharField(max_length=100)
	cape = models.CharField(max_length=100)
	nebulosite_haute = models.CharField(max_length=100)
	nebulosite_moyenne = models.CharField(max_length=100)
	nebulosite_basse = models.CharField(max_length=100)
	nebulosite_totale = models.CharField(max_length=100)