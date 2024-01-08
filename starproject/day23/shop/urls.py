from django.contrib import admin
from django.urls import path
from . import views



#>>>>>  this is "Shop" Urls


urlpatterns = [
    path('',views.indexshop,name="ShopHome"),
    path('about',views.about,name="AboutUs"),
    path('contract',views.contract,name="ContractUs"),
    path('tracker',views.tracker,name="TrackingStatus"),
    path('search',views.search,name="Search"),
    path('prodviews',views.prodviews,name="productviews"),
    path('cheackout',views.cheackout,name="CheackOut"),
    
    
   
]
