from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions


from apps.translatable_content.models import Post, Content, Tag, Media
from .serializers import (
    PostSerializer, 
    MediaSerializer, 
    TagSerializer, 
    ContentSerializer
)

""" @csrf_exempt
def test(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)

    return JsonResponse(serializer.data, safe=False) """

class PostDetail(APIView):
    """
    Post Detail View
    """

    def get(self, request, format=None):
        """
        Return a detail of a Post.
        * Requires the slug of the Post
        """

        try:
            slug = request.GET.get('slug')
        except:
            slug = None         
            
        
        post = Post.objects.filter(slug=slug)
        if not post:
            message = 'Post not exists or Invalidad data format'
            return Response(message, status.HTTP_404_NOT_FOUND)

        else:

            serializer = PostSerializer(post, many=True)
            return JsonResponse(serializer.data, safe=False)

        
        