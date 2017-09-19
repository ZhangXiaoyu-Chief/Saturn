from books.models import Publisher, Author
from books.serializers import PublisherSerializer, AuthorSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.


@api_view(["GET", "POST"])
def publisher_list(request):

    if request.method == "GET":
        """
        处理GET请求，获取列表
        """
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        # Response需要api_view装饰过的视图函数
        return Response(serializer.data)

    elif request.method == "POST":
        """
        处理POST请求，创建对象
        """
        data = JSONParser().parse(request)
        serializer = PublisherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def publisher_detail(request, pk):
    try:
        publisher = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        """
        处理GET请求，获取单个对象
        """
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)

    elif request.method == 'PUT':
        """
        处理PUT请求，修改对象
        """
        data = JSONParser().parse(request)
        serializer = PublisherSerializer(publisher, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        '''
        DELETE请求，删除对象
        '''
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorList(APIView):

    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        author = self.get_object(pk)
        author.delete()
        return Response(status.HTTP_204_NO_CONTENT)