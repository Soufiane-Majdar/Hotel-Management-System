import  datetime
from hotel.models import Room, Booking


def check_availability(room,check_in,check_out):
    avail_list=[]
    Booking_list=Booking.objects.filter(room=room)
    if len(Booking_list)>0:
        for b in Booking_list:
            if b.check_in > check_out or b.check_out < check_in:
                avail_list.append(True)
            else:
                avail_list.append(False)
    else:
        return True


    return all(avail_list)
