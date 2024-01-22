from django.shortcuts import render,redirect
from .models import Ratings
# Create your views here.
def ratings(request):
    if request.method == 'POST':
        rating_value = request.POST.get('rating_value')
        
        # Assuming you want to save the rating to the database
        Ratings.objects.create(rating=rating_value)

        # Redirect or render a response
        return redirect('rating:thanks')  # Redirect to a success page
        # or return render(request, 'success.html')  # Render a success template

    return render(request, 'ratings.html')

def thanks(request):
    return render(request,'thankyou.html')