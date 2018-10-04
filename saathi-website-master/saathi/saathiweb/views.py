from django.shortcuts import render
from saathiweb.forms import AppointmentForm
from django.http import HttpResponse
import smtplib
# Create your views here.
def index(request):
    form = AppointmentForm()

    if request.method == "POST":
        name = request.POST.get('name')
        webmail = request.POST.get('email')
        body = request.POST.get('message')

        TO = ['ayush2016@iitg.ac.in','pallabita.b.c@iitg.ernet.in','namrata.r@iitg.ernet.in','rkakati@iitg.ernet.in','nesmita.d@iitg.ernet.in']
        SUBJECT = 'Saathi Appointment Form'
        TEXT = name +" \n "+ webmail +" \n "+ body

        # Gmail Sign In
        gmail_sender = 'saathiiitg@gmail.com'
        gmail_passwd = 'Saathi20189'

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)

        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_sender,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])

        try:
            server.sendmail(gmail_sender, TO, BODY)
            print('email sent')
        except:
            print('error sending mail')

        server.quit()
    return render(request, 'saathiweb/index.html',{'form':form})

