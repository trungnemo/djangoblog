# djangoblog 
This is a simple blog that developed based on django='3.1.3' and bootstrap4
## Start-up
```bash
#Create a virtual evironment
python -m venv venv_quickdjango
pip install django=3.1.3
#Create a django project
django-admin startproject djangoblog
#Migrate the admin db dashboard
python manage.py migrate
#Create a super user admin
python manage.py createsuperuser
#Create django app: blog
python manage.py startapp blog
```
## Contributing
By [TrungVan](https://www.facebook.com/trungnemo)
## License
[MIT](https://choosealicense.com/licenses/mit/)
