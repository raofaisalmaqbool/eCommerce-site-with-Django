from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from shoppinglyx import settings
from django.views.static import serve
# from django.conf.urls import url
# from account import views
# from account.views import UserRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]