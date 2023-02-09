from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from quiz.views import QuizViewSet, MyResultView


router = routers.DefaultRouter()
router.register(r'quizzes', QuizViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'my_result/', MyResultView.as_view()),
    path('', include(router.urls))
]