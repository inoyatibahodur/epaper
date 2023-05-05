from django.urls import path

from .views import ProductView

# app_name will help us do a reverse look-up latter.
app_name = "productes"

urlpatterns = [
    path('productes/', ProductView.as_view()),
]


