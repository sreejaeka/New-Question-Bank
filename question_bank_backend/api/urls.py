from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('college/', college_api, name='college_api'),
    path('questionpaper/', get_question_paper, name='get_question'),
    path('questionpaper/add/', add_question_paper, name='add_question'),
    path('answerkey/', get_answer_key, name='get_answer'),
    path('answerkey/add/', add_answer_key, name='add_answer'),
]
