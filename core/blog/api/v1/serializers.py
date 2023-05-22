from rest_framework import serializers

from ...models import Post


# class PostSerializer(serializers.Serializer):

#     title = serializers.CharField()


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "id", "title", "content", "author", "status", "category", "published_date"
        ]
