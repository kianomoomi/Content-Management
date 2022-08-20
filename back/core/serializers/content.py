from rest_framework import serializers
from core.models import Content


class CreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('title', 'file_format', 'file')

    def create(self, validated_data):
        title, file_format, file = validated_data['title'], validated_data['file_format'], validated_data['file']
        content = Content.objects.create(
            title=title,
            file_format=file_format,
            file=file,
            extra={k: self.initial_data[k] for k in set(self.initial_data) - set(validated_data)}
        )
        user = self.context['request'].user

        content.users.add(user)

        return content


class RetrieveRequestSerializer(serializers.Serializer):

    title = serializers.CharField(required=True)
    file_format = serializers.ChoiceField(choices=(('V', 'Video'), ('A', 'Audio'), ('D', 'Document')))


class RetrieveResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('title', 'file_format', 'file', 'extra')

