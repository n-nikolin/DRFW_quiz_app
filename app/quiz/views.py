from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Quiz, Question, Result
from .serializers import QuizSerializer, QuestionSerializer, ResultSerializer
from collections import Counter
from django.db.models import Q
from functools import reduce


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class MyResultView(views.APIView):
    def get(self, request):
        # change this
        results = Result.objects.all()
        serializer_class = ResultSerializer(results, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        """
        POST DATA STRUCTURE
        {
            quiz_id: INT,
            choices: [
                {q_id: INT, c_id: INT, value: INT},
                ...,
                {q_id: INT, c_id: INT, value: INT}
            ]
        }
        """
        # refactor and clean
        answers = request.data['choices']
        results = Result.objects.all().filter(
            quiz_id=request.data['quiz_id'])
        if not results:
            return Response('inconsistent data')
        answers_list = [i['value'] for i in answers]
        counter = Counter(answers_list)
        most_common_value = counter.most_common(3)[0][1]
        equals = []
        for k, v in counter.items():
            if v == most_common_value:
                equals.append(k)
        response = []
        for result in results:
            if result.value in equals:
                response.append(result)
        result_serializer = ResultSerializer(response, many=True)
        return Response(result_serializer.data)
