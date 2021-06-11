from django.shortcuts import render, redirect
from Export.models import Client_Demand, Export
import logging

logger = logging.getLogger(__name__)


def displayExportOrders_view(request):
    """
    """
    logger.info("Inside displayExportOrders_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        exports = Export.objects.all()
        logger.info(
            "Record fetched successfully and request redirected to displayExportOrders page.")
        return render(request, "exportOrders.html", {'exports': exports})
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def clientDemands_view(request):
    """
    """
    logger.info("Inside clientDemands_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        clients = Client_Demand.objects.all()
        logger.info(
            "Record fetched successfully and request redirected to clientDemands page.")
        return render(request, "clientDemands.html", {'clients': clients})
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def insertExportOrders_view(request, id):
    """
    """
    logger.info("Inside insertExportOrders_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        client = Client_Demand.objects.get(id=id)
        logger.info(
            "Record fetched successfully and request redirected to exportPage page.")
        return render(request, 'exportPage.html', {'client': client})
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def placeExportOrder_view(request, id):
    """
    """
    logger.info("Inside placeExportOrder_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        if request.method == 'POST':
            eid = request.POST['orderid']
            dateOfOrder = request.POST['orderdate']
            clientName = request.POST['clientname']
            status = request.POST['list']
            pricePerPiece = request.POST['price']

            clientDemand = Client_Demand.objects.get(id=id)
            exportOrder = Export(exportProduct_id=eid, product_name=clientDemand, client_name=clientName,
                                 price_per_piece=pricePerPiece, date_of_export=dateOfOrder, status=status)
            exportOrder.save()
            logger.info(
                "Record inserted in database successfully and request redirected to display orders page.")
            return redirect('/displayExportOrders')
        else:
            return render(request, 'exportPage.html')
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def editExportOrder_view(request, id):
    """
    """
    logger.info("Inside editExportOrders_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        export = Export.objects.get(id=id)
        logger.info("Record fetched on the basis of id: "+str(id) +
                    " and request redirected to editExportPage")
        return render(request, 'editExportPage.html', {'export': export})
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def updateExportOrder_view(request, id):
    """
    """
    logger.info("Inside updateExportOrder_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        orginalOrder = Export.objects.get(id=id)
        clientDemand = orginalOrder.product_name
        eid = request.POST['orderid']
        dateOfOrder = request.POST['orderdate']
        clientName = request.POST['clientname']
        status = request.POST['list']
        pricePerPiece = request.POST['price']

        exportOrder = Export(id=id, exportProduct_id=eid, product_name=clientDemand, client_name=clientName,
                             price_per_piece=pricePerPiece, date_of_export=dateOfOrder, status=status)
        exportOrder.save()
        logger.info(
            "Record inserted in database successfully and request redirected to display orders page.")
        return redirect('/displayExportOrders')
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def deleteExportOrder_view(request, id):
    """
    """
    logger.info("Inside deleteExportOrder_view")
    if 'user' in request.session:
        logger.debug("User session successful")
        export = Export.objects.get(id=id)
        export.delete()
        logger.info("Record with id "+str(id) +
                    " deleted successfully and request forwarded to exportOrders page")
        return redirect('/displayExportOrders')
    else:
        logger.warn(
            "User session not found and request redirected to dashboard.")
        return redirect('/')


def partnerPage_view(request):
    """
    """
    logger.info("Inside partnerPage_view")
    return render(request, 'partners.html')
