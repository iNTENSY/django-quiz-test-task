import requests
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status

from quiz_api.mixins import SerializerClassesMixin
from quiz_api.models import Quiz, Category
from quiz_api.serializers import QuizSerializer, QuestionSerializer


class QuizViewSet(SerializerClassesMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    List = QuizSerializer
    Retrieve = QuizSerializer
    Create = QuestionSerializer
    queryset = Quiz.objects.all()

    def create(self, request, *args, **kwargs) -> Response:
        count: int = request.data['questions_num']
        questions: list = self.get_questions(count=count)
        pre_last: int = questions[-2]['id'] if len(questions) > 1 else None

        self.create_objects(questions=questions)

        try:
            current_q = Quiz.objects.get(question_id=pre_last)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = QuizSerializer(current_q)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_objects(self, questions: list) -> None:
        repeating_count: int = 0

        for question in questions:
            category, _ = Category.objects.get_or_create(title=question['category']['title'],
                                                         created_at=question['category']['created_at'])
            _, is_created = Quiz.objects.get_or_create(question_id=question['id'],
                                                       category=category,
                                                       value=question['value'],
                                                       text=question['question'],
                                                       answer=question['answer'],
                                                       created_at=question['created_at'])
            if not is_created:
                repeating_count += 1

        if repeating_count != 0:
            self.create_objects(self.get_questions(count=repeating_count))

    def get_questions(self, count: int) -> list:
        url = 'https://jservice.io/api/random'
        response = requests.get(url, params={'count': count})
        return response.json()
