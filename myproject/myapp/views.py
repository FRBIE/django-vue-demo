from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Data, ImageUpload, User
from .serializers import DataSerializer
from rest_framework.decorators import action
from rest_framework.request import Request
from django.shortcuts import render, redirect
from .forms import ImageUploadForm


# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()  # 保存上传的文件
#             return redirect('upload_image')  # 重定向到上传页面或成功页面
#     else:
#         form = ImageUploadForm()
#     return render(request, 'upload_image.html', {'form': form})


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


@api_view(['POST'])
def upload_image(request):
    image_file = request.FILES.get('image')  # 获取上传的文件
    if image_file:
        image_upload = ImageUpload(image=image_file)
        image_upload.save()  # 保存到数据库
        return JsonResponse({'message': 'Image uploaded successfully!'}, status=200)
    return JsonResponse({'error': 'No image provided!'}, status=400)


class ApiUser(viewsets.ViewSet):
    @action(methods=['post'], detail=False)
    def login(self, request):
        user = User.objects.filter(username=request.data['username']).first()

        result = {
            "code": 200,
            "msg": "登录成功",
            "body": ""
        }
        if user and user.password == request.data['password']:
            return Response(result)
        else:
            result['msg'] = "登录失败"
            result['code'] = -1
            return Response(result)

    @action(methods=['post'], detail=False)
    def register(self, request):
        username = request.data['username']
        password = request.data['password']
        User.objects.create(username=username, password=password)
        result = {
            "code": 200,
            "msg": "注册成功",
            "body": ""
        }
        return Response(result)
# class ApiUser(viewsets.ViewSet):
#     @action(methods=['post'], detail=False)
#     def login(self, request):
#         username = request.data['username']
#         password = request.data['password']
#           这个用的是auth_user表的数据
#         user = authenticate(username=username,password=password)
#         if user is not None:
#             result = {
#                 "code": 200,
#                 "msg": "登录成功",
#                 "body": ""
#             }
#             return Response(result)
#         else:
#             result = {
#                 "code": -1,
#                 "msg": "登录失败",
#                 "body": ""
#             }
#             return Response(result, status=status.HTTP_401_UNAUTHORIZED)  # 登录失败返回401
#
#     @action(methods=['post'], detail=False)
#     def register(self, request):
#         username = request.data['username']
#         password = request.data['password']
#         User.objects.create(username=username, password=password)
#         result = {
#             "code": 200,
#             "msg": "注册成功",
#             "body": ""
#         }
#         return Response(result)
