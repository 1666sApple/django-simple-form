from django.urls import path, include
from basicapp import views

app_name="basicapp"
urlpatterns = [
    path("forms/", views.form_name_view, name='form_name')
    
]