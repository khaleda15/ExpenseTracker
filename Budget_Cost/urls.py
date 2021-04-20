from django.contrib import admin
from django.urls import path,include
from Budget.views import Home,AddCost,UpdateCost,DeleteCost,AddAsset,DeleteAsset,Userlogin,userlogout,UserSignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='home'),
    path('addcost/',AddCost.as_view(),name='addcost'),
    path('addasset/',AddAsset.as_view(),name='addasset'),
    path('updatecost/<int:pk>/',UpdateCost.as_view(),name='updatecost'),
    path('deletecost/<int:pk>/',DeleteCost.as_view(),name='deletecost'),
    path('deleteasset/<int:pk>/',DeleteAsset.as_view(),name='deleteasset'),
    path('login/',Userlogin.as_view(),name = 'login'),
    path('logout/',userlogout,name = 'logout'),
    path('signup/',UserSignUp.as_view(),name = 'signup'),
]
