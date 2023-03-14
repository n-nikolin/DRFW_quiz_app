from rest_framework import serializers
from .models import Quiz, Question, Result, Choice


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'title', 'description', 'value']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'value']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']


class QuizSerializer(serializers.ModelSerializer):
    # TODO: refering to Writable Nested Serializers make a custom create method
    # TODO: make LIST and DETAIL viewset
    questions = QuestionSerializer(many=True)
    results = ResultSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['url', 'id', 'title', 'description', 'created',
                  'edited', 'questions', 'results']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        results_data = validated_data.pop('results')
        quiz = Quiz.objects.create(**validated_data)
        for result_data in results_data:
            Result.objects.create(quiz=quiz, **result_data)
        for question_data in questions_data:
            choices_data = question_data.pop('choices')
            question = Question.objects.create(quiz=quiz, **question_data)
            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)
        return quiz
