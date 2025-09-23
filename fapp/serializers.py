from rest_framework import serializers
from .models import McDonalds   # import your model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = McDonalds
        fields = '__all__'   # include all model fields in the API
