🛠 Step 1: Set up your Django project
Install Django (if you haven't already):


pip install django
Create a Django project:


django-admin startproject myproject
cd myproject
Run the server to verify:


python manage.py runserver
Visit http://127.0.0.1:8000/ to confirm it’s working.

🛠 Step 2: Create a Django app
Create an app (say, blog):


python manage.py startapp blog
Add the app to your project settings:

Open myproject/settings.py.

Add 'blog', to the INSTALLED_APPS list.

🛠 Step 3: Define a model (optional - if you want database functionality)
In blog/models.py:


from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

🛠 Step 4: Create and apply migrations (for the database)

python manage.py makemigrations
python manage.py migrate

🛠 Step 5: Create a view (the actual functionality)
In blog/views.py:


from django.http import HttpResponse
from .models import Post

def home(request):
    posts = Post.objects.all()
    post_titles = ', '.join([post.title for post in posts])
    return HttpResponse(f"Posts: {post_titles}")
🛠 Step 6: Map the view to a URL
Create a urls.py inside the blog app (if it doesn’t exist).

In blog/urls.py:


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
Include the app’s urls.py in the main project’s urls.py:

In myproject/urls.py:


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include blog app URLs
]
🛠 Step 7: Run the server and test

python manage.py runserver
Go to http://127.0.0.1:8000/

You should see a list of post titles (even if empty).

🛠 Step 8 (Optional): Create Admin panel for managing posts
In blog/admin.py:


from django.contrib import admin
from .models import Post

admin.site.register(Post)
Create a superuser:


python manage.py createsuperuser
Login at http://127.0.0.1:8000/admin to add/edit posts easily.

✅ Done!
You just created and added a functionality in Django — from project setup ➔ app ➔ model ➔ view ➔ URL ➔ server running!

