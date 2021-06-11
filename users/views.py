from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Shipping
from django.contrib import messages, auth
from django.core.mail import send_mail
from django.conf import settings
import logging

# Create your views here.

logger = logging.getLogger('django')


# ====================================================================================
# login(), will check the inserted details from Login form with the database data
# if details entered matched the database data
# a session will create and user will redirect to the dashboard
# if details doesn't match, will redirect to the login page
# ====================================================================================

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if Customer.objects.filter(cust_uname=username, cust_password=password):
            request.session['cust'] = username
            logger.info('session created and login successful')
            return redirect('dashboard')
        else:
            logger.info('Invalid Credentials')
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


# ================================================================================
# logout() it will delete the session and redirect to login page
# ================================================================================

def logout(request):
    try:
        del request.session['cust']
        logger.info('session terminated and logout successful')
    except:
        return redirect('login')
    return redirect('login')


# ================================================================================
# customer() open the register.html page
# ================================================================================

def customer(request):
    return render(request, 'register.html');


# ================================================================================
# register() this will take the data from html page(register.html)
# insert the data into the database and store the details
# will also verify the username or email already exists in the database or not
# if already exists it will redirect to the registered page and show the message
#   that username or email already registered
# password and confirm password field will be verified that both are same or not
# the registered email will get an email that Welcome to FASHION HUB
# ================================================================================

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        phone_no = request.POST['phoneno']

        if password == confirm_password:
            if Customer.objects.filter(cust_uname=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('/custregister')
            elif Customer.objects.filter(cust_email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('/custregister')
            elif len(password)<5:
                messages.info(request, 'Password length should be more than 5')
                return redirect('/custregister')
            else:
                cust = Customer(cust_uname=username, cust_phone=phone_no, cust_password=password, cust_email=email,
                                cust_fname=first_name, cust_lname=last_name)
                cust.save()
                print('user created')
                logger.info('user registered')
                send_mail("Welcome to FASHION HUB", f"Thankyou {username} for joining the FASHION HUB",
                          settings.EMAIL_HOST_USER,
                          [email])

                return redirect('login')
        else:
            logger.info('Password not matched')
            messages.info(request, 'Password not matching')
            return redirect('/custregister')
    else:
        return redirect('register.html')


# ================================================================================
# dashboard() if session is running, only then this will redirect to dashboard.html
# if session is terminated, then it will redirect to the login page
# ================================================================================

def dashboard(request):
    if 'cust' in request.session:
        current_user = request.session['cust']
        param = {'current_user': current_user}
        return render(request, 'dashboard.html', param)
    else:
        return redirect('login')


# ================================================================================
# shipping() it will store the shipping details
# it will take the input from dashboard.html
# store the given data in database
# ================================================================================

def shipping(request):
    if 'cust' in request.session:
        if request.method == 'POST':
            current_user = request.session['cust']
            cust = Customer.objects.get(cust_uname=current_user)
            shipfname = request.POST['first_name']
            shiplname = request.POST['last_name']
            shipphoneno = request.POST['phoneno']
            shipaddress = request.POST['address']
            print(cust, shipfname, shiplname, shipaddress, shipphoneno)
            ship = Shipping(ship_uname=cust, ship_fname=shipfname, ship_lname=shiplname, ship_phone=shipphoneno,
                            ship_address=shipaddress)
            ship.save()
            logger.info('Shipping details saved')
            return redirect('profile')
        else:
            return redirect('dashboard')
    else:
        return redirect('login')


# ================================================================================
# profile() if session is running it will open the custprofile.html
# it will show all the details in the custprofile.html
# if session is terminated, it will redirect to the login
# ================================================================================

def Profile(request):
    if 'cust' in request.session:
        prof = []
        current_user = request.session['cust']
        cust = Customer.objects.get(cust_uname=current_user)
        for object in Shipping.objects.filter(ship_uname_id=cust.id):
            prof.append(object)
            print(object)
        return render(request, 'custprofile.html', {'prof': prof})

    else:
        return redirect('login')


# ================================================================================
# destroy() it will delete the shipping detail of the select ID
# ID will be select from the html page
# ================================================================================

def custdestroy(request, id):
    ship = Shipping.objects.get(id=id)
    ship.delete()
    logger.info('Delete Successful')
    return redirect('profile')


# ================================================================================
# edit() it will redirect to the edit page
# edit page form field would be autofilled with the details of selected ID
# changes can be done there and can edit the details in form
# ================================================================================

def custedit(request, id):
    ship = Shipping.objects.get(id=id)
    logger.info('Redirect to edit page with ID')
    return render(request, 'editsomnath.html', {'ship': ship})


# ================================================================================
# update() it will update the details as filled in edit.html
# will redirect to the custprofile.html and reflect the changes
# ================================================================================

def custupdate(request, id):
    shipfname = request.POST['first_name']
    shiplname = request.POST['last_name']
    shipphoneno = request.POST['phoneno']
    shipaddress = request.POST['address']
    print(shipfname, shiplname, shipaddress, shipphoneno)
    ship = Shipping(id=id, ship_fname=shipfname, ship_lname=shiplname, ship_phone=shipphoneno, ship_address=shipaddress)
    ship.save()
    logger.info('Update successful')
    return redirect('profile')


# ================================================================================
# home() will redirect to the home page of the project which is the landing page,
# home.html
# ================================================================================

def home(request):
    return render(request, 'home.html')


# ================================================================================
# custadmin() it will verify the admin login with the given admin credentials,
# if, the credentials match and verified the session will start and admin will
# redirect to the custadmin.html page, where admin can delete the users.
# ================================================================================

def custadmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'somnath' and password == 'admin':
            request.session['adminlogin'] = username
            return redirect('adminhome')

        else:
            return render(request, 'adminuser.html')
    else:
        return render(request, 'adminuser.html')


# ================================================================================
# adminlogout() it will delete the session, and redirect to the adminlogin,
# which is, adminuser.html
# ================================================================================


def adminlogout(request):
    try:
        del request.session['adminlogin']
        logger.info('session terminated and logout successful')
    except:
        return redirect('custadmin')
    return redirect('custadmin')


# ================================================================================
# adminhome() it will check if the session is there, admin will redirect to,
# custadmin.html, else redirect to the admin login page.
# ================================================================================

def adminhome(request):
    if 'adminlogin' in request.session:
        admincust = Customer.objects.all()
        logger.info('Redirect to custadmin.html')
        return render(request, 'custadmin.html', {'admincust': admincust})

    else:
        return redirect('custadmin')


# ================================================================================
# admindelete() it will take the 'id' of the selected customer details, and
# delete the data from the database, means, the user is deleted, and have to
# register if user want to login again.
# ================================================================================

def admindelete(request, id):
    if 'adminlogin' in request.session:
        admindel = Customer.objects.get(id=id)
        admindel.delete()
        logger.info('Delete Successful')
        return redirect('adminhome')
    else:
        return redirect('custadmin')
