from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse
from .models import Poll

# Create your views here.

# def ville_list(request):
# 	MAX_OBJECTS = 20
# 	villes = Ville.objects.all()[:MAX_OBJECTS]
# 	data = {"results": list(villes.values("nom"))}
# 	return JsonResponse(data)

# def ville_detail(request, pk):
# 	ville = get_object_or_404(Ville, pk=pk)
# 	datas = {"results": {
# 		"nom": ville.nom
# 	}}
# 	return JsonResponse(data)

# def echeance_list(request):
# 	MAX_OBJECTS = 20
# 	echeances = Echeance.objects.all()[:MAX_OBJECTS]
# 	data = {"results": list(echeances.values("date"))}
# 	return JsonResponse(data)

# def echeance_detail(request, pk):
# 	echeance = get_object_or_404(Echeance, pk=pk)
# 	datas = {"results": {
# 		"date": echeance.date
# 		"temp_sol" : echeance.temp_sol
# 		"humidité_2m" : echeance.humidité_2m
# 		"vent_moyen_10m" : echeance.vent_moyen_10m
# 		"risque_neige" : echeance.risque_neige
# 		"pluie_interval_3h" : echeance.pluie_interval_3h
# 	}}
# 	return JsonResponse(data)
