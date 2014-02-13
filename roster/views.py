from django.shortcuts import render

#define and object has certain properties associated with it and it brings in other things that
#we need from it , each time we go to home of django then it will return here 
def home (request):
    context = {'message': 'This is a dynamic message variable!'}
    return render(request, "base.html", context)

# Create your views here.
