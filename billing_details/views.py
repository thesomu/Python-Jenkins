from django.http import request
from django.shortcuts import redirect, render
from datetime import datetime
from billing_details.models import billing,Salary
from django.contrib import messages
import logging
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
logger = logging.getLogger('django')
         
 #inserting credit card values   
def billing_view(request):
   if request.method =="POST":
       logger.info(" credit card data inserted")
       fname = request.POST['fullname']
       emailid = request.POST['emailid']
       address = request.POST['address'] 
       city = request.POST['city'] 
       state = request.POST['state']
       zip = request.POST['zip'] 
       cardname = request.POST['cardname'] 
       cardnumber = request.POST['cardnumber'] 
       expiry_month = request.POST['expiry_month']
       expiry_year = request.POST['expiry_year']
       cvv = request.POST['cvv']  
       bill=billing(fullname=fname,emailid=emailid,address=address,city=city,state=state,zip=zip,cardname=cardname,cardnumber=cardnumber,expiry_month=expiry_month,expiry_year=expiry_year,cvv=cvv)
       bill.save()

       return render(request,'homejai.html')

   else:
        return render(request,'index.html')       

#showing credit card value
def show(request):
     logger.info("showing credit card details")
     
     bill=billing.objects.all()
     return render(request,'showdata.html',{'bills': bill})
#deleting credit card details
def destroy(request, id):  
    employee = billing.objects.get(id=id)  
    employee.delete()  
    return redirect("/billing/")  
#login function with session
def loginjai(request):
    
    if request.method =="POST":
        
        logger.info('Accounts  login successful')
        username=request.POST['username']
        password=request.POST['password']
        if(username=="jai" and password=="123"):
            request.session['loginjai'] = username
            print("login")
            return redirect('dashboardjai/')
        else:
           messages.error(request, 'Invalid Credentials')
           logger.error('Accounts login fails')
           return render(request,'loginjai.html')
    else:
        return render(request,'loginjai.html')  
#showing all the fuctionalities
def dashboard(request):
    
    if 'loginjai' in request.session:
        print("dashboard")
        name = request.session['loginjai']
        logger.info('Accounts session started')
        
        return render(request, "homejai.html", {'name': name})
    else:
        messages.error(request, 'Login first')
        logger.warning('Wrong session')
        #messages.error(request, 'Login first')
        return render(request, 'loginjai.html')
#logut fucntion to logout from session
def Logout(request):
    logger.info("logout from accounts department")
    try:
        print("logout")
        logger.info('Acounts session ends')
        del request.session['loginjai']
        logger.info('Accounts deparment logout')
    except:
        pass
    return redirect('/')

def salary(request):
    if request.method=="POST":
     Employee_ID=request.POST["Employee_ID"]
     working_hour=float(request.POST['working_hour'])
     month=request.POST["month"]
     email=request.POST["email"]
     sla=Salary(Employee_ID=Employee_ID,working_hour=working_hour,month=month,email=email)
     sla.save()
     result=float(working_hour*500)
     subject = 'Welcome to Fashion HUB'
     message = 'Hello Mr./Miss Employee ID:'+Employee_ID+' your salary amount Rs'+str(float(result))+'has been credited to your bank account for the '+month+' month'
     email_from = settings.EMAIL_HOST_USER
     recipient_list = [email]
     send_mail(subject, message, email_from, recipient_list)
     return render(request,'homejai.html')

    else:
      return render(request,'Attendance.html')  