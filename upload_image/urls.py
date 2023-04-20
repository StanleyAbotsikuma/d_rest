"""django_project URL Configuration

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

from django.urls import path
from .views import test_users,create_users,update_users,delete_user,get_image,update_image

urlpatterns = [
    
   path('',test_users),
   path('create',create_users),
   path('<int:id>',update_users),
   path('delete/<int:id>',delete_user),
   path('images',get_image),
  path('images/<int:id>',update_image),
]
