from core.serializers.content import CreateSerializer, RetrieveRequestSerializer, RetrieveResponseSerializer
from core.models import Content

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core import serializers


class CreateView(CreateAPIView):

    queryset = Content.objects.all()
    serializer_class = CreateSerializer


class RetrieveView(APIView):

    def get(self, request):
        serializer = RetrieveRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        user = request.user
        title, file_format = serializer.validated_data['title'], serializer.validated_data['file_format']
        content = get_object_or_404(user.content_set.all(), title=title, file_format=file_format)
        serializer = RetrieveResponseSerializer(content)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )


