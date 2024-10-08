from django.contrib import admin
from django.urls import path,include
import BookingDetails
import api
import SeatDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('booking/',include('BookingDetails.urls')),
    path('seats/',include('SeatDetails.urls')),#checking seat availability
]
