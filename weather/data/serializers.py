from rest_framework import serializers
from .models import Ville, Echeance
class EcheanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Echeance
		fields = '__all__'

class VilleSerializer(serializers.ModelSerializer):
	villes = EcheanceSerializer(many=True, read_only=True, required=False)
	class Meta:
		model = Ville
		fields = '__all__'
