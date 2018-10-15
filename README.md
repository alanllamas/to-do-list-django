# to-do-list-django

To use this API in a local server follow these instructions

clone the repository

```
git clone https://github.com/alanllamas/to-do-list-django.git
``` 
go to project root
````
cd to-do-list-django
````
create and run virtual env (mac)

````
virtualenv env
source env/bin/activate

````
 install dependencies
 
 ````
 pip3 install -r requirements.txt 
 ````
 go to project folder
 
 ````
 cd to_do
 ````
 
run migrations

````
python3.6 manage.py migrate
````

run server

````
 python3.6 manage.py runserver
````

now you'll be able to use this api locally 

http://localhost:8000/
 
