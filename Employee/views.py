from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from Employee.models import empTable
from Management.models import dailyAttendance, empAttendance, totalAttendance

import logging

logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

"""This is to register the employee
    It would use POST method if data is coming from web page
    It would use GET method to redirect to the web page
"""


def empregister(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        designation = request.POST['designation']
        password = phone

        countAddress = address.count(',')
        countName = name.count(' ')

        if countAddress >= 2 and countName > 0:
            emp = empTable(name=name, address=address, phone=phone, email=email, designation=designation,
                           password=password)
            emp.save()
            daily = dailyAttendance(empId=emp)
            daily.save()
            empAtt = empAttendance(empId=emp)
            empAtt.save()
            total = totalAttendance(empId=emp)
            total.save()
            logging.info('Employee registered successfuuly')

            subject = 'Welcome to Fashion HUB'
            message = 'Hello Mr./Miss ' + name + ', thank you for registering in Fashion HUB.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)

            return redirect('details')
        else:
            if countName < 1:
                logging.error('Error in name')
                messages.error(request, 'Name should have first and last name')
            if countAddress < 2:
                logging.error('Error in address')
                messages.error(request, 'Address should have society, city and pin code')
            return render(request, 'EmployeeRegistration.html')
    else:
        logging.info('Registering an employee')
        return render(request, 'EmployeeRegistration.html')


"""To get the details of all employees"""


def details(request):
    emp = empTable.objects.all()
    logging.info('Getting employees details')
    return render(request, 'Details.html', {'details': emp})


"""This is a dynamic page for a particular employee"""


def employeeProfile(request):
    if 'emp' in request.session:
        current_emp = request.session['emp']
        logging.info('Employee session starts')
        return render(request, 'EmployeeProfile.html', {'current_emp': current_emp})
    else:
        logging.warning('Wrong session')
        return redirect('employeeLogin')


"""To move to the update page"""


def edit(request):
    id2 = request.POST.get('id')
    employee = empTable.objects.get(id=id2)
    logging.info('Update the employee')
    return render(request, 'Update.html', {'employee': employee})


def employeeEdit(request):
    id2 = request.POST.get('id')
    employee = empTable.objects.get(id=id2)
    logging.info('Update the employee')
    return render(request, 'EmployeeUpdate.html', {'employee': employee})


"""To update the employee details"""


def update(request):
    id2 = request.POST['id']  # primary key
    name = request.POST['name']
    address = request.POST['address']
    phone = request.POST['phone']
    email = request.POST['email']
    designation = request.POST['designation']
    print(type(designation))
    password = phone

    countAddress = address.count(',')
    countName = name.count(' ')

    if countAddress >= 2 and countName > 0:
        emp = empTable(id=id2, name=name, address=address, phone=phone, email=email, designation=designation,
                       password=password)
        emp.save()
        logging.info('Employee updated successfully')
        return redirect('details')
    else:
        if countName < 1:
            logging.error('Error in updating employee name')
            messages.error(request, 'Name should have first and last name')
        if countAddress < 2:
            logging.error('Error in updating employee address')
            messages.error(request, 'Address should have society, city and pin code')
        employee = empTable.objects.get(id=id2)
        return render(request, 'Update.html', {'employee': employee})

    emp = empTable.objects.all()
    return render(request, 'Details.html', {'details': emp})


def employeeUpdate(request):
    id2 = request.POST['id']  # primary key
    name = request.POST['name']
    address = request.POST['address']
    phone = request.POST['phone']
    email = request.POST['email']
    employee = empTable.objects.get(id=id2)
    designation = employee.designation
    password = employee.password

    countAddress = address.count(',')
    countName = name.count(' ')

    if countAddress >= 2 and countName > 0:
        emp = empTable(id=id2, name=name, address=address, phone=phone, email=email, designation=designation,
                       password=password)
        emp.save()
        logging.info('Employee updated successfully')
        return render(request, 'EmployeeProfile.html', {'employee': employee})
    else:
        if countName < 1:
            logging.error('Error in updating employee name')
            messages.error(request, 'Name should have first and last name')
        if countAddress < 2:
            logging.error('Error in updating employee address')
            messages.error(request, 'Address should have society, city and pin code')
        employee = empTable.objects.get(id=id2)
        return render(request, 'EmployeeUpdate.html', {'employee': employee})

    emp = empTable.objects.all()
    return render(request, 'EmployeeProfile.html', {'employee': employee})


"""To delete an employee"""


def destroy(request):
    id2 = request.POST.get('id')
    employee = empTable.objects.get(id=id2)
    employee.delete()
    emp = empTable.objects.all()
    logging.info('Employee deleted successfully')
    return render(request, 'Details.html', {'details': emp})
