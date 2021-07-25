"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from main.views import indexHandler, authorsHandler, countrysHandler, bookItemHandler, countryItemHandler, chelseasHandler, booksHandler
from django.views.static import serve
from mysite import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', authorsHandler),
    path('countrys/', countrysHandler),
    path('chelseas/', chelseasHandler),
    path('books/<int:book_id>', bookItemHandler),
    path('countryes/<int:country_id>', countryItemHandler),
    path('bookes/', booksHandler),
    path('', indexHandler),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
