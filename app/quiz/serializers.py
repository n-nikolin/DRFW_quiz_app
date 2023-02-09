from rest_framework import serializers
from .models import Quiz, Question, Result, Choice


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'title', 'description', 'value']

class ChoiceSerializer( serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'value']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = ['id', 'text', 'quiz', 'choices']


class QuizSerializer(serializers.ModelSerializer):
    # TODO: refering to Writable Nested Serializers make a custom create method
    # TODO: make LIST and DETAIL viewset
    questions = QuestionSerializer(many=True)
    results = ResultSerializer(many=True)
    class Meta:
        model = Quiz
        fields = ['url', 'id', 'title', 'description', 'created',
                  'edited', 'questions', 'results']

