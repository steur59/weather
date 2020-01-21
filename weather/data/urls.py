from django.urls import path
from .apiviews import VilleList, VilleDetail, EcheanceList, CreateEcheance , EcheanceDetail
urlpatterns = [
path("villes/", VilleList.as_view(), name="Liste des villes"),
path("villes/<int:pk>/", VilleDetail.as_view(), name="Detail d'une ville"),
path("echeances", EcheanceList.as_view(), name="Liste des echéances"),
path("echeances/<int:pk>", EcheanceDetail.as_view(), name="Detail d'une echéance"),
#path("villes/<int:pk>/echeances", EcheanceByVille.as_view(), name="Liste des echéances d'une ville"),
path("new/", CreateEcheance.as_view(), name="create_echeance"),
]
