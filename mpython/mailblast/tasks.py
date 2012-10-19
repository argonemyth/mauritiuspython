from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context
from celery import task
import smtplib
from time import sleep
from mailblast.models import Email, SentLog

@task()
def send_newsletter(email):
    """
    The task accepts an email and send it to all the subscribers in
    the newsletter.
    """
    email.change_status(3)
    sender = email.newsletter.get_sender()
    
    # Get contents ready
    # text_template, html_template = email.get_templates()
    text_template = "mailblast/invite.txt"
    html_template = "mailblast/invite.html"
    d = Context({ 'email': email })
    t = loader.get_template(text_template)
    # text_content = t.render(email.content)
    text_content = t.render(d)
    t = loader.get_template(html_template)
    #html_content = t.renderd(email.content)
    html_content = t.render(d)

    """
    if email.image:
        t = loader.get_template("emails/mailblast.html")
        c = Context({'image_url': settings.IMAGE_HOST+str(email.image.url)})
        html_content = t.render(c) 
    else:
        html_content = None
    """

    total_subscribers = str(email.newsletter.subscription.count())
    composer = email.newsletter.get_sender()
    listname = email.newsletter.title
    #blast_logger.info('Mailblast %s to %s started, from %s, %s recipients on the list, sent as %s.' % (email.subject, listname, composer, email_count, str(email.sender)))
    #mail_admins('Blast Started', composer + " is going to send " + email_count+ " emails from " + listname + " as " + str(email.sender))
    print 'Mailblast %s to %s started, from %s, %s recipients on the list.' % (email.subject, listname, composer, total_subscribers)

    for subscription in email.newsletter.subscription.select_related():
        recipient = subscription.get_recipient()
        try:
            email.send_log.get(to__iexact=subscription.email)
        except: 
            try:
                msg = EmailMultiAlternatives(email.subject, text_content, 
                                             sender, [recipient])
                msg.attach_alternative(html_content, "text/html")
                """
                if html_content:
                    msg.attach_alternative(html_content, "text/html")
                elif email.file:
                    msg.attach_file(email.file.path)
                """
                msg.send()
                db_log = SentLog(email=email, to=subscription.email, result=1)
                db_log.save()
                #blast_logger.info(to_email.infoValue + " - Email Sent")
                print subscription.email + " - Email Sent"
                sleep(30)
            except (smtplib.SMTPSenderRefused, smtplib.SMTPRecipientsRefused, smtplib.SMTPAuthenticationError), err:
                #EmailLog.objects.log(email, to_email.infoValue, 2, log_message=str(err))
                db_log = SentLog(email=email, to=subscription.email, result=2,
                                 log_message=str(err))
                db_log.save()
                #blast_logger.error("%s - Failer %s" % (to_email.infoValue, err))
                print "%s - Failer %s" % (subscription.email, err)
            except Exception as e:
                #EmailLog.objects.log(email, to_email.infoValue, 4, log_message=u"Unknown error %s" % (str(e)))
                db_log = SentLog(email=email, to=subscription.email, result=4,
                                 log_message=u"Unknown error %s" % (str(e)))
                db_log.save()
                #blast_logger.error("%s - Unknown Failer %s" % (to_email.infoValue, e))
                print "%s - Unknown Failer %s" % (subscription.email, e)
        else:       
            #blast_logger.info(to_email.infoValue + " - Already Sent")
            print subscription.email + " - Already Sent"

    #blast_logger.info('Mailblast %s to %s is ended.' % (email.subject, listname))
    print 'Mailblast %s to %s is ended.' % (email.subject, listname)
    return True
