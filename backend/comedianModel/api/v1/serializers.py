from rest_framework import serializers
from comedianModel.models import Comedians, Jokes


class ComediansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comedians
        fields = "__all__"


class JokesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jokes
        fields = "__all__"
