from rest_framework import serializers
from .models import Ville, Echeance
class EcheanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Echeance
		fields = '__all__'

class VilleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ville
		fields = '__all__'