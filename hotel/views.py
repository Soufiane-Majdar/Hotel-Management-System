from email import message
from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, FormView, View
from .models import Room,Booking,Contact
from user.models import User
from .forms import AvailabilityForm
from .booking_functions.availability import check_availability
from  django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def RoomListView(request):
    # load Room
    Hotels=Room.objects.all()

    title="Home"


    p =Paginator(Hotels,12)

    #number of pages

    Num_page = request.GET.get('page',1)

    try:
        page = p.page(Num_page)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page= p.page(1)

    

    return render(request,'home/home.html',{'title':title,'Hotels':page})
    

class BookingList(ListView):
    model = Booking

class RoomDetailView(View):
    def get(self, request,*args,**kwargs):
        num=self.kwargs.get('num',None)
        form=AvailabilityForm

        room_list = Room.objects.filter(number=num)

        if len(room_list)>0:
            room= room_list[0]
            context ={
                'room':room,
                'form':form
            }
                
            
            return render(self.request,"hotel/room_detail_view.html",context)
        else:
            return HttpResponse("category do not exist.")

        
 
    def post(self, request,*args,**kwargs):
        if 'USER' in self.request.session:
            num=self.kwargs.get('num',None)
            room_list = Room.objects.filter(number=num)
            form = AvailabilityForm(request.POST)

     

            if form.is_valid():
                data = form.cleaned_data
            available_rooms=[]
            for room in room_list:
                    if check_availability(room,data['check_in'],data['check_out']):
                        available_rooms.append(room)
                
            if len(available_rooms)>0:
                    room=available_rooms[0]
                    booking = Booking.objects.create(
                        user=User.objects.get(email= self.request.session['USER'][4]),### USER session
                        room = room,
                        check_in=data['check_in'],
                        check_out=data['check_out']
                    )
                    booking.save()
                    message=["You have booked this Room successfuly.",'success']
                    if len(room_list)>0:
                        room= room_list[0]
                        context ={
                            'room':room,
                            'form':form,
                            'title':"Booking a Room",
                            'message':message
                        }


                    return render(self.request,"hotel/room_detail_view.html",context)
            else:
                    message=["this rooms is booked.try another time line or deferante category",'Error']
                    if len(room_list)>0:
                        room= room_list[0]
                        context ={
                            'room':room,
                            'form':form,
                            'title':"Booking a Room",
                            'message':message
                        }
                    return render(self.request,"hotel/room_detail_view.html",context)
        else:
            return HttpResponse("login first.")


class BookingView(FormView):
    form_class=AvailabilityForm
    template_name='hotel/availability_form.html'

    def form_valid(self, form):
        if 'USER' in self.request.session:
            data = form.cleaned_data
            print(data)
            room_list = Room.objects.filter(category=data['room_category'])
            available_rooms=[]
            for room in room_list:
                if check_availability(room,data['check_in'],data['check_out']):
                    available_rooms.append(room)
            
            if len(available_rooms)>0:
                room=available_rooms[0]
                booking = Booking.objects.create(
                    user=User.objects.get(email= self.request.session['USER'][4]),### USER session
                    room = room,
                    check_in=data['check_in'],
                    check_out=data['check_out']
                )
                booking.save()
                message=[booking,'success']
                return render(self.request,"hotel/availability_form.html",{'title':"Booking a Room",'message':message})
            else:
                message=["All of this cotegory of rooms are booked.try another time line or deferante category",'Error']
                return render(self.request,"hotel/availability_form.html",{'title':"Booking a Room",'message':message})
        else:
            return HttpResponse("login first.")




def contact(request):
    if(request.POST):
        try:
            title="Contact Posted"

            ### Create object
            c=Contact(name=request.POST['name'],email=request.POST['email'],message=request.POST['message'])
            c.save()
            message=['Your mesage has been submitted  successfully!','success']

            return render(request,"home/contact.html",{'title':title,'message':message})
        except Exception as e:
            message=[e,'Erreur']
            return render(request,"home/contact.html",{'title':title,'message':message})
    else:
        title="Contact"
        return render(request,"home/contact.html",{'title':title})

