from django.shortcuts import render
from django.forms.fields import NullBooleanField
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from .models import persoinfo
from .models import memberdets
from .models import newuserdets
import random
from django.contrib.auth import authenticate



def query(request):
        return render(request,"landingpage.html")

def query1(request):
        return render(request,"login.html")

# Create your views here.

sl = random.randint(100, 999)  #
global slnew
slnew =sl

global inc
inc = 1

def personal_inf(request):
    print("hi")
    if request.method == 'POST':
        print("hello")
        id_str = request.POST.get('id')
        if id_str != '' and id_str != 'NaN':
            id = int(id_str)
        else:
            id = None 

        a=request.POST.get('namee')
        b=request.POST.get('contacts')
        c=request.POST.get('emails')
        d=request.POST.get('dobs')
        e=request.POST.get('gen')
        f=request.POST.get('dept')

        a1=request.POST.get('ideaname')
        b1=request.POST.get('painp')
        c1=request.POST.get('solnp')
        d1=request.POST.get('innovm')
        e1=request.POST.get('prodf')
        f1=request.POST.get('custo')
        g=request.POST.get('availp')
        h=request.POST.get('busic')
        j=request.POST.get('spe')
        
        k=request.POST.get('businessidea')

        i = request.POST.get('prodname') 

        product_options = {
            '1': 'Software - Front End',
            '2': 'Software - BackEnd',
            '3': 'Software - AI/ML',
            '4': 'Software - Data Analytics',
            '5': 'Software - AR',
            '6': 'Software - VR',
            '7': 'Software - XR',
            '8': 'Software - Blockchain/Distributed Ledger',
            '9': 'Software - Fintech',
            '10': 'Other'
        }

        selected_option = product_options.get(i, '')

        per=persoinfo(id=id,SL=sl_value,Name=a,Contactno=b,Email=c,DateofBirth=d,Gender=e,Department=f,Projectname=a1,Painpoints=b1,Solution=c1,Innovation=d1,Features=e1,Customers=f1,Availability=g,Businessmodel=h,Projectdomain=selected_option,Specifications=j,Teamdetails=k)
        per.save()
        reset_sl_value()
    
    return render(request,"landingpage.html")

def reset_sl_value():
    sl = random.randint(100, 999)  
    global slnew
    slnew = sl


def save_member_details(request):
    if request.method == 'POST':
        id_str = request.POST.get('id')
        if id_str:
            id = int(id_str)
        else:
            id = None

        project_id_str = request.POST.get('project_id')
        if project_id_str:
            project_id = int(project_id_str)
        else:
            project_id = None

        member_name = request.POST.get('memnameone')
        contact_number = request.POST.get('memcontone')
        email = request.POST.get('memmailone')
        date_of_birth = request.POST.get('memdobone')
        gender = request.POST.get('memgenone')
        tsip_department = request.POST.get('memdeptone')
        role = request.POST.get('memroleone')
        core_competency = request.POST.get('memcoreone')

        member = memberdets(
            member_id=id,
            project_id=sl_value,
            MemberName=member_name,
            Contactnumber=contact_number,
            Email=email,
            DateofBirth=date_of_birth,
            Gender=gender,
            Department=tsip_department,
            Role=role,
            Competency=core_competency
        )
        member.save()

        return HttpResponse('Member details saved successfully')
    
    return HttpResponseBadRequest('Invalid request method')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if username == 'admin' and password == 'tsip123!@#':
                submissions = persoinfo.objects.all().values('id', 'Projectname','SL')  # Retrieve all form submissions
                context = {
                    'submissions': submissions
                }
                return render(request, 'submittedforms.html',context)
            try:
                user = newuserdets.objects.get(username=username, password=password)
            except newuserdets.DoesNotExist:
                error_message = 'Incorrect username or password.'
                return render(request, 'landingpage.html', {'error_message': error_message})
            
            global sl_value
            sl_value = user.SL
            request.session['sl_value'] = sl_value

            return render(request, 'login.html')
            
        else:
            error_message = 'Passwords entered do not match.'
            return render(request, 'landingpage.html', {'error_message': error_message})

    return render(request, 'login.html')


def new_user_page(request):
    return render(request, 'newuserlogin.html')

def loginpage(request):
    return render(request, 'landingpage.html')

def submit_form_login(request):
    return render(request, 'landingpage.html')

from django.core.exceptions import ObjectDoesNotExist

def newusercheck(request):
    if request.method == 'POST':
        firstname = request.POST.get('name1')
        lastname = request.POST.get('name2')
        username = request.POST.get('name3')
        mail = request.POST.get('email1')
        password = request.POST.get('password1')
        password1 = request.POST.get('password2')

        if password == password1:
            if firstname == "" or lastname == "" or username == "" or password == "" or password1 == "":
                error_message = 'Incorrect username or password.'
                return render(request, 'newuserlogin.html', {'error_message': error_message})
            
            if newuserdets.objects.filter(username=username).exists():
                error_message = 'Username already exists. Please choose a different username.'
                return render(request, 'newuserlogin.html', {'error_message': error_message})

            nud = newuserdets(SL=slnew, firstname=firstname, lastname=lastname, username=username, emailaddress=mail, password=password)
            nud.save()
            reset_sl_value()
            return render(request, 'landingpage.html')
        else:
            error_message = 'Passwords entered do not match.'
            return render(request, 'newuserlogin.html', {'error_message': error_message})
            
    return render(request, 'login.html')


def submitted_form(request, form_SL):
    try:
        member_data = memberdets.objects.filter(project_id=form_SL)
        form_data = persoinfo.objects.get(SL=form_SL)
    except (memberdets.DoesNotExist, persoinfo.DoesNotExist):
        return HttpResponse('Form not found.')

    form_data_dict = {
        'Name': form_data.Name,
        'Contactno': form_data.Contactno,
        'Email': form_data.Email,
        'DateofBirth': form_data.DateofBirth,
        'Gender': form_data.Gender,
        'Department': form_data.Department,
        'Projectname': form_data.Projectname,
        'Painpoints': form_data.Painpoints,
        'Solution': form_data.Solution,
        'Innovation': form_data.Innovation,
        'Features': form_data.Features,
        'Customers': form_data.Customers,
        'Availability': form_data.Availability,
        'Businessmodel': form_data.Businessmodel,
        'Projectdomain': form_data.Projectdomain,
        'Specifications': form_data.Specifications,
        'Teamdetails': form_data.Teamdetails,
    }
    member_data_list = []
    for member in member_data:
        member_data_dict = {
            'MemberName': member.MemberName,
            'Contactnumber': member.Contactnumber,
            'Email': member.Email,
            'DateofBirth': member.DateofBirth,
            'Gender': member.Gender,
            'Department': member.Department,
            'Role': member.Role,
            'Competency': member.Competency,
        }
        member_data_list.append(member_data_dict)

    context = {
        'member_data': member_data_list,
        'form_data': form_data_dict
    }
    return render(request, 'submittedform.html', context)

def view_form_users(request):
    return render(request, 'viewformuser.html' )

def formcheck(request):
    if request.method == 'POST':
        username = request.POST.get('name3')
        password = request.POST.get('password3')
        password1 = request.POST.get('password4')

        if password == password1:
            try:
                user = newuserdets.objects.get(username=username, password=password)
            except newuserdets.DoesNotExist:
                error_message = 'Incorrect username or password.'
                return render(request, 'viewformuser.html', {'error_message': error_message})
            
            global sl_value
            sl_value = user.SL
            request.session['sl_value'] = sl_value
            try:
                member_data = memberdets.objects.filter(project_id=sl_value)
                form_data = persoinfo.objects.get(SL=sl_value)
            except (memberdets.DoesNotExist, persoinfo.DoesNotExist):
                return HttpResponse('Form not found.')
            form_data_dict = {
                'Name': form_data.Name,
                'Contactno': form_data.Contactno,
                'Email': form_data.Email,
                'DateofBirth': form_data.DateofBirth,
                'Gender': form_data.Gender,
                'Department': form_data.Department,
                'Projectname': form_data.Projectname,
                'Painpoints': form_data.Painpoints,
                'Solution': form_data.Solution,
                'Innovation': form_data.Innovation,
                'Features': form_data.Features,
                'Customers': form_data.Customers,
                'Availability': form_data.Availability,
                'Businessmodel': form_data.Businessmodel,
                'Projectdomain': form_data.Projectdomain,
                'Specifications': form_data.Specifications,
                'Teamdetails': form_data.Teamdetails,
            }
            member_data_list = []
            for member in member_data:
                member_data_dict = {
                    'MemberName': member.MemberName,
                    'Contactnumber': member.Contactnumber,
                    'Email': member.Email,
                    'DateofBirth': member.DateofBirth,
                    'Gender': member.Gender,
                    'Department': member.Department,
                    'Role': member.Role,
                    'Competency': member.Competency,
                }
                member_data_list.append(member_data_dict)

            context = {
                'member_data': member_data_list,
                'form_data': form_data_dict
            }
            return render(request, 'userviewform.html', context)
            
        else:
            error_message = 'Passwords entered do not match.'
            return render(request, 'viewformuser.html', {'error_message': error_message})

