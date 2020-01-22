from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'contactform/index.html')

def send(request):
    if request.method == "POST":
        sender = request.POST.get("emailFrom")
        receiver = request.POST.get("emailTo")
        subject = request.POST.get("emailSubject")
        message = request.POST.get("emailMessage")

        message = Mail(
            from_email=sender,
            to_emails=receiver,
            subject=subject,
            html_content=message)

        with open('contactform/templates/contactform/sendgrid_key.txt') as f:
            SENDGRID_KEY = f.read().strip()

        try:
            sg = SendGridAPIClient(SENDGRID_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

        return redirect("/")
    return render(request, 'contactform/index.html')

