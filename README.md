### Projectsview
### Description
##### Projectsview is a platform where users can display their projects for others to see, they can also  see other peoples Projects with the languages they have used. 
### Author
Alex Muliande


### Screenshot
<img src="https://github.com/alex-muliande/projectsview/blob/master/Screenshot%20from%202019-10-25%2016-39-15.png" width="1000">

### Requirements
##### These are the requirements you need to get the project running locally on your machine:
  - Text Editor
  - Install python3
  - Install and activate virtual
  - Setup Database
  - Install Django

### Installation Process
##### Download any text editor of your choice, either Sublime, Visual-Studio-Code or Atom.
##### Install your preferred version of python
  - ```sudo apt-get install python3.6```.
  - ```python --version``` to confirm that python has been installed.
##### Open the command-line and run the following command to open a directory:
  - ```cd your preferred directory``` => ```cd Desktop```
##### Git clone the project on your current directory by:
  - ```git clone https://github.com/alex-muliande/Projectsview.git```.
##### Open the project on your terminal:
  - ```atom . or code .``` , according to the type of your text editor.
##### Move to your project directory:
  - ```cd Projectsview```.
##### Install virtual environment using python:
  - ```python3.6 -m venv virtual```, check your project to confirm you have a folder called virtual,
  - then activate it by running ```source virtual/bin/activate```
##### To install the packages in the ```requirements.txt file```,
  - ```pip install -r requirements.txt```  That will install all packages including Django.
##### To open python shell:
  - ```python3.6``` ,
  - ```import django```
  - And lastly ```django.get_version()``` to see and confirm the version of django installed.
  - You can then ```ctrl z``` to get out of the shell,
##### After confirming you have all this
  - ```python3 manage.py runserver``` to run the project.
  - Then click the local host link given to open the project on a browser ```http://127.0.0.1:8000/```.


#### For more information read the following django and python documentation:
  - [DjangoDocumentation](https://docs.djangoproject.com/en/1.11/intro/install/)
  - [PythonDocumentation](https://www.python.org/doc/)


### User Stories
##### As a user, I would like to view different Projects that .
##### As a user I would like to View projects overall score
##### As a user I would like to View my profile page
##### As a user I would like to Rate/ review other users' projects
##### As a user I would like Post a project to be rated/reviewed


### Behavior Driven Development
##### The application should display Projects.
##### When a user clicks Review the  project should display apage to review that project.
##### When a user enters a search term on the search input and submits it, then they should be able to get a result of what they are looking for or if the term does not exist, they should get a message to inform them.
##### When a user click view site they should be redirect to a page with the Project of the day.

### Technologies Used
##### Python
##### Django
##### PostgreSQL
##### HTML5
##### CSS3

## Dependencies
##### Postgresql

### Licence
[MIT](LICENSE)

### Contact
##### alexnad425@gmail.com