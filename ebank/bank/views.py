from django.http import HttpResponse
from django.shortcuts import render
from . models import transaction
from . models import team

# Create your views here.
def demo(request):
    # return HttpResponse("hey am here")
    x = transaction.objects.all()
    y = team.objects.all()
    obj = {
        'obj1': x,
        'obj2': y}
    return render(request, "index.html", obj)
    # return render(request,"index.html",{'result':obj})