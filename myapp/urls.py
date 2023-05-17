from django.template.defaulttags import url
from django.urls import include, path
from myapp import views
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('delete/', views.delete_view, name='delete'),
    path('accounts/', include('two_factor.urls', namespace = 'two_factor')),
    url(r'', include(tf_urls)),
]