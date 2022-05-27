from django.contrib import admin
from django.urls import path, include
# from account import views
# from account.views import UserRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
