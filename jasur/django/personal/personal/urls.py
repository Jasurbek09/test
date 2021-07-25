"""personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from personal import settings

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('persons/', personsHandler),
    path('about/', aboutHandler),
    path('students/', studentsHandler),
    path('services/', serviceHandler),
    path('services/<int:servis_id>/', serviceitemHandler),
    path('portfolio/', portifolioHandler),
    path('price/', pricingHandler),
    path('blog/', blogHandler),
    path('blog/<int:blog_id>/', blog_singleHandler),
    path('elements/', elementsHandler),
    path('pages/', pagesHandler),
    path('contact/', contactHandler),
    path('', indexHandler),


    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
