from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    pid = models.CharField(unique=True, max_length=12)
    grade = models.IntegerField(unique=False, null=True, max_length=3)
    age = models.IntegerField(unique=False, null=True, max_length=2)
    classrank = models.IntegerField(unique=False, null=True, max_length=4)
    gradyear = models.IntegerField(unique=False, null=True, max_length=4)
    hometown = models.CharField(max_length=50)
    
    #have to have a grade no matter what but you won't have a grade your first day
    
    #imageurl = models.ImageField(max_length =100)
    #score would have been better name
    
    class Meta(object):
        ordering = ('pid', 'name')
        
    def __unicode__(self):
        return U'%s %s' %(self.name, self.pid)


class Courses(models.Model):
    name = models.CharField(unique=True, max_length=50)
    callnumber = models.CharField(unique=False, max_length=4)
    instructor = models.CharField(max_length=50)
    #could have a model for course/student and instructor
    description = models.CharField(max_length=200)
    term = models.CharField(max_length=50)
    student = models.ManyToManyField(Student)
    date = models.DateField()
    #remember to import the datefield
    
    class Meta(object):
        verbose_name_plural = "Courses"
        ordering = ('-date', 'name')
    
    def __unicode__(self):
        return U'%s | %s' %(self.callnumber, self.name)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Course, self).save(*args, **kwargs)
        
    #could be a TextField if you wanted, if you didn't care how man


