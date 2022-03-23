# Navtech-proj

First we need to create a virtual enviornment.
After creating virtulaenv we need to run -
pip3 install -r requirements.txt

python3 manage.py makemigrations
python3 manage,py migrate

python3 manage.py runserver

------------------------------------------------------------

EndPoint Details -

1 - register/ -
A user need to create an account , for create an account we need some info such as username.first_name, last_name, email and password

2- login/ -
after creating user need to login to the portal for , at the time of login user will get  a token, have to provide the token whenever required.

3-upload_data/ - 
Admin user can upload a csv file which contains product info , if the product is already available then it will update the price column.

4- get_info /
Admin user can see the last 3month reports.
