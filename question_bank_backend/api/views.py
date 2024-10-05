from django.shortcuts import render

from .models import CustomUser, College, QuestionPaper, AnswerKey
from .serializers import CustomUserSerializer, AnswerKeySerializer, QuestionPaperSerializer, CollegeSerializer

from rest_framework import status
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        user_type = user.user_type
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token' : token.key, 'user_type' : user_type}, 200)
    return Response({'error': 'Invalid username or password'}, 401)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def college_api(request):
    if request.method == "GET":
        colleges = College.objects.all()
        serializer = CollegeSerializer(colleges, many=True)
        print(serializer)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])

def add_question_paper(request):
    try:
        question_paper = request.FILES['question_paper']
        title = request.data.get('title')
        college = request.data.get('college')
        question_paper_obj = QuestionPaper(question_paper=question_paper, title=title, college=college)
        question_paper_obj.save()
        return Response({"message": "Question Paper uploaded successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Failed to upload question paper"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_question_paper(request):
    college_id = request.query_params.get('college', None)
    if college_id:
        question_papers = QuestionPaper.objects.filter(college=college_id)
        serializer = QuestionPaperSerializer(question_papers, many=True)
        return Response(serializer.data, 200)
    else:
        return Response({"message": "College ID not provided"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_answer_key(request):
    question_id = request.query_params.get('question_id', None)
    print(question_id)
    if question_id:
        try:
            answer_key = request.FILES['answer_key']
            # question = QuestionPaper.objects.get(question_paper_id=question_id)
            answer_key_obj = AnswerKey(answer_key=answer_key, question_paper_id=question_id)
            answer_key_obj.save()
            return Response({"message": "Answer Key uploaded successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"message": "Failed to upload answer key"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Question ID not provided"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_answer_key(request):
    question_id = request.query_params.get('question_id', None)
    if question_id:
        answer_key = AnswerKey.objects.filter(question_paper_id=question_id)
        serializer = AnswerKeySerializer(answer_key, many=True)
        print(serializer.data)
        return Response(serializer.data, 200)
    else:
        return Response({"message": "Question ID not provided"}, status=status.HTTP_400_BAD_REQUEST)