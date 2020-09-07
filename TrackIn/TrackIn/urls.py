"""TrackIn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from . import signup, signin, commodity, create_commodities
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signup/$', signup.SignupUser.as_view(), name='signup'),
    url(r'^login/$', signin.LoginUser.as_view(), name='login'),
    url(r'^get_commodities_details/$', commodity.GetCommoditiesDetails.as_view(), name='GetCommoditiesDetails'),
    url(r'^get_commodities_list/$', commodity.GetCommoditiesList.as_view(), name='GetCommoditiesList'),
    url(r'^create_commodities/$', create_commodities.CreateCommodities.as_view(), name='CreateCommodities'),
]
