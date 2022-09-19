# AppCompanion

This is a Python + React Web App
Powered by Django in the backend.

Installation:
Create Virutal Env for the project and start installing the below mentioned packages.

Django:
pip install djangorestframework
pip install django-cors-headers

Postges:
pip install psycopg2

Conda:
conda create --name env_name (Eg: travel-comp-app)
conda activate env_name

Installtion Packages:
conda install django djangorestframework
conda install -c conda-forge django-cors-headers
conda install -c anaconda psycopg2

In settings.py at the parent level of the application:

```js
DATABASES = {
  default: {
    ENGINE: "django.db.backends.postgresql",
    NAME: "sampledb",
    USER: "postgres",
    PASSWORD: "samplepassword",
    HOST: "127.0.0.1",
    PORT: "5432",
  },
};
```

Make sure to create/modify your databases like how it is in TravelCompProject/settings.py

Run Application:

- Delete the Migration folder from the application i.e. `travelcompapp/migrations`
- Run this command from the Parent Folder: `python manage.py makemigrations travelcompapp`
  - Output after Running the above command:
  - - Migrations for 'travelcompapp':
      `travelcompapp/migrations/0001_initial.py - Create model UserDetails`
- - Run this command to migrate the DB: `python manage.py migrate travelcompapp`
    - Output:
      - Operations to perform:
        - Apply all migrations: travelcompapp
      - Running migrations:
        - Applying travelcompapp.0001_initial... OK
- Run this command to migrate the DB: `python manage.py migrate`
  - Output:
    - This Above command migrates the Admin, Auth part of the app.
- To Run the server: `python manage.py runserver 8080` # localhost server will run on 8080

Test the application from PostMan:

`http://localhost:8080/api/getuserlist`
