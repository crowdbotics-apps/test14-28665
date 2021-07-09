from rest_framework import authentication
from comedianModel.models import Comedians, Jokes
from .serializers import ComediansSerializer, JokesSerializer
from rest_framework import viewsets


class ComediansViewSet(viewsets.ModelViewSet):
    serializer_class = ComediansSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Comedians.objects.all()


class JokesViewSet(viewsets.ModelViewSet):
    serializer_class = JokesSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Jokes.objects.all()
