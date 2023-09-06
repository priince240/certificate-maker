from django.contrib import admin
from django.urls import path,include
from . import views
from .views import userget,userlogin,usersignin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
router =routers.DefaultRouter()
router.register("api",views.postviewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/accesstoken
    path('accesstoken/',TokenObtainPairView.as_view(),name="access"),
     #http://127.0.0.1:8000/refreshtoken
    path('refreshtoken/',TokenRefreshView.as_view(),name="refresh"),
    path("certificate/<int:id>",views.certificate,name='home'),
    path("certificatepdf/",views.printt,name='home'),
     #http://127.0.0.1:8000/verfytoken
    path("verfytoken/", TokenVerifyView.as_view(),name='verfytoken'),
    #http://127.0.0.1:8000/fillform/  + id  or click on template image to fill th form
    path("fillform/<int:id>",views.fillform,name='hello'),
     #http://127.0.0.1:8000/
    path("",views.firstpage,name='firstpage'),
     #http://127.0.0.1:8000/list/api
    path("list/",include(router.urls)),
    
    path("convert/<int:id>",views.html_to_pdf,name='pdf'),
    path("signin",usersignin.as_view(),name='signin'),
    path("login",userlogin.as_view(),name='login'),
    path("getdata/",userget.as_view(),name='getuser'),  #get user data
    # path("auth/",include('rest_framework.urls'))
  
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#|___________________________________________________________\
#                    image/file upload code