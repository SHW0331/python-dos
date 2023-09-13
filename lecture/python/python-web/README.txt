# pip install django
# django-admin startproject [projectname]
# cd [projectname]
# python manage.py startapp [appname]

# add [appname] to settings.py
INSTALLED_APPS = [
    ...
    '[appname].apps.[apps.py class name]',
    ...
]

# models.py

#app urls include
urlpatterns = [
    path('', views.index, name='index'),
]

#project ruls include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# run server
python manage.py runserver