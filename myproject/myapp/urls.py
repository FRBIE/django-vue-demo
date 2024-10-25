# myapp/urls.py
from django.urls import path
from rest_framework import routers

from .views import upload_image, ApiUser

router = routers.DefaultRouter()
router.register('user', ApiUser, basename='user')

urlpatterns = [

    path('upload/', upload_image, name='upload_image'),

]

urlpatterns += router.urls
