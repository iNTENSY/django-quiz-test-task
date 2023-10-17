from rest_framework.serializers import ModelSerializer


class SerializerClassesMixin:
    """
    Миксин позволяющий гибко использовать сериализаторы в вьюсетах.
    """

    Retrieve: ModelSerializer = None
    List: ModelSerializer = None
    Create: ModelSerializer = None

    def set_serializers(self) -> dict[str, ModelSerializer]:
        __serializer_classes = {
            'list': self.List,
            'retrieve': self.Retrieve,
            'create': self.Create
        }
        return __serializer_classes

    def get_serializer_class(self) -> ModelSerializer:
        serializer = self.set_serializers().get(self.action, self.set_serializers()['list'])
        return serializer