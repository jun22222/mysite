"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

   # ???

urlpatterns = [
    path('add_question', views.add_question),
    path('data', views.data),
    # path('', admin.site.urls),
    path('', views.index),
       # polls만 입력받으면 일로 넘어옴
       #    views로 ㄱㄱ

    # viee
    path('<int:id>', views.detail, name='detail'),
    path('vote/', views.vote, name = 'vote'),
    path('input',views.input),

]
