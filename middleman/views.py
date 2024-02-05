import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from citizen.models import CitizenInput
from .models import Progress,WorkMan,Completed,Pre_completed
from .forms import WorkManRegisterForm,WorkManLogin
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail, EmailMessage

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            workman = WorkMan.objects.get(name=username)
        except WorkMan.DoesNotExist:
            workman = None

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if workman:                                         #Since same login for admin and workman redirect to the right page depending on the person
                return redirect('middleman:workman_panel')
            return redirect('middleman:panel')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('middleman:login')
    return render(request, 'login.html')

def logout(request):                                            #Handle logout fuction
    auth.logout(request)
    messages.error(request, 'You were logged out') 
    return redirect('middleman:login')

def add_workman(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        WorkMan.objects.create(name=username,password=password)
        user = User.objects.create_user(username=username,password=password)
        user.save()
        return redirect('middleman:panel')
    return render(request,'workman_register.html')

def panel(request):
    entered_data = CitizenInput.objects.all()
    progress_data = Progress.objects.all()
    complete_data = Completed.objects.all()
    pre_complete = Pre_completed.objects.all()
    context = {
        'entered_data': entered_data,
        'progress_data': progress_data,
        'complete_data': complete_data,
        'pre_complete' :pre_complete
    }
    return render(request,'panel.html',context)



def proceed(request, citizen_id):
    try:
        # Retrieve the CitizenInput record
        citizen = CitizenInput.objects.get(pk=citizen_id)

        # Create a Progress record and copy data
        Progress.objects.create(
            name=citizen.name,
            email=citizen.email,
            image=citizen.image,
            address=citizen.address,
            latitude=citizen.latitude,
            longitude=citizen.longitude,
            input_date=citizen.input_date
        )

        # Delete the CitizenInput record
        citizen.delete()

        return redirect('middleman:panel')  # Redirect to the original page
    except CitizenInput.DoesNotExist:
        # Handle the case where the CitizenInput record doesn't exist
        return render(request, 'error_template.html', {'error_message': 'CitizenInput record not found'})


def workman_panel(request):
    progress_data = Progress.objects.all()
    context={'progress_data':progress_data}
    return render(request,'workman_panel.html',context)

def completed(request, citizen_id):
    if request.method == "POST":
        image = request.FILES.get('image')
        worker_complete = Progress.objects.get(pk=citizen_id) #This gets the data that was submitted by the worker
        temp = Pre_completed.objects.create(
            name=worker_complete.name,
            email=worker_complete.email,
            image=worker_complete.image,
            address=worker_complete.address,
            latitude=worker_complete.latitude,
            longitude=worker_complete.longitude,
            input_date=worker_complete.input_date
        )
        Completed.objects.create(sent_id=temp.id,image = image)
        worker_complete.delete()                        #Deletes the data that was submitted by the worker
        return redirect('middleman:workman_panel')
    return render(request, 'completed.html', {'citizen_id': citizen_id})

def deleting(request, id):                  #This clears the data from the db and sends an email to the user(citizen) stating work complete
    if id:
        complete_data = Completed.objects.get(pk=id)
        pre_complete = Pre_completed.objects.get(pk=complete_data.sent_id)
        ##Note to who ever it concers. This method is slightly different from what we have been taught in class.
        mail = EmailMessage(
        'Pollution Report',
        f'The location you reported on {pre_complete.input_date} with regards to pollution/littering has been cleared. A picture post-clearance has been attached for your reference. Please feel free to drop a review at http://127.0.0.1:8000/rating/ratings/', #change if not local host
        'rahulmanoj1000@gmail.com',  # Sender's email address
        [pre_complete.email, 'rahulmanoj1200@gmail.com'],  # Recipient list
        )
        image_path = os.path.join(settings.BASE_DIR, 'media', complete_data.image.name)
        mail.attach_file(image_path, mimetype='image/jpeg')
        mail.send()         
        pre_complete.delete()
        complete_data.delete()
        return redirect('middleman:panel')
    return render(request, 'deleting.html')