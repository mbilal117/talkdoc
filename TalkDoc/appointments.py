from datetime import *
import smtplib
from django.conf import settings
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import Encoders
__author__ = 'abilal'

def upload_appointment(emails, s_date, e_date):

    # from_zone = tz.gettz('UTC')
    # to_zone = tz.gettz('America/New_York')
    CRLF = "\r\n"
    login = settings.ORGANISER_EMAIL
    password = settings.ORGANISER_PASS
    attendees = []
    for emailed in emails:
        attendees.append(emailed)
    mail_to = settings.ORGANISER_EMAIL
    organizer = "ORGANIZER;CN=TalkDoc:mailto:%s" %login
    fro = "TalkDoc <%s>"%mail_to

    ddtstart = s_date - timedelta(hours=5)
    dtend = e_date - timedelta(hours=5)

    date_sen = s_date.date()
    date_sen = date_sen.strftime("%B %d, %Y")
    strt_time = s_date.time()
    end_time = e_date.time()
    dtstamp = datetime.now().strftime("%Y%m%dT%H%M%SZ")
    dtstart = ddtstart.strftime("%Y%m%dT%H%M%SZ")
    dtend = dtend.strftime("%Y%m%dT%H%M%SZ")
    description = "DESCRIPTION: Appointment Invitation"+CRLF

    attendee = ""
    for att in attendees:
        attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE"+CRLF+" ;CN="+att+";X-NUM-GUESTS=0:"+CRLF+" mailto:"+att+CRLF
    ical = "BEGIN:VCALENDAR"+CRLF+"PRODID:pyICSParser"+CRLF+"VERSION:2.0"+CRLF+"CALSCALE:GREGORIAN"+CRLF
    ical+="METHOD:REQUEST"+CRLF+"BEGIN:VEVENT"+CRLF+"DTSTART:"+dtstart+CRLF+"DTEND:"+dtend+CRLF+"DTSTAMP:"+dtstamp+CRLF+organizer+CRLF
    ical+= "UID:%s"%dtstamp+CRLF
    ical+= attendee+"CREATED:"+dtstamp+CRLF+description+"LAST-MODIFIED:"+dtstamp+CRLF+"LOCATION:"+CRLF+"SEQUENCE:0"+CRLF+"STATUS:CONFIRMED"+CRLF
    ical+= "SUMMARY:Appointment Detail"+CRLF+"END:VEVENT"+CRLF+"END:VCALENDAR"+CRLF
    # ical+="BEGIN:VTIMEZONE"+CRLF+"TZNAME:"+uc+CRLF+"END:VTIMEZONE"+CRLF
    eml_body = "<p>Hi,<br><br>You have an appointment on "+str(date_sen)+ " ,from " + str(strt_time)+" to " + str(end_time)+""
    msg = MIMEMultipart('mixed')
    msg['Reply-To'] = fro
    msg['In-Reply-To'] = eml_body
    msg['Date'] = formatdate(localtime=False)
    msg['Subject'] = "Appointment Invitation"
    msg['From'] = fro
    msg['To'] = ",".join(attendees)

    part_email = MIMEText(eml_body,"html")
    part_cal = MIMEText(ical,'calendar;method=REQUEST')
    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    ical_atch = MIMEBase('application/ics',' ;name="%s"'%("invite.ics"))
    ical_atch.set_payload(ical)
    Encoders.encode_base64(ical_atch)
    ical_atch.add_header('text/calendar', 'attachment; filename="%s"'%("invite.ics"))

    eml_atch = MIMEBase('text/plain', '')
    Encoders.encode_base64(eml_atch)
    eml_atch.add_header('Content-Transfer-Encoding', "")

    msgAlternative.attach(part_email)
    msgAlternative.attach(part_cal)

    mailServer = smtplib.SMTP('smtp.live.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(login, password)
    mailServer.sendmail(fro, attendees, msg.as_string())
    mailServer.close()



#Send Email
def send_email(name, email_to, message):

    html = """\
        <html>
        <head></head>
        <body>
        <p> """
    html = html

    try:
        user_name = settings.ORGANISER_EMAIL
        password = settings.ORGANISER_PASS
        from email.mime.text import MIMEText

        msg = MIMEMultipart()
        msg['Subject'] = "TalkDoc"
        msg['From'] = user_name
        msg['To'] = email_to

        html += """Hi """ +name+""",<br><br>"""+message+""".<br>"""
        html += """<br><br>Thanks,<br>TalkDoc Team</body></html>"""

        msg.attach(MIMEText(html, 'html'))
        import smtplib

        session = smtplib.SMTP('smtp.live.com', 587)
        session.ehlo()
        session.starttls()
        session.login(user_name, password)
        session.sendmail(user_name, email_to, msg.as_string())
        session.quit()
        return True
    except:
        return False
