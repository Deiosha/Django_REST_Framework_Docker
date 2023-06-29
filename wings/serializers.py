from rest_framework import serializers
from .models import Wing


class WingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'description', 'created_at')
        model = Wing
