from django.shortcuts import render
from ratings.models import Ratings
# Create your views here.
def home(request):
    ratings = Ratings.objects.all()
    sum = 0
    total= 0
    for i in ratings:
        sum+= i.rating
        total+=1
    avg = sum//total    
    op = [1]*avg
    context={'ratings': op}
    return render(request,'home.html',context)

