# ganit-data-piepeline-mock-project

The Solution is broken down into 3 parts
1> Airflow (airflow-dags Folder)- The airflow dags are written to fetch data from the api and store it in the database
2> Django Backend(mockProjectBackend Folder) - A backend service to fetch data processed in  the data and pass it to the UI
3> UI in Angular(ganit-mock-project-ui Folder) - A UI to display visualizations

Setup file 
Use the setup.txt to install required dependencies

Airflow
Install airflow,update the airflow.cfg to our dags folder and create a mysql connection (refer connection_image in execution_images folder)
Run the fetch data dag to fetch the data and store it in database (Refer dag_exexution image in execution_images folder)

Django
Run the django backend service  (Refer backend_response image in execution_images folder)
cd mockProjectBackend 
python manage.py runserver

Angular
Run the angular project to render UI (Refer UI_visualizations image in execution_images folder)
cd ganit-mock-project-ui
ng serve



