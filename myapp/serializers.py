from rest_framework import serializers
from .models import Student
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token=super().get_token(user)

        token['username']=user.username
        token['role']= user.role

        return token
    
    def validate(self,attrs):
        data=super().validate(attrs)

        data['role']=self.user.role
        return data