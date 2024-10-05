from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255, default='Student') # Student, Teacher, Admin
    
    def __str__(self):
        return self.username

class College(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class QuestionPaper(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    question_paper = models.FileField(upload_to='question_paper')
    
    def __str__(self):
        return self.title


class AnswerKey(models.Model):
    question_paper = models.ForeignKey(QuestionPaper, on_delete=models.CASCADE)
    answer_key = models.FileField(upload_to='answer_key')
    
    def __str__(self):
        return f'Answer Key for {self.question_paper.title}'

