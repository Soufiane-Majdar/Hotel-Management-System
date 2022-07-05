from django.shortcuts import render,redirect
from .models import User,Erreur


# Create your views here.




############ Logout form Session ############
def logout(request):
    try:
        del request.session['USER']
    except:
        return redirect('login')
    return redirect('home')
############ end Logout form Session ############
 



############ Login to Session ###########
def login(request):
    if 'USER' in request.session:
        return redirect('home')
    else:
        ### Check if the data is Posted 
        if(request.POST):
            ### check if user exists
            check_user=User.objects.filter(email=request.POST['email'],password=request.POST['password'])
            if check_user:
                #print(check_user[0].userName)

                ### Add User to Session
                
                #uname=str(check_user[0].userName)
                request.session['USER'] = {
                    'role':check_user[0].role,
                    'userName':check_user[0].userName,
                    'fName':check_user[0].fName,
                    'lName':check_user[0].lName,
                    'email':check_user[0].email,
                    'img':str(check_user[0].img),
                    'about':check_user[0].about,
                    'adress':check_user[0].adress,
                    }
                #print(check_user[0])
                #print(request.session['USER'][0])
                #request.session['USER']=check_user[1]
                # request.session['fName']=check_user[0].fName
                # request.session['lName']=check_user[0].lName
                # request.session['email']=check_user[0].email

                return redirect('home')
            else:
             # User not found email or psss word incorect:
             title="Login"#
             message=['email or psss word incorect!','danger']
             return render(request,'user/login.html',{'title':title,'message':message})
        ### if it's not Post method
        else:
            title="Login"
            return render(request,'user/login.html',{'title':title})
############ end Login to Session ###########



############ signup : Add user to database ###########
def signup(request):
    if 'user' in request.session:
        return redirect('home')
    else:
        ### Check if the data is Posted
        if(request.POST):

            ### Check if Email alridy exist 
            check_user=User.objects.filter(email=request.POST['email'])
            if check_user:
                    title="signup"
                    message=['Email already exists .']
                    return render(request,"user/signup.html",{'title':title,'message':message})
            else:
                ### Try to push user to database
                try:
                    title="User Created"
                    ### Create object
                    u=User(userName=request.POST['userName'],fName=request.POST['fName'],lName=request.POST['lName'],email=request.POST['email'],password=request.POST['password'],role="client")
                    u.save()
                    message=['Your acount has been created  successfully!','success']

                    return render(request,"user/signup.html",{'title':title,'message':message})

                ### Show an error message
                except Exception as e:

                    ######## add Erreur to tabel Erreurs
                    ###############################################
                    er=Erreur(url="signup : POST",erreur=e)
                    er.save()
                    ###############################################


                    message=['Erreur']
                    return render(request,"user/signup.html",{'title':title,'message':message})

        ### if it's not Post method
        else:
            title="signup"
            return render(request,'user/signup.html',{'title':title})
############ end signup : Add user to database ###########


def profile(request):
    if 'USER' in request.session:
         check_user=User.objects.filter(email=request.session['USER']["email"])
         request.session['USER'] = {
                    'role':check_user[0].role,
                    'userName':check_user[0].userName,
                    'fName':check_user[0].fName,
                    'lName':check_user[0].lName,
                    'email':check_user[0].email,
                    'img':str(check_user[0].img),
                    'about':check_user[0].about,
                    'adress':check_user[0].adress,
                    }
         title="Profile"
         print(request.session['USER'])
         return render(request,'user/profile.html',{'title':title})
    else:
        title="Home"
        return render(request,'home/home.html',{'title':title})


def Host(request):
        title="Host"
        return render(request,'host/becam_host.html',{'title':title})