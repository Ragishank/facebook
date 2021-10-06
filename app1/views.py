from django.shortcuts import render
from . models import *
from random import random
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from app1.serializers import user_serializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
def fnIndex(request):
    try:
        mob_email=request.POST['mob_email']
        us_obj=login.objects.filter(username=mob_email).exists()
        if us_obj==False:
            fname=request.POST['firstname']
            sname=request.POST['surname']
           
            print(mob_email)
            password=request.POST['password']
            day=request.POST['day']
            month=request.POST['month']
            year=request.POST['year']
            date=year+'-'+month+'-'+day
            gender=request.POST['gender']
           
            userObj=user(firstname=fname,surname=sname,dob=date,gender=gender)
            print(userObj)
            userObj.save()
            loginObj=login(username=mob_email,password=password,user_id_id=userObj.id)
            loginObj.save()
            return render(request,'index.html',{"message":"saved successfully"})
        return render(request,'index.html',{"message":"user already exist"})  
        
    except Exception as e:
        print(e)
    return render(request,'index.html')
def fnA(request):
    return render(request,'a.html')

# login
def fnLogin(request):
    try:
        username=request.POST['username']
        password=request.POST['password']
        userObj=login.objects.get(username=username,password=password)
        request.session['user']=userObj.id
        user_Obj=user.objects.get(id=userObj.user_id_id)
        return render(request,'home.html',{"user":user_Obj})
    except Exception as e:
        print(e)
        return render(request,'index.html',{"message":"invalid username or password"})
def fnChangepassword(request):
    try:
        user_id=request.session['user']
        userObj=login.objects.get(id=user_id)
        password=request.POST['oldpass']
        newpassword=request.POST['npass']
        if(userObj.password==password):
            userObj.password=newpassword
            userObj.save()
            return render(request,'change_password.html',{'message':'password changed'})
        return render(request,'change_password.html',{'message':'password not matching'})
   
    except Exception as e:
        print(e)
    return render(request,'change_password.html')
def fnLogout(request):
    del request.session['user']
    return render(request,'index.html')         
def fnLogins(request):
    return render(request,'login.html')   
    
def fntest(request):
    if(request.method=="POST"):
        name=request.POST['name']
        addr=request.POST['address']
        files=request.FILES['files']
        files_name=str(random())+files.name
        fileObj=FileSystemStorage()
        fileObj.save(files_name,files)
        profObj=prof(name=name,address=addr,img=files_name)
        profObj.save()
        # return redirect('test.html')
    obj2=prof.objects.all()
    return render(request,'test.html',{'obj1':obj2})
    # return render(request,'test.html')

def fnAjax(request):
    return render(request,'ajaxex.html')   

def fnadd_Ajax(request):
    name=request.POST['name']
    contact=request.POST['address']
    email=request.POST['email']

    obj=ajaxex(name=name,address=contact,email=email)
    obj.save()
    return JsonResponse({'message':'data inserted'})  
def fnEdit(request):
    # if(request.method=='POST'):
    #     mob_email=request.POST['mob_email']
    #     us_obj=login.objects.filter(username=mob_email).exists()
    #     if us_obj==False:
            # fname=request.POST['firstname']
            # sname=request.POST['surname']
            # print(mob_email)
            # password=request.POST['password']
            # day=request.POST['day']
            # month=request.POST['month']
            # year=request.POST['year']
            # date=year+'-'+month+'-'+day
            # gender=request.POST['gender']
    user=request.session['user']
    print((user))
    usrObj=login.objects.select_related('user_id').filter(id=user)
    print(usrObj)
    return render(request,'manage_profile.html',{'userObj':usrObj})
@csrf_exempt
def fnSerial(request):
    if request.method=='GET':
        ajaxObj=ajaxex.objects.all()
        serialUserData=user_serializer(ajaxObj,many=True)
        return JsonResponse(serialUserData.data,safe=False)
    elif request.method=='POST':
        userdata=JSONParser().parse(request)
        sdata=user_serializer(data=userdata)
        if sdata.is_valid():
            sdata.save()
            return JsonResponse('data inserted successfully',safe=False)
        return JsonResponse('error',safe=False)
def fnSample(request):
    obj=user.objects.all()
    return render(request,'sampleuser.html',{'user':obj})

def fnUserdelete(request):
    if request.method=='POST':
        us_id=request.POST['us_id']
        print(us_id)
        userObj=user.objects.get(id=us_id).delele()
        return render(request,'sampleuser.html',{'msg':"user deleted"})
    return render(request,'sampleuser.html',{'msg':"failed"})
def fnTestcase(request):
    dob='1993-11-20'
    gender='female'
    return render(request,'select.html',{'dob':dob,'gen':gender})