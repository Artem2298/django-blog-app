from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer

class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()  # Получаем все статьи из базы
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)  # Получаем данные от клиента
        if serializer.is_valid():  # Проверяем, что данные валидны
            serializer.save()  # Сохраняем новую статью в базе
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Ответ с кодом 201
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Ошибка валидации
