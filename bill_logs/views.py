from bill_logs.models import Export, imported
from django.shortcuts import redirect, render
from bill_logs.models import Export,imported
import logging
from django.http import HttpResponse
from django.views.generic import View
from bill_logs.utils import render_to_pdf 

import datetime


# Create your views here.
logger = logging.getLogger('django')
#showing Export bills
def shows(request):
     logger.info("showing export bills")
     bill=Export.objects.all()
     return render(request,'exported_bill.html',{'export': bill})
#Deleting Export bills
def destroys(request, id):  
    logger.info("deleting export bills")
    logs = Export.objects.get(id=id)  
    logs.delete()  
    return redirect("/exports/")   
#showing Import bills
def showss(request):
    logger.info("showing import bills")
    bill=imported.objects.all()
    return render(request,'import_bill.html',{'import': bill})
#Deleting Import bills
def destroyss(request, id):
    logger.info("deleting import bills")  
    logs = imported.objects.get(id=id)  
    logs.delete()  
    return redirect("/imports/") 
#Redirecting to editing page
def edit(request, id): 
    logger.info("redirecting to edit page for export bills") 
    jai = Export.objects.get(id=id)  
    return render(request,'edit.html', {'jai':jai})  
#updating the values
def update(request, id):
    logger.info("updating export bills")  
    billing_amt = request.POST['billing_amt']
    date_of_export = request.POST['date_of_export']
    gst_imposed = request.POST['gst_imposed']
    exported_to = request.POST['exported_to']
    order_ID = request.POST['order_ID']
    quantity = request.POST['quantity']
    estimated_time = request.POST['estimated_time']
    jais=Export(id=id,billing_amt=billing_amt,date_of_export=date_of_export,gst_imposed=gst_imposed,exported_to=exported_to,order_ID=order_ID,quantity=quantity,estimated_time=estimated_time)
    jais.save()
    return redirect('/exports/')
#class used to generate balance shet pdf
class GeneratePdf(View):
    logger.info("balance sheet pdf generated")
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('balancesheet.html', data)
        return HttpResponse(pdf, content_type='application/pdf')    
       