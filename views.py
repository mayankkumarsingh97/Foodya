# from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail  import EmailMultiAlternatives
from django.conf import settings
from .forms import FoodyaContactus

import sendgrid
from sendgrid import SendGridAPIClient



# Create your views here.


# def index(request):
#     if request.method == "POST":
#         name = request.POST.get('name')

#         email = request.POST.get('email')

#         phone = request.POST.get('phone')
#         message_1 = request.POST.get('message')
#         message = f'User details and order details are given below:-'+'\n'+'Name: '+ name + '\n' + 'Email: '+email + '\n' + 'Phone: '+phone + '\n' +'Message: '+message_1
#         Contactus.objects.create(name=name,email=email,message=message_1)
#         print(name,email,phone,message_1)

#         html_content_receive = render_to_string("contact_template_receive.html",{'name':name,'email':email,'phone':phone,'message':message_1})

#         mailing= EmailMultiAlternatives(
#         phone,
#         message_1,
#         settings.EMAIL_HOST_USER,
#         ['dreamboxincindia@gmail.com'],
#         ['kum.atul96@gmail.com'],

#         )
#         mailing.attach_alternative(html_content_receive,"text/html")
#         mailing.send()

#         html_content_send = render_to_string("contact_template_send.html",{'name':name})

#         mailing1= EmailMultiAlternatives(
#         phone,
#         message_1,
#         settings.EMAIL_HOST_USER,
#         [email],
#         )
#         mailing1.attach_alternative(html_content_send,"text/html")
#         mailing1.send()
#         print(mailing1)
#         try:
#             print("status==",mailing.status)
#         except:
#             print("fail==",mailing)
#     return render(request, 'index.html')



def index(request):


    fm = FoodyaContactus(request.POST)
    print(fm)
    if request.method == 'POST':
      
      if fm.is_valid():
          name = fm.cleaned_data['name']
          email = fm.cleaned_data['email']
          phone = fm.cleaned_data['phone']
          org = fm.cleaned_data['org']
          print(name)
          print(email)
          print(phone)
          print(org)
          reg = Contactus(name=name,email=email,phone=phone,org=org)
          reg.save()
    
          return redirect('home:thankyou')
        
      else:
              fm= FoodyaContactus()
    return render(request, 'index.html',{'form':fm})








def thankyou(request):
    return render(request, 'thankyou.html')


def contact1(request):

    return render(request, 'contact_template_receive.html')
#

def contact2(request):

    return render(request, 'contact_template_send.html')
