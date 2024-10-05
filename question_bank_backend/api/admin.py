from django.contrib import admin
from . import models

admin.site.register(models.CustomUser)
admin.site.register(models.College)
admin.site.register(models.QuestionPaper)
admin.site.register(models.AnswerKey)
# Register your models here.
