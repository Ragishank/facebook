from django.shortcuts import render
from . models import login,user
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
    # try:
    #     user_id=request.session['user']
    #     userObj=login.objects.get(id=user_id)
    #     password=request.POST['oldpass']
    #     newpassword=request.POST['npass']
    #     if(userObj.password==password):
    #         userObj.password=newpassword
    #         userObj.save()
    #         return render
    return render(request,'change_password.html')

    # try:
    #     user_id=request.session['user']
    #     userObj=login.objects.get(id=user_id)
    #     oser_obj=user.object.get(id=userObj.user_id_id)
    #     return render(request,'profile.html',{"user":userObj,"us1":oser_obj})



def fnLogins(request):
    return render(request,'login.html')   
    
def fntest(request):
    return render(request,'test.html')