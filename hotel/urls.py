from django.urls import path
from .views import RoomList,BookingList,BookingView,contact



urlpatterns = [
    path('',RoomList.as_view() ,name="home"),#room_list/
    path('booking_list/',BookingList.as_view() , name="BookingList"),
    path('book/',BookingView.as_view() , name="BookingView"),

    path('contact/',contact, name="contact" ),

]
