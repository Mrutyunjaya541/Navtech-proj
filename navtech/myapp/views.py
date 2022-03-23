from django.shortcuts import render
import io
# Create your views here.
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import  api_view, permission_classes,authentication_classes
from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import json
from rest_framework.response import Response
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from .models import Product,Order_Info
from django.contrib.auth.models import User
#from .models import Order_Info
from django.http import HttpResponse



class RegisterApiView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Upload_Data(GenericAPIView):
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        user = request.user
        user_obj = User.objects.get(username=user)
        if user.is_staff == True:
            file = self.request.FILES.get('file_data')
            file_data = file.read().decode('utf-8')
            io_string = io.StringIO(file_data)
            reader = csv.reader(io_string)
            header = next(reader)
            rows = []
            for row in reader:
                rows.append(row)
            for i in rows:
                if Product.objects.filter(product_name=i[0]):
                    obj = Product.objects.get(product_name=i[0])
                    print(obj)
                    obj.product_price = i[1]
                    obj.save()
                else:
                    obj = Product.objects.create(product_name=i[0],product_price=i[1])
                    obj.save()
            return Response({'success':True,'msg':'created Successfully'})
        else:
            return Response({'success':False,'msg':'You are not an Adminstrator'})
        


    
        
from .models import Order_Info  
from datetime import datetime, timedelta

     

class GetLast3MonthInfo(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        user_obj = User.objects.get(username=user)
        if user.is_staff == True:
            response = HttpResponse(content_type='text/csv')  
            response['Content-Disposition'] = 'attachment; filename="file.csv"' 
            writer = csv.writer(response)
            today = datetime.today()
            long_ago = today + timedelta(days=-90)
            obj = Order_Info.objects.filter(order_date__gte = long_ago)
            writer.writerow(["Product","Price","Order_Date"]) 
            for i in obj: 
                writer.writerow([i.product.product_name,i.product.product_price,i.order_date])
            return response
        else:
            return Response({'status':False,"msg":"Yoa are not an admin user"}) 