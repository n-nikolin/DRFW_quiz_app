from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

class Result(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    value = models.IntegerField()
    quiz = models.ForeignKey(Quiz, related_name='results', on_delete=models.CASCADE)

class Choice(models.Model):
    text = models.TextField()
    value = models.IntegerField()
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)