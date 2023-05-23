from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins

from ...models import Post
from .serializers import *


# class PostList(APIView):
#     """
#     List all blog post, or create a new post.
#     """

#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self, request):
#         """
#         Return a list of all posts.
#         """

#         posts = Post.objects.filter(status=True)
#         serializers = PostSerializer(posts, many=True)
#         return Response(serializers.data)

#     def post(self, request):
#         """
#         Create a new post with provided data
#         """

#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# class PostDetail(APIView):
#     """
#     Retrieve, update or delete a post with ID
#     """

#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self, request, id):
#         """
#         Retrieving the post data
#         """

#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def put(self, request, id):
#         """
#         Updating the post data
#         """

#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def delete(self, request, id):
#         """
#         Removing the post data
#         """

#         post = get_object_or_404(Post, pk=id, status=True)
#         post.delete()
#         return Response({"detail": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)


class PostList(ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a post instance.
    """

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostDetail(RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a post with ID.
    """

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
