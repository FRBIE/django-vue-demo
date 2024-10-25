from django.db import models

# Create your models here.
class Data(models.Model):
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')  # 指定上传的图片存储目录
    uploaded_at = models.DateTimeField(auto_now_add=True)  # 记录上传时间

    def __str__(self):
        return self.image.name


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
