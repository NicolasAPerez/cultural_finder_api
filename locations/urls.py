from django.urls import path

from . import views

app_name = "locations"
urlpatterns = [
    path("", views.LocationAllAPI.as_view()),
    path("<int:pk>/", views.LocationGetAPI.as_view()),
    path("city/<str:city>/", views.LocationCityAPI.as_view()),
    path("rating/", views.RatingAPI.as_view())
]