from django.urls import path
from .apiviews import VilleList, VilleDetail, EcheanceList, CreateEcheance
urlpatterns = [
path("ville/", VilleList.as_view(), name="villes_list"),
path("ville/<int:pk>/", VilleDetail.as_view(), name="villes_detail"),
path("echeance/", EcheanceList.as_view(), name="echeance_list"),
path("new/", CreateEcheance.as_view(), name="create_echeance"),
]
