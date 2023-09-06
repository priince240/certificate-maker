from django.shortcuts import render,redirect,HttpResponse
from rest_framework.response import Response
from .models import postclass,imageupload
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import postclassserializer,signinserializer,loginserializer,usergetserializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.authentication import authenticate


from rest_framework_simplejwt.tokens import RefreshToken
#token---------------------------------


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
    
def certificate(request,id):
    # if id is not None:
    data4 = postclass.objects.get(id=id)
    
    # else:
    # data4 = postclass.objects.all()

    return render(request, "certificate.html", {'data4': data4})

def fillform(request,id):
    data=imageupload.objects.get(id=id)
    if request.method=='POST':
        name = request.POST.get('name')
        course=request.POST.get('course')
        date=request.POST.get('date')
        sign=request.FILES.get('sign')
        fileup=imageupload.objects.get(id=id)
        data3=postclass()
        
        data3.name=name
        data3.course=course
        data3.date=date
        data3.sign=sign
        data3.fileup=fileup
        data3.save()
        return redirect("/certificate/"+str(data3.id))
    return render(request,"fillform.html",{'data':data,})






#first page
def firstpage(request):
    data=imageupload.objects.all()
    data4=postclass.objects.all()
    return render(request,"firstpage.html",{'data':data,'data4':data4})




def printt(request,id):
    data4=postclass.objects.get(id=id)
    return render(request,"print.html",{'data4':data4})




#this function create PDF

def html_to_pdf(request,id):
     data4=postclass.objects.get(id=id)
     template_path='print.html'
     content={'data4':data4}
     response=HttpResponse(content_type="application/pdf")
     response['Content Disposition']='filename="certificate.pdf"'
     template=get_template(template_path)
     html=template.render(content)
     pisa_load=pisa.CreatePDF(html,dest=response)
     if pisa_load.err:
         return HttpResponse('error')
     return response       


class postviewset(viewsets.ModelViewSet):
    queryset=postclass.objects.all()
    serializer_class=postclassserializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
#-------------------------------------------------------------------------------------------------------------
#this function create User in database
#http://127.0.0.1:8000/signin
#user json formate eg:-
#{ "name": "",
#"email": "",
#"password": "",
# "password2":""}

# usersignin----------------------------------------
class usersignin(APIView):
    def post(self,request):
        serializer=signinserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'sign success'})
        return Response(serializer.errors)
    

#this function login the User
#http://127.0.0.1:8000/login
#use json format :-  {"email":"","password":"" }
# userlogin------------------------------------------
class userlogin(APIView):
    
    def post(self,request):
        serializer=loginserializer(data=request.data)
        if serializer.is_valid():
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({"msg":"login success",'token':token})
            return Response({"msg":"invalid -----"})
        return Response(serializer.errors)  
    
    
#this function get all data for visiter
# http://127.0.0.1:8000/getdata/         
#userget-------------------------------------------------        
class userget(APIView):
    def get(self,request):
        data=postclass.objects.all()
        serializer=usergetserializer(data,many=True,context={'request':request})            
        return Response({'msg':'get success',"data":serializer.data})
     