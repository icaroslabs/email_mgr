from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class EmailTemplate(models.Model):
    name = models.CharField(max_length=100, default='Default Email Template')
    subject = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)
    attachment = models.FileField(upload_to='upload', blank=True)

    def __unicode__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=100, default='Default Campaign', unique=True)
    # num days from subscriber.start_date; see scripts/emailer.py
    first_time_delta = models.IntegerField(default=2)
    second_time_delta = models.IntegerField(default=7)
    third_time_delta = models.IntegerField(default=10)
    fourth_time_delta = models.IntegerField(default=14)
    fifth_time_delta = models.IntegerField(default=28)
    ad_infinitum = models.BooleanField(default=True)
    first_email = models.ForeignKey(EmailTemplate, related_name='first_email', blank=True)
    second_email = models.ForeignKey(EmailTemplate, related_name='second_email', blank=True)
    third_email = models.ForeignKey(EmailTemplate, related_name='third_email', blank=True)
    fourth_email = models.ForeignKey(EmailTemplate, related_name='fourth_email', blank=True)
    fifth_email = models.ForeignKey(EmailTemplate, related_name='fifth_email', blank=True)

    def __unicode__(self):
        return self.name


class Client(models.Model):
    email = models.EmailField(blank=True)
    slug = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    subscribe_now = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.email:
            self.slug = str(abs(hash(self.email)))
            super(Client, self).save(*args, **kwargs)
        if self.subscribe_now:
            # client = Client.objects.get()
            campaign = Campaign.objects.get(name='Default Campaign')
            Subscriber.objects.create(client=self, campaign=campaign)

    def __unicode__(self):
        return (self.email or self.fax)


class Subscriber(models.Model):
    client = models.ForeignKey(Client, unique=True)
    campaign = models.ForeignKey(Campaign)
    join_date = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=100, blank=True)
    last_delta = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.url = "http://drssrealestate.com/unsubscribe/%s" % self.client.slug
        super(Subscriber, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.client)


class Spreadsheet(models.Model):
    document = models.FileField(upload_to='upload')
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.document)

