from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from socialnetwork.models import Blogs, Like
from socialnetwork.serializer import BlogsSerializer, BlogsSerializerResponse, LikeSerializer
from socialnetwork.social_network_pagination import SocialNetworkPagination


# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializerResponse
    pagination_class = SocialNetworkPagination
    permission_class = [IsAuthenticated]

    def create(self, request):
        serializer = BlogsSerializer(data=request.data,context={'user':request.user.id})
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            blog_data = BlogsSerializer(instance).data
            return Response({"msg": "Blog post added", "data": blog_data}, status=status.HTTP_200_OK)

    def destroy(self, request):
        id = request.query_params.get('id', None)
        if id:
            blog_to_del = Blogs.objects.filter(id=id)
            if blog_to_del:
                blog_to_del.delete()
                return Response({"msg":"Blog deleted!!"})
            else:
                return Response({"msg": "Blog not found"},status=400)

        else:
            return Response({"msg": "id not found"},status=400)

    @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated])
    def update_like_blog(self, request):
        blog_id = request.data.get('blog_id', None)
        like_blog = request.data.get('like_blog', False)

        if blog_id is None:
            return Response({"msg": "Blog ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        blog = get_object_or_404(Blogs, id=blog_id)

        if like_blog:
            # Check if the user has already liked the blog
            check_like = Like.objects.filter(user=request.user, blog=blog)
            if check_like.exists():
                return Response({"msg": "You have already liked this blog"}, status=status.HTTP_400_BAD_REQUEST)

            like = Like.objects.create(user=request.user, blog=blog, is_liked=True)
            like_serializer = LikeSerializer(like).data
            return Response({"msg": "Blog liked successfully", "like": like_serializer}, status=status.HTTP_200_OK)
        else:
            # Unlike the blog
            un_like = Like.objects.filter(user=request.user, blog=blog)
            un_like.update(is_liked=False)
            # un_like_serializer = LikeSerializer(un_like).data
            return Response({"msg": "Blog unliked successfully"}, status=status.HTTP_200_OK)





