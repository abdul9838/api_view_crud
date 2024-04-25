from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .serializers import StudentSerializers
from .models import Student

@api_view(['GET','POST','PUT','DELETE'])
def studentapi(request):
    if request.method == 'GET':
        id = request.query_params.get('id')
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        serializer = StudentSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            res = { 'msg': 'DAta Inserted success full!!'}
            return Response(res) 
        return Response(serializer.errors)   
    if request.method == 'PUT':
        data=request.data
        stu = Student.objects.get(id = data.get('id') )
        serializer = StudentSerializers(stu,data=data,partial = True)
        if serializer.is_valid():
            serializer.save()
            res = { 'msg': 'DAta Updated success full!!'}
            return Response(res) 
        return Response(serializer.errors)
    if request.method == 'DELETE':
        id=request.data.get('id')
        stu = Student.objects.get(id = id )
        stu.delete()
        res = { 'msg': 'DAta Deleted success full!!'}
        return Response(res) 
        