# Project in brief

### Simple Django Project that helps users submit pics of polluted areas and the appropriate service provider can fix it.

## Key Features:

### User Reporting:

- Users can submit pollution incidents by uploading images and providing optional details.
- The system detects the user's current location using the Google Maps API.
  
### Admin Management:

- Admins receive reported incidents and can assign them to appropriate service providers.
- Admins have the option to add new service providers to the system.

### Service Provider Interaction:

- Assigned service providers receive notifications of reported incidents.
- Service providers can view details of assigned tasks and mark them as complete by uploading images of the remediated area.

### Approval and Notification:

- Admins verify completed tasks and approve them.
- Users receive email notifications upon task approval, informing them of the completed remediation work.

## Technologies Used

- Django
- Sqlite
- Html
- CSS
- Bootstrap 5

## How do I get set up locally?

- Set up venv
  
  -`python -m venv myenv`
  
  -`source myenv/bin/activate`
  
- Clone Repo
  
  -`git clone <repository_url>`
  
- Install dependencies from requirements.txt
  
  -`pip install -r requirements.txt`
  
- Add a .env file in the base directory and add google maps api there
  
  - get it here [https://developers.google.com/maps/documentation/javascript/examples/map-geolocation#maps_map_geolocation-html](https://developers.google.com/maps/documentation/javascript/get-api-key)

- Ensure to add your email details to settings.py file and in middleman/views.py
    
-run `python manage.py makemigrations`

-run `python manage.py migrate`

-run `python manage.py runserver`
