from django.db import models


class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    order = models.IntegerField()


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    contact_no = models.IntegerField()


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images", default="")
   # time = models.DateTimeField()




class Material(models.Model):
    mat_id = models.AutoField(primary_key=True)
    mat_link = models.CharField(max_length=255)
    mat_description = models.CharField(max_length=255)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
