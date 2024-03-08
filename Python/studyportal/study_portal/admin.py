from django.contrib import admin
from .models import Video
from .models import Course
from .models import Material
# Register your models here.


admin.site.register(Video)
admin.site.register(Course)
admin.site.register(Material)