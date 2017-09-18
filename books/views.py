from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from books.models import Publisher
from books.serializers import PublisherSerializer
from rest_framework.parsers import JSONParser
# Create your views here.


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = "application/json"
        super(JSONResponse,self).__init__(content, **kwargs)


@csrf_exempt
def publisher_list(request):

    if request.method == "GET":
        """
        处理GET请求，获取列表
        """
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return JSONResponse(serializer.data)

    elif request.method == "POST":
        """
        处理POST请求，创建对象
        """
        data = JSONParser().parse(request)
        serializer = PublisherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)




@csrf_exempt
def publisher_detail(request, pk):
    try:
        publisher = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        """
        处理GET请求，获取单个对象
        """
        serializer = PublisherSerializer(publisher)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        """
        处理PUT请求，修改对象
        """
        data = JSONParser().parse(request)
        serializer = PublisherSerializer(publisher, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        '''
        DELETE请求，删除对象
        '''
        publisher.delete()
        return HttpResponse(status=204)
