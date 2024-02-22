from django.shortcuts import render
import csv
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def send_emails(request):
    csv_file_path =r'D:\PFSD\pythonProject\DjangoProjects\TTM\static\mail.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here
            send_mail(
                subject,
                message_body,
                '2200033161cseh@gmail.com',
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
        return render(request, 'Emails_sent_successfully.html')