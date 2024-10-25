# myapp/serializers.py
from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'  # 或者指定具体的字段，例如 ['id', 'value', 'created_at']
