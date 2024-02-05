from django.conf import settings
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import CitizenInput
from django.utils import timezone
from django.contrib import messages 

# Create your views here.
def citizen_home(request):
    google_maps_api_key = settings.GOOGLE_MAPS_API_KEY   # Google maps API key is retreived from .env file through settings.py
    context = {'GOOGLE_MAPS_API_KEY':google_maps_api_key} #This will be used in the template
    
    try:
        if request.method == 'POST':
            # Extract data from the POST request
            name = request.POST.get('name')
            email = request.POST.get('email')
            image = request.FILES.get('image')
            address = request.POST.get('address')
            latitude = float(request.POST.get('latitude'))
            longitude = float(request.POST.get('longitude'))
            current_date = timezone.now().date()
            
            #Writing the data obtained from POST to the database
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
    except: #This exception is just to handle the case where the user doesnt click the location button
        messages.error(request, 'Please select a location by clicking the "Pan to current location" button')
        return render(request,'citizen_home.html',context)
    return render(request,'citizen_home.html',context)

def final_citizens(request): # This is rendered after user submits their data
    return render(request,'final_citizen.html')