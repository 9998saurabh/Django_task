from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from .models import *
def index(request):
    return render(request,"index.html")



@csrf_exempt
def register_(request):
    print("hello")
    supplier_business_name = request.POST.get('supplier_business_name')
    print(supplier_business_name)
    supplier_address = request.POST.get('supplier_address')
    print(supplier_address)
    representaive_full_name = request.POST.get('representaive_full_name')
    print(representaive_full_name)
    email = request.POST.get('email')
    print(email)



    password = request.POST.get('password')
    # ptype =  request.POST.get('ptype')
    data = Registration(supplier_business_name=supplier_business_name, supplier_address=supplier_address,representaive_full_name= representaive_full_name,
                     email=email
                    , password=password)
    data.save()
    html = render(request,"reg.html")

    return HttpResponse(html)


@csrf_exempt
def editprofile(request):
    try:
        if request.session['user_id_id'] == '':
            return HttpResponse('Hello')
    except Exception as e:
        print("Exception", e)
        if e =="user_id_id":
            return HttpResponseRedirect('/')
    email = request.POST.get('email')
    user_id = request.session['user_id_id']
    print("userid ", user_id)
    pr_id = request.POST.get('pr_id')
    data = Registration.objects.get(User_id=user_id)

    if data:
        supplier_business_name = request.POST.get('supplier_business_name')
        print("supplier", supplier_business_name)
        supplier_address = request.POST.get('supplier_address')
        representaive_full_name = request.POST.get('primary_representaive_full_name')
        email = request.POST.get('email_address')
        phone_number = request.POST.get('phone_number')
        seondary_representaive_full_name = request.POST.get('secondary_representaive_full_name')
        secondary_email_address = request.POST.get('secondary_email_address')
        secondary_phone_number = request.POST.get('secondary_phone_number')
        related_entities = request.POST.get('related_entities')
        Product_and_services = request.POST.get('Product_and_services')
        product_edit = Registration.objects.get(User_id=user_id)
        product_edit.supplier_business_name = supplier_business_name
        product_edit.supplier_address = supplier_address
        product_edit.representaive_full_name = representaive_full_name
        product_edit.email_address = email
        product_edit.phone_number = phone_number
        product_edit.seondary_representaive_full_name = seondary_representaive_full_name
        product_edit.secondary_email_address = secondary_email_address
        product_edit.secondary_phone_number = secondary_phone_number
        product_edit.related_entities = related_entities
        product_edit.Product_and_services = Product_and_services
        product_edit.save()

    print("hello i am data ", data.supplier_business_name)
    html = render(request, "profilepage.html")

    return HttpResponse(html)


@csrf_exempt
def Registerd_details(request):
    try:
        if request.session['user_id_id'] == '':
            return HttpResponse('Hello')
    except Exception as e:
        print("Exception", e)
        return HttpResponseRedirect('/')
    email = request.POST.get('email')
    user_id = request.session['user_id_id']
    print("userid ", user_id)
    pr_id = request.POST.get('pr_id')
    data = Registration.objects.get(User_id=user_id)

    html = render(request,"profilepage.html",{'data':data})

    return HttpResponse(html)

@csrf_exempt
def saveProfile(request):
    try:
        if request.session['user_id_id'] == '':
            return HttpResponse('Hello')
    except Exception as e:
        if e =="user_id_id":
            return HttpResponse('/')
    supplier_business_name = request.POST.get('supplier_business_name')
    print("supplier", supplier_business_name)
    supplier_address = request.POST.get('supplier_address')
    representaive_full_name = request.POST.get('primary_representaive_full_name')
    email = request.POST.get('email_address')
    phone_number = request.POST.get('phone_number')
    seondary_representaive_full_name = request.POST.get('secondary_representaive_full_name')
    secondary_email_address = request.POST.get('secondary_email_address')
    secondary_phone_number = request.POST.get('secondary_phone_number')
    related_entities = request.POST.get('relative_entity')
    Product_and_services = request.POST.get('product_and_services')

    # ptype =  request.POST.get('ptype')
    data = Registration(supplier_business_name=supplier_business_name, supplier_address=supplier_address,representaive_full_name =representaive_full_name,
                     email=email,phone_number=phone_number,seondary_representaive_full_name=seondary_representaive_full_name,secondary_email_address=secondary_email_address
                     ,secondary_phone_number=secondary_phone_number,related_entities=related_entities,Product_and_services=Product_and_services
                    )
    data.save()
    html = render(request,"profilepage.html")

    return HttpResponse(html)

@csrf_exempt
def emailcheck(request):
    email = request.POST.get('email')
    check_data= Registration.objects.filter(email=email).exists()

    response = {"check_data":check_data}

    return JsonResponse(response)

@csrf_exempt
def login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    print("email, pasword", email,password)

    error = "enter valid data"
    data = Registration.objects.filter(email=email, password=password)
    print("data",data)
    #data1 = user_data.objects.filter(email=email, password=password)
    if email == "login1@admin.com":
        UserSessions = Registration.objects.get(email=email)
        request.session['user_id_id'] = UserSessions.User_id
        print("iddd", request.session['user_id_id'])
        # type = {'type':"admin"}
        return HttpResponse("admin")
    elif data:
        UserSessions = Registration.objects.get(email=email)
        request.session['user_id_id'] = UserSessions.User_id
        print("iddd",request.session['user_id_id'])
        # type = {'type':"admin"}
        return HttpResponse("success")
    else:
        return HttpResponse("error")




def Logoutuser(request):
    try:
        del request.session['user_id_id']
        print("delited")
    except Exception as e:
        print("Error in logging out ",str(e))
        if e =="user_id_id":
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')



def admin(request):

    try:
        if request.session['user_id_id'] == '':
            return HttpResponse('Please Login')
    except Exception as e:
        if e =="user_id_id":
            return HttpResponseRedirect('/')
    if request.GET:
        print("1")
    elif request.POST:
        print("2")
    else:
        print("3")


    if request.GET:
        search  = request.GET.get("Search")
        print("serching for ",search)
        data={}
        phone_number = ""
        supplier_business_name=""
        try:
            import re
            phone_number = re.search(r'[0-9]+', search).group(0)
        except Exception as e:
            supplier_business_name = re.search(r'[A-Za-z]+', search).group(0)

        if search is not None:
            if "@" in search:
                data = Registration.objects.filter(email=search)
                print("in iemail",data)

            elif phone_number:

                data = Registration.objects.filter(phone_number=search)
                print("in phone number",data)
            elif supplier_business_name:
                data = Registration.objects.filter(supplier_business_name=search)
                print("in business name ")


        return render(request, 'admin.html', {'data': data})
    else:
        return render(request, 'admin.html')

