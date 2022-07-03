from django.urls import path
from .views import RoomListView,BookingList,BookingView,RoomDetailView,contact



urlpatterns = [
    path('',RoomListView.as_view() ,name="home"),#room_list/
    path('booking_list/',BookingList.as_view() , name="BookingList"),
    path('book/',BookingView.as_view() , name="BookingView"),
    path('room/<category>',RoomDetailView.as_view() , name="RoomDetailView"),

    path('contact/',contact, name="contact" ),

]
