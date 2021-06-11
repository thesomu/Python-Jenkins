"""Fashion_Hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include

from Management.views import *
from billing_details.views import loginjai, billing_view, loginjai, show, destroy, dashboard, Logout, salary
from bill_logs.views import shows, destroys, destroyss, showss, edit, update, GeneratePdf
from Import.views import portal_view, portalLogin_view, logout_view, import_view, insertImportOrder_view, displayImportOrders_view, editImportOrders_view, updateImportOrders_view, deleteImportOrders_view, displayCompanies_view
from Export.views import clientDemands_view, displayExportOrders_view, insertExportOrders_view, placeExportOrder_view, editExportOrder_view, deleteExportOrder_view, updateExportOrder_view, partnerPage_view

# Flow of the program starts from codingfreaks(project) urls.
# Here path will be checked and redirected to shopping(app) urls.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shopping.urls')),
    path('wrogn', include('shopping.urls')),
    path('flying', include('shopping.urls')),
    path('peter', include('shopping.urls')),
    path('product', include('shopping.urls')),
    path('cart', include('shopping.urls')),

    # kanishk url
    path('management', include('Management.urls')),
    path('register', include('Employee.urls')),

    # jai function urls
    path('loginjai', loginjai),
    path('bills', billing_view, name="billing_details"),
    path('billing/', show),
    path('delete/<int:id>', destroy),
    path('exports/', shows),
    path('deletes/<int:id>', destroys),
    path('imports/', showss),
    path('deletess/<int:id>', destroyss),
    path('edit/<int:id>', edit),
    path('update/<int:id>', update),
    path('dashboardjai/', dashboard),
    path('logoutjai/', Logout),
    path('pdf/', GeneratePdf.as_view()),
    path('salary', salary),

    path('ielogin', portal_view, name='portalPage'),
    path('login', portalLogin_view, name='portalLogin'),
    path('out', logout_view, name='pageLogout'),
    path('menu', import_view, name='importMain'),
    path('import', insertImportOrder_view, name="importOrder"),
    path('displayOrders', displayImportOrders_view, name='showOrders'),
    path('editImportOrder/<int:id>', editImportOrders_view, name="editOrders"),
    path('updateImportOrder/<int:id>',
         updateImportOrders_view, name="updateOrders"),
    path('deleteImportOrder/<int:id>',
         deleteImportOrders_view, name="deleteOrder"),
    path('viewCompanies', displayCompanies_view, name="viewCompanies"),
    path('displayExportOrders', displayExportOrders_view, name="exportOrders"),
    path('insertExportOrder/<int:id>',
         insertExportOrders_view, name="insertExportOrders"),
    path('clientDemands', clientDemands_view, name='clientDemand'),
    path('placeExportOrder/<int:id>', placeExportOrder_view, name="placeOrder"),
    path('editExportOrder/<int:id>', editExportOrder_view, name="editExportOrder"),
    path('updateExportOrder/<int:id>',
         updateExportOrder_view, name="updateExportOrder"),
    path('deleteExportOrder/<int:id>',
         deleteExportOrder_view, name="deleteExportOrder"),
    path('partners', partnerPage_view, name="partnerPage"),

    # somnath url
    path('custregister', include('users.urls'))

]
