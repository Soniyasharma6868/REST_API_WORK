import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import *
from rest_framework import viewsets

def StudentDetails(request,pk):
    stud=Student.objects.get(id=pk)
    #print(stud)
    serializer=StudentSerializer(stud)
    #print(serializer)
    #print(serializer.data)
    #json_data=JSONRenderer().render(serializer.data)
    #print(json_data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

def StudentDetailsList(request):
    stud=Student.objects.all()
    #print(stud)
    serializer=StudentSerializer(stud,many=True)
    #print(serializer)
    #print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    #print(json_data)
    #return JsonResponse(serializer.data,safe=False)
    return HttpResponse(json_data,content_type='application/json')



######## function base views ################
@csrf_exempt
def StudentCreate(request):
    if request.method =='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
#@method_decorator(csrf_exempt,name='dispatch')
@csrf_exempt
def student_api(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')


    if request.method =='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method =='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        id=pythondata.get('id')
        stud=Student.objects.get(id=id)
        serializer=StudentSerializer(stud,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stud=Student.objects.get(id=id)
        stud.delete()
        res={'msg':'Data Deleted!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')

#class base views
@method_decorator(csrf_exempt,name='dispatch')
class StaffAPI(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Staff.objects.get(id=id)
            serializer=StaffSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Staff.objects.all()
        serializer=StaffSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')


    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StaffSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StaffSerializer(data=pythondata)
        id=pythondata.get('id')
        stud=Staff.objects.get(id=id)
        serializer=StaffSerializer(stud,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stud=Staff.objects.get(id=id)
        stud.delete()
        res={'msg':'Data Deleted!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')


# REST Framework function based view

@api_view()
def EmployeeCreate(request):
    return Response({'msg':'Createing fun base view in DRF'})


# @api_view(['GET'])
# def EmployeeCreate(request):
#     return Response({'msg':'Createing fun base view in DRF'})

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@csrf_exempt
def EmployeeAPI(request, pk=None):
    if request.method == 'GET':
        # id=request.data.get('id')
        id = pk
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    # return Response({'msg':'Createing fun base view in DRF by get'})

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method == 'PUT':
        # id=request.data.get('id')
        id = pk
        emp = Employee.objects.get(pk=id)
        # serializer=EmployeeSerializer(emp,data=request.data,partial=True)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Completely Updated'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        # id=request.data.get('id')
        id = pk
        emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data partialy Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        # id=request.data.get('id')
        id = pk
        emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        emp.delete()

        return Response({'msg': 'Data Delete'})
        # return Response(serializer.errors)


# REST Framework Class based view
class EmployeeAPIView(APIView):
    def get(self, request, pk=None, format=None):
        # id=request.data.get('id')
        id = pk
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    # return Response({'msg':'Createing fun base view in DRF by get'})

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        # id=request.data.get('id')
        id = pk
        emp = Employee.objects.get(pk=id)
        # serializer=EmployeeSerializer(emp,data=request.data,partial=True)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Completely Updated'})
        return Response(serializer.errors)

    def patch(self, request, pk, format=None):
        # id=request.data.get('id')
        id = pk
        emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data partialy Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        emp = Employee.objects.get(pk=id)
        emp.delete()
        return Response({'msg': 'Data Delete'})

class StudentList(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,*kwargs)


class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,*kwargs)


class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,*kwargs)


class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)


class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,*kwargs)




################use all in one and perform crud in all in one using mixin ###############################

#List and Create - PK not allowed
class StudentListCreateAPIVIEW(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,*kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,*kwargs)

#Reteriteve,update, delete - PK not allowed
class StudentUDRAPIVIEW(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,*kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,*kwargs)


### Concrete View Class

class studList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class studCreateList(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class studRetrieveList(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class studUpdateList(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class studDestroyList(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class studListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class RUDstud(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class RUstud(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class RDstud(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class RUDstud(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


################# Create,list and update retive ,destroy

class STudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class STudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stud = Student.objects.all()
        serializer = StudentSerializer(stud, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stud = Student.objects.get(id=id)
            serializer = StudentSerializer(stud)
            return Response(serializer.data)

    def create(self, request, pk=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'})
        return Response(serializer.errors)

    def update(self, request, pk=None):
        id = pk
        stud = Student.objects.get(pk=id)
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stud = Student.objects.get(pk=id)
        stud.delete()
        return Response({'msg': 'Data deleted'})


class StudenModeltViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# ReadOnlyModelViewSet class
class StudenReadOnlyModeltViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer