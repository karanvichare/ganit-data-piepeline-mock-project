#Create virtual environment
virtualenv env -p python3
source env/bin/activate

#Install and setup airflow
python -m pip install --upgrade pip
pip install apache-airflow
pip install apache-airflow-providers-mysql
pip install sqlalchemy
pip install  pymysql

#Run airflow
#airflow webserver -D &
#airflow scheduler -D &
#airflow worker -D &


#Install and setup django for backend
pip install django
pip install djangorestframework
pip install django-cors-headers

#Create Django Project
#django-admin startproject mockProjectBackend
cd mockProjectBackend

#Create Django Application
#python manage.py startapp chart_api

#Create Models using existing database
#python manage.py inspectdb > chart_api/models.py
#python manage.py makemigrations
#python manage.py migrate

#Run django server
#python manage.py runserver

# Craete Angular App for frontend
# ng new ganit-mock-project && cd ganit-mock-project
npm install -g @angular/cli
npm install chart.js --save

