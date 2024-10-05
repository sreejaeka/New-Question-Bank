from rest_framework import status
from rest_framework.response import Response
from .models import CustomUser, College, QuestionPaper, AnswerKey
from rest_framework.serializers import ModelSerializer


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'user_type', 'name']
    
    def create(self, validated_data):
        user = CustomUser(username=validated_data['username'], name=validated_data['name'], user_type=validated_data['user_type'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class CollegeSerializer(ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class QuestionPaperSerializer(ModelSerializer):
    class Meta:
        model = QuestionPaper
        fields = '__all__'

class AnswerKeySerializer(ModelSerializer):
    class Meta:
        model = AnswerKey
        fields = '__all__'
