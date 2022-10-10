from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Application

def application(request):
  if request.method == 'POST':
    requisition_id = request.POST['requisition_id']
    requisition = request.POST['requisition']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    manager_email = request.POST['manager_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Application.objects.all().filter(requisition_id=requisition_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already applied for this position')
        return redirect('/requisitions/'+requisition_id)

    application = Application(requisition=requisition, requisition_id=requisition_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    application.save()

    # Send email
    # send_mail(
    #   'Requisition Application',
    #   'There has been an application for ' + requisition + '. Sign into the admin panel for more info',
    #   ' @tubefab.org',
    #   [manager_email, 'hr@tubefab.org'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/requisitions/'+requisiton_id)
