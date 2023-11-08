from django.contrib import admin
#from .models import ReviewModel
from.models import category, image, user_home
# Register your models here.

#admin.site.register(ReviewModel)
admin.site.register(category)
admin.site.register(image)
admin.site.register(user_home)