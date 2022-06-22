from datetime import datetime

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Questions

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = ('question', 'answer')
