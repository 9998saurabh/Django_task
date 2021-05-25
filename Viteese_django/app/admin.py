from django.contrib import admin
from .models import Question,user_data,Registration

admin.site.register(Question)
admin.site.register(user_data)
admin.site.register(Registration)