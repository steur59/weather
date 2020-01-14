from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse
from .models import Poll

# Create your views here.
def ville_list(request):
	MAX_OBJECTS = 20
	villes = Ville.objects.all()[:MAX_OBJECTS]
	data = {"results": list(villes.values("nom"))}
	return JsonResponse(data)

def ville_detail(request, pk):
	ville = get_object_or_404(Ville, pk=pk)
	datas = {"results": {
		"nom": ville.nom
	}}
	return JsonResponse(data)
# in urls.py

from django.urls import path
from .views import data_list, ville_detail

urlpatterns = [
	path("data/", ville_list, name="ville_list"),
	path("data/<int:pk>/", ville_detail, name="ville_detail")
]