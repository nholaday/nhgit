Django Application - an app that performs a particular function for the full web application like a registration app, polling app, comments app.
Pluggable Application - apps can be reused or shared and plugged into different full web application 

__init.py__ - Just tells python that this is a module
admin.py - register your models here.  Makes the automatic django admin interface.
apps.py - application specific config
models.py - stores data models. Entities and relationships to the data
tests.py - store functions to test code
views.py - Handles requests and returns responses

migrations - database specific information as it relates to the models


1. Create project
django-admin startproject <<project name>>
2. Create app
python manage.py startapp <<app name>>
3. Add app name to settings.py in project in INSTALLED_APPS
4. Create views in views.py
from django.http import HttpResponse
def index(request):
    return HttpResponse("Here it is")
Every view should have a response in it
4. Edit urls.py in the project to have the created view
from first_app import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
This maps that applications view to that url (in this case just the IP address with no extension)

5. Change url pattern to include('app_name.urls') instead of specifically call a view to make a more generic url mapping.
    from django.conf.urls import include
    url(r'^app_name/',include('app_name.urls')),
5a. Then create a urls.py file in the app_name folder and all urls in there will use the extension app_name

6. Templates - Create an html template to insert Django snippets into: templates/ directory in the project directory
6a. Create a TEMPLATE_DIR in settings.py
    TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")
    DIRS: [TEMPLATE_DIR],
6b. Create an html file in the templates directory.  Use `{{ insert_me }}` for django injections
6b. Change the views.py file to render the inserted code
    my_dict = {'insert_me':'This was inserted from views.py yo!'}
    return render(request, 'first_app/index.html',context=my_dict)
6c. Relative urls with template tags
Create a variable called app_name='basicapp' in urls.py
    url(r'^$', views.blog_index, name='blog index')
Call the url name with <a class="nav-link" href="{% url "blogapp:blog index" %}">Blog</a>
    use url "index" and url "admin:index" as shortcuts to those two
6d. Make a base template and Extensions
    {% block body_block %}
    {% endblock %}
In the extension
<!DOCTYPE html>
{% extends "blogapp/base.html" %}
and call {% block body_block %} again with the extended code
6e. Template Filters - optionally pipe injections to django filters.  Custom filters are possible, found in templatetags/
    {{ text_inject|upper }}
    {{ num_inject|add:10 }}

7. Static files
    - Create 'static/' directory under proj.
    - Modify settings.py with a STATIC_URL
    - Make STATICFILES_DIRS = [] and list paths
    - Reference those static files in a template by injecting with 
        {% load staticfiles %}
        <img src="{% static "IMG_0118.jpg" %}">
7a. Getting static files from the user
    - in settings.py make MEDIA_ROOT = MEDIA_DIR #MEDIA_DIR = os.path.join(BASE_DIR,"media")
        MEDIA_URL = '/media/'
    - Make a media/ directory and media/profile_pics
    - profile_pic = models.ImageField(upload_to="profile_pics", blank=True)
    - activate venv and pip install pillow
    - in views.py access with request.FILES['profile_pic']
        if 'profile_pic' in request.FILES:
            upi.profile_pic = request.FILES['profile_pic']

8. Models
8a. Create classes inheriting from Model.models
class Topic(Model.models):
    topicname = models.CharField(max_length=264, unique=True)
8b. Set foreign keys to link other models. Use str() function to define name.
class Webpage(Model.models):
    topic = models.ForeignKey(Topic)
    url = models.URLfield()
    def __str__(self):
        return self.url
8c. Register models in django admin
    from fourth_proj.LunaApp.models import Person, FavFood, Age
    admin.site.register(Person)
8d. Create superuser
    python manage.py createsuperuser (nic, lunabuna)
8e. If necessary create fake data using Faker library in a script.
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
import django
django.setup()
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker
Topic.objects.get_or_create(top_name=random.choice(topics))[0]

9. MTV (Model Template View) - Putting it all together
9a. Import models into the view.  
    from first_app.models import Topic
9b. Query the model in the view
    ar_list = AccessRecord.objects.filter().order_by('date')
    ar_dict = {'Access Record': arlist}
9c. Then you will be able to inject contect from the models into the Template.
    return render(request, 'first_app/index.html', context=ar_dict)
9d. Use pseudo-python code to loop through your data and display
    {% for acc in access_records %}
    <tr> {{ acc.name }} </tr>
    {% endfor %}

10. Forms
10a. Create forms.py in app
10b. Make forms like models```
from django import forms
class FormName(forms.Form):
    name = form.CharField()```
10c. import forms into views.py and make a view```
from forms import FormName
def new_form_view(request):
    f = FormName()
    return render(request,'form_name.html',{'form':f})```
10d. Add form view to urls.py
10e. Make a form_name.html file in templates/
<div class="container">
    <form method="POST">
        {{ form.as_p }} // inject form as <p>
        {% csrf_token %} // security token
        <input type="submit" class="btn btn-primary" value="Submit">
    </form>
</div>
10f. Get the data back in the view
if request.method == "POST":
    f = FormName(request.POST)
    if f.is_valid():
        print("Name" + form.cleaned_data['name'])
return render(request,'form_name.html',{'form':f})
10g. Add validators for form fields if necessary
from django.core import validators
class FormName(forms.Form):
    name = form.CharField(
        validators=[validators.MaxLengthValidator(5)]
    )
10h. To put data directly into a model use forms.ModelForm
from django import forms
from myapp.models import MyModel
class NewForm(forms.ModelForm):
    class Meta:          #Connects model to form
        model = MyModel
        fields = "__all__" #grabs all fields from the model and puts in the form
        fields = ("field1", "field2")
        #or# exclude = ["field1", "field2"]
Then in views.py just use modelinstance.save() to save the form data
*How do you make imported ModelForms look nice?*
To modify singular fields/widgets ModelForms, configure the widgets variable under the Meta class
        widgets = {
            # this class referring to a css class to apply to the widget
            'field1':TextInput(attrs={'class':'textinputclass'}),
            # can apply multiple classes separated by spaces
            'field2':Textarea(attrs={'class':'class1 class2'})
        }

11. Passwords
11a. Add 2 apps to INSTALLED_APPS list in settings.py
    "django.contrib.auth", "django.contrib.contenttypes"
11b. pip install bcrypt django[argon2]
    Hashes (e.g. SHA-256) take a string and build a hash from it.  It's almost impossible to get back to the string from the hash, but the same string will produce the same hash every time.
11c. Add password hashers to settings.py
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher,
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher,
    'django.contrib.auth.hashers.BCrpytPasswordHasher,
    'django.contrib.auth.hashers.Argon2PasswordHasher,
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher,
]

12. User Models - to extend built in User model make another model with a OneToOne relationship
from django.contrib.auth.models import User
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
12a. Make the forms in forms.py
from django.contrib.auth.models import User
from usersapp.models import UserProfileInfo
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username", "email", "password")
class UserProfileInfoForm(models.Model):
    class Meta():
        model = UserProfileInfo
12b. Add to django admin
12c. Save the User data and hash the password in views.py
def user_view():
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        upi_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and upi_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) #Uses settings.py and hashes password
            user.save()
            upi = upi_form.save(commit=False) #Set commit=False to avoid overwriting linked User instance
            upi.user = user #Set user OneToOne relationship equal to the user instance we just saved
            upi.save()

13. Logins
- In settings.py
    LOGIN_URL = '/baseapp/user_login'
- In views.py
    from django.contrib.auth import authenticate, login, logout
    from django.http import HttpResponseRedirect
    from django.core.urlresolver import reverse
    from django.contrib.auth.decorators import login_required
    def user_login(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password) //django built in auth
        if user:
            if user.is_active:
                login(request,user)  //django built in login
                return HttpResponseRedirect(reverse('index'))
            else:
            ...
    @login_required
    def user_logout(request):
        logout(request) //django built in logout
        return HttpResponseRedirect(reverse('index'))
- In the html template
    {% if user.is_authenticated %} //attribute of user is set with authenticate line in views
        <li><a class='navbar-link' href="{{ url 'user_logout' }}">Logout</a></li>
    {% else %}
        <li><a class='navbar-link' href="{{ url 'baseapp:user_login }}>Login</a></li>
    {% endif %}
- In login.html, make form
    <form action="{% url 'baseapp:user_login' %}" method="POST">
        {% csrf_token %}
        <label for="username">Username</label>
        <input type="text" name="username" placeholder="Enter Username">
- In urls.py, add urls

14. Mixins
In views.py, for class based views, instead of a decorator @login_required use a Mixin
from django.contrib.auth.mixins import LoginRequiredMixin

 

# General project building cycle:
MTV Model Template View Architecture:

Each page the user visits will be listed in urls.py
That url will link to a View in views.py
That view gets/posts data to a model in models.py
That view gets its html from templates

Another process could look like:
Create a Model, Model Forms if necessary
Create Views for each model
For every View connect a URL in urls.py

# Changing Models and Migrations
- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes.  These are actual files that get created in the migrations directory
- Run python manage.py migrate <<optional app name>> to apply those changes to the database.
If you database gets to a situation where it doesn't match up with your models, you can unmigrate everything with
$ python manage.py migrate zero
- python manage.py showmigrations

at Introducing the Django Admin¶ in first Django App part 2
# Django Admin
- python manage.py createsuperuser
- Go to localhost:8000/admin
- Edit admin.py to include the Question model, then 
- admin.site.register(Question)
# Tests
- Edit tests.py, add a class for a model that inherits from TestCase
- Make a function for each thing you want to test, the name of the function should start with the word 'test'.  Inside the function, make an instance of the model and variables just like you would in a shell but at the end use self.assertIs(instance_of_model.function_to_test(), True/False)
- Run python manage.py test <<app name>>
Speed up testing using the -k option
The tests file consists of creating instances of models then running code against them.  After, ensure they're correct using `assert` commands:
j = TagPointsFromList.objects.create(box=self.j.box)
self.assertEquals(j.job_status, "COMPLETE")
# Queries
You can filter objects of a model using queries.  These queries can be chained.
Device.object.filter(name__regex='hello').exclude(building__startswith='fake)
Adding queries -- q1 | q2
None query -- Device.objects.none()
