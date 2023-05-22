from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ...models import Post
from .serializers import *


# @api_view()
# def post_list(request):
    # """
    # List all blog post, or create a new post.
    # """

#     posts = Post.objects.filter(status=True)
#     serializers = PostSerializer(posts, many=True)
#     return Response(serializers.data)


# @api_view()
# def post_detail(request, id):
    # """
    # Show the details of a post with ID
    # """

#     post = get_object_or_404(Post, pk=id, status=True)
#     serializers = PostSerializer(post)
#     return Response(serializers.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    """
    List all blog post, or create a new post.
    """

    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request, id):
    """
    Retrieve, update or delete a post with ID
    """

    post = get_object_or_404(Post, pk=id, status=True)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
