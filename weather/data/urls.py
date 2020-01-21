from django.urls import path
from .apiviews import VilleList, VilleDetail, EcheanceList, CreateEcheance , EcheanceDetail
urlpatterns = [
path("ville/", VilleList.as_view(), name="villes_list"),
path("ville/<int:pk>/", VilleDetail.as_view(), name="villes_detail"),
path("ville/<int:pk>/echeances", EcheanceList.as_view(), name="echeance_list"),
path("ville/<int:pk1>/echeances/<int:pk2>", EcheanceDetail.as_view(), name="echeance_detail"),
path("new/", CreateEcheance.as_view(), name="create_echeance"),
]
