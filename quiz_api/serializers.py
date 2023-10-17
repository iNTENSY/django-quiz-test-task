from rest_framework import serializers

from quiz_api.models import Quiz


class QuestionSerializer(serializers.Serializer):
    """
    Сериализатор для запросов к django-серверу.
    """
    questions_num = serializers.IntegerField(min_value=0)


class QuizSerializer(serializers.ModelSerializer):
    """
    Сериализатор для ответов пользователю по модели Quiz.
    """
    category = serializers.StringRelatedField()

    class Meta:
        model = Quiz
        fields = ('question_id',
                  'text',
                  'category',
                  'answer',
                  'value')
