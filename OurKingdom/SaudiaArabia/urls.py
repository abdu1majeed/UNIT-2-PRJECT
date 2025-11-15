from django.urls import path
from . import views

app_name = "SaudiaArabia"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("history/", views.history_page, name="history_page"),
    path("culture/", views.culture_page, name="culture_page"),
    path("tourism/", views.tourism_page, name="tourism_page"),
    path("education/", views.education_page, name="education_page"),
    path("manufacturing/", views.manufacturing_page, name="manufacturing_page"),
    path("vision/", views.vision_page, name="vision_page"),
    
    path("theme/toggle/", views.toggle_theme, name="toggle_theme"),
    path("theme/set/<str:mode>/", views.set_theme, name="set_theme"),
]