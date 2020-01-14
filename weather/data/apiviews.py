from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Ville, Echeance
from .serializers import VilleSerializer, EcheanceSerializer


class VilleList(generics.ListCreateAPIView):
	queryset = Ville.objects.all()
	serializer_class = VilleSerializer

class VilleDetail(generics.RetrieveDestroyAPIView):
	queryset = Ville.objects.all()
	serializer_class = VilleSerializer

class EcheanceList(generics.ListCreateAPIView):
	def get_queryset(self):
		queryset = Echeance.objects.filter(Echeance_id=self.kwargs["pk"])
		return queryset
	serializer_class = EcheanceSerializer

class CreateEcheance(generics.CreateAPIView):
	serializer_class = EcheanceSerializer