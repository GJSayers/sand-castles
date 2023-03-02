from django.urls import path
from members import views

urlpatterns = [
    path('members/', views.ProfileList.as_view()),
]