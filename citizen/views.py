from django.shortcuts import render,redirect
from django.urls import reverse
from .models import CitizenInput
from django.utils import timezone 

# Create your views here.
def citizen_home(request):
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        address = request.POST.get('address')
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))
        current_date = timezone.now().date()
        
        CitizenInput.objects.create(
            name=name,
            email=email,
            image=image,
            address=address,
            latitude=latitude,
            longitude=longitude,
            input_date=current_date 
        )
        return redirect(reverse('citizen:final_citizen'))
    return render(request,'citizen_home.html')

def final_citizens(request):
    return render(request,'final_citizen.html')