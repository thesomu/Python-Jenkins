from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render

from Import.models import Import, Companies
import logging

logger = logging.getLogger(__name__)

# Create your views here.


def portal_view(request):
    logger.info("Main Dashboard page is requested")
    return render(request, "importAndExportPortal.html", {})


def portalLogin_view(request):
    """
    """
    logger.info("Inside portalLogin_view")
    if request.method == "POST":
        userId = request.POST['user']
        password = request.POST['password']
        if((userId == 'harsh1234') and (password == "1998")):
            logger.info('User authenticated and request sent to next page')
            request.session['user'] = userId
            return render(request, "menuPage.html")
        else:
            logger.warning(
                "Authentication failed. Wrong login details. The login page is reloaded")
            messages.error(request, "Wrong credentials")
            return redirect('/')
    else:
        logger.warn("Post method not used and request redirected ")
        return render(request, 'importAndExportPortal.html')


def logout_view(request):
    logger.info("Inside logout_view")
    try:
        del request.session['user']
    except:
        logger.info(
            "Logout successful and request redirected to login dashboard")
        return redirect('/')
    logger.info("Logout successful and request redirected to login dashboard")
    return redirect('/')


def import_view(request):
    """
    """
    logger.info("Inside import_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        if request.method == "POST":
            if(request.POST.get('imp') != None):
                logger.info(
                    "Request redirected to next page if the user selects import option from the menu")
                return render(request, "importPage.html")
            elif(request.POST.get('exp') != None):
                logger.info(
                    "Request redirected to next page if the user selects export option from the menu")
                return redirect('/displayExportOrders')
        else:
            return render(request, 'menuPage.html')

    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def insertImportOrder_view(request):
    """
    """
    logger.info("Inside insertImportOrder_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        if request.method == "POST":
            id = request.POST['orderid']
            date = request.POST['orderdate']
            country = request.POST['orderCountry']
            product = request.POST['orderProduct']
            status = request.POST['list']
            print(status)
            totalCost = request.POST['orderCost']

            order = Import(orderImport_id=id, order_date=date, import_product=product,
                           orderImport_country=country, status_of_import=status, total_cost=totalCost)
            order.save()
            logger.info(
                "Record inserted in database successfully and request redirected to display orders page.")
            return redirect('/displayOrders')
        else:
            return render(request, 'importPage.html')

    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def displayImportOrders_view(request):
    """
    """
    logger.info("Inside displayImportOrders_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        importOrders = Import.objects.all()
        logger.info(
            "Record fetched successfully and request redirected to importOrders page.")
        return render(request, "importOrders.html", {'importOrders': importOrders})
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def editImportOrders_view(request, id):
    """
    """
    logger.info("Inside editImportOrders_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        orders = Import.objects.get(id=id)
        logger.info("Record fetched on the basis of id: "+str(id) +
                    " and request redirected to editImportPage")
        return render(request, 'editImportPage.html', {'orders': orders})
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def updateImportOrders_view(request, id):
    """
    """
    logger.info("Inside updateImportOrders_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        orderImport_id = request.POST['orderid']
        date = request.POST['orderdate']
        country = request.POST['orderCountry']
        product = request.POST['orderProduct']
        status = request.POST['list']
        totalCost = request.POST['orderCost']
        order = Import(id=id, orderImport_id=orderImport_id, order_date=date, import_product=product,
                       orderImport_country=country, status_of_import=status, total_cost=totalCost)
        order.save()
        logger.info("Record with id: "+str(id) +
                    " updated successfully and request redirected to the displayOrders page.")
        return redirect('/displayOrders')
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def deleteImportOrders_view(request, id):
    """
    """
    logger.info("Inside deleteImportOrders_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        orders = Import.objects.get(id=id)
        orders.delete()
        logger.info("Record with id "+str(id) +
                    " deleted successfully and request forwarded to displayOrders page")
        return redirect('/displayOrders')
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def displayCompanies_view(request):
    """
    """
    logger.info("Inside displayCompanies_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        companies = Companies.objects.all()
        logger.info(
            "Record fetched successfully and request redirected to viewCompanies page.")
        return render(request, "viewCompanies.html", {'companies': companies})
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')
