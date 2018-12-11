from django.contrib import admin
from django.urls import path

from .views import persons_list, persons_new, persons_update, persons_delete

urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:pk>', persons_update, name="person_update"),
    path('delete/<int:pk>', persons_delete, name="person_delete"),

]