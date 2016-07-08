"""gitrec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.homepage, name='homepage'),
    url(r'^reviews$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /repo/
    url(r'^repo$', views.repo_list, name='repo_list'),
    # ex: /repo/5/
    url(r'^repo/(?P<wine_id>[0-9]+)/$', views.repo_detail, name='repo_detail'),
    url(r'^wine/(?P<wine_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    # ex: /review/user - get reviews for the logged user
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),
    url(r'users/(?P<username>\w+)/$',views.UserProfileDetailView, name='profile'),
    #url(r'users/(?P<profile_id>\w+)/$',views.UserProfileDetailView.as_view(), name='profile'),
]