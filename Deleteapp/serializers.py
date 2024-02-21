from rest_framework import serializers
from Deleteapp.models import delete
class deleteserializers(serializers.ModelSerializer):
    class Meta:
        model=delete
        fields='__all__'