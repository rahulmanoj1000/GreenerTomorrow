from django.shortcuts import render,redirect
from .models import Ratings

def ratings(request):
    if request.method == 'POST':
        rating_value = request.POST.get('rating_value')
        
        # Save the rating to the database
        Ratings.objects.create(rating=rating_value)

        # Redirect or render a response
        return redirect('rating:thanks')  # Redirect to a success page
    return render(request, 'ratings.html')

def thanks(request):
    return render(request,'thankyou.html')