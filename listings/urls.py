from django.urls import path
from listings import views

urlpatterns = [
    path('', views.ListingsList.as_view()),
    path('listing/<int:pk>', views.ListingDetail.as_view())
]
