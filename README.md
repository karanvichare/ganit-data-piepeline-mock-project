# ganit-data-piepeline-mock-project

<p class="has-line-data" data-line-start="0" data-line-end="1">The Solution is broken down into 3 parts</p>
<p class="has-line-data" data-line-start="2" data-line-end="5">1&gt; Airflow (airflow-dags Folder)- The airflow dags are written to fetch data from the api and store it in the database<br>
2&gt; Django Backend(mockProjectBackend Folder) - A backend service to fetch data processed in the data and pass it to the UI<br>
3&gt; UI in Angular(ganit-mock-project-ui Folder) - A UI to display visualizations</p>
<p class="has-line-data" data-line-start="6" data-line-end="8">Setup file<br>
Use the setup.txt to install required dependencies</p>
<p class="has-line-data" data-line-start="9" data-line-end="12">Airflow<br>
Install airflow,update the airflow.cfg to our dags folder and create a mysql connection (refer connection_image in execution_images folder)<br>
Run the fetch data dag to fetch the data and store it in database (Refer dag_exexution image in execution_images folder)</p>
<p class="has-line-data" data-line-start="13" data-line-end="17">Django<br>
Run the django backend service (Refer backend_response image in execution_images folder)<br>
cd mockProjectBackend<br>
python <a href="http://manage.py">manage.py</a> runserver</p>
<p class="has-line-data" data-line-start="18" data-line-end="22">Angular<br>
Run the angular project to render UI (Refer UI_visualizations image in execution_images folder)<br>
cd ganit-mock-project-ui<br>
ng serve</p>


