from rest_framework import serializers

from ...models import Post, Category


class PostSerializer(serializers.ModelSerializer):

    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.ReadOnlyField(source="get_absolute_url")

    class Meta:
        model = Post
        fields = [
            "id", "author", "title", "content", "snippet", "category",
            "status", "relative_url", "published_date", "created_date"
        ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]
