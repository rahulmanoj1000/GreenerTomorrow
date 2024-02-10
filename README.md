# Project in brief

### Simple Django Project that helps citizens submit pics of polluted areas and the appropriate authorities can fix it.

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
