"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hello import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', views.login_view,name='login'),
    url(r'^logout', views.logout_view),
    url(r'^testdb$', views.testdb,name='testdb'),
    url(r'^nologin$', views.nologin,name='nologin'),

    url(r'^report$', views.report,name='report'),
    url(r'^add_report$', views.add_report,name='add_report'),
    url(r'^h_report$', views.h_report,name='h_report'),
    url(r'^del_report$', views.del_report,name='del_report'),
    url(r'^mod_report$', views.mod_report,name='mod_report'),
    url(r'^xlwt_report$', views.xlwt_report,name='xlwt_report'),

    url(r'^card$', views.card,name='card'),
    url(r'^add_card$', views.add_card,name='add_card'),
    url(r'^h_card$', views.h_card,name='h_card'),
    url(r'^del_card$', views.del_card,name='del_card'),
    url(r'^mod_card$', views.mod_card,name='mod_card'),
    url(r'^xlwt_card$', views.xlwt_card,name='xlwt_card'),

    url(r'^setbet$', views.setbet,name='setbet'),
    url(r'^add_setbet$', views.add_setbet,name='add_setbet'),
    url(r'^h_setbet$', views.h_setbet,name='h_setbet'),
    url(r'^del_setbet$', views.del_setbet,name='del_setbet'),
    url(r'^mod_setbet$', views.mod_setbet,name='mod_setbet'),
    url(r'^xlwt_setbet$', views.xlwt_setbet,name='xlwt_setbet'),

    url(r'^retained$', views.retained,name='retained'),
    url(r'^add_retained$', views.add_retained,name='add_retained'),
    url(r'^h_retained$', views.h_retained,name='h_retained'),
    url(r'^del_retained$', views.del_retained,name='del_retained'),
    url(r'^mod_retained$', views.mod_retained,name='mod_retained'),
    url(r'^xlwt_retained$', views.xlwt_retained,name='xlwt_retained'),

    url(r'^notice$', views.notice,name='notice'),
    url(r'^add_notice$', views.add_notice,name='add_notice'),
    url(r'^h_notice$', views.h_notice,name='h_notice'),
    url(r'^del_notice$', views.del_notice,name='del_notice'),
    url(r'^mod_notice$', views.mod_notice,name='mod_notice'),
    url(r'^xlwt_notice$', views.xlwt_notice,name='xlwt_notice'),
]
