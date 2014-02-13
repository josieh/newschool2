from django.contrib import admin

# Register your models here.

from django.contrib import admin
from roster.models import Courses, Student

class CourseAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    #that is a search box

admin.site.register(Courses, CourseAdmin)

class StudentAdmin(admin.ModelAdmin):
    serach_fields = ('name',)
    
admin.site.register(Student, StudentAdmin)