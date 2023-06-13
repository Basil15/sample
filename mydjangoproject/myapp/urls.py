
from django.contrib import admin
from django.urls import path

from mydjangoproject.myapp.views import UserProfileCreateView, UserProfileUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', UserProfileCreateView.as_view(), name='profile-create'),
    path('profiles/<int:pk>/', UserProfileUpdateView.as_view(), name='profile-update'),

]
