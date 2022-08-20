from core.serializers.content import CreateSerializer, RetrieveSerializer, ListSerializer
from core.models import Content

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView


class CreateView(CreateAPIView):

    queryset = Content.objects.all()
    serializer_class = CreateSerializer


class RetrieveView(RetrieveAPIView):

    serializer_class = RetrieveSerializer

    def get_queryset(self):
        user = self.request.user
        return user.content_set.all()


class ListView(ListAPIView):

    serializer_class = ListSerializer

    def get_queryset(self):
        user = self.request.user
        return user.content_set.all().values('id', 'title', 'file_format')

