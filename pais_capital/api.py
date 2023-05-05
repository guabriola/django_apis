from .models import pais_capital
from rest_framework import viewsets, permissions
from .serializers import PaisCapitalSerializer

#Decimos que operaciones vamos a poder hacer. 
class PaisCapitalViewSet(viewsets.ModelViewSet):
    queryset = pais_capital.objects.all()#Le estamos diciendo que consulte todos los objetos de pais_capital
    permission_classes = [permissions.AllowAny] #Permitimos que cualquiera pueda consultar
    serializer_class = PaisCapitalSerializer #Especificamos a partir de quie serializer va a convertir a Json. 

