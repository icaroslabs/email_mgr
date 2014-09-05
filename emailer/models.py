from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class Client(models.Model):
    email = models.EmailField(blank=True)
    slug = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    subscribe_now = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.email:
            self.slug = str(abs(hash(self.email)))
            super(Client, self).save(*args, **kwargs)
        # if self.subscribe_now:
            # Subscriber.objects.create(Client=self)

    def __unicode__(self):
        return (self.email or self.fax)


class EmailTemplate(models.Model):
    name = models.CharField(max_length=100, default='Default Email Template')
    subject = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)
    attachment = models.FileField(upload_to='upload', blank=True)

    def __unicode__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=100, default='Default Campaign')
    first_time_delta = models.IntegerField(default=2)
    second_time_delta = models.IntegerField(default=7)
    third_time_delta = models.IntegerField(default=10)
    fourth_time_delta = models.IntegerField(default=14)
    fifth_time_delta = models.IntegerField(default=14)
    ad_infinitum = models.BooleanField(default=True)
    first_email = models.ForeignKey(EmailTemplate, related_name='first_email')
    second_email = models.ForeignKey(EmailTemplate, related_name='second_email')
    third_email = models.ForeignKey(EmailTemplate, related_name='third_email')
    fourth_email = models.ForeignKey(EmailTemplate, related_name='fourth_email')
    fifth_email = models.ForeignKey(EmailTemplate, related_name='fifth_email')

    def __unicode__(self):
        return self.name


class Subscriber(models.Model):
    client = models.ForeignKey(Client, unique=True)
    campaign = models.ForeignKey(Campaign)
    join_date = models.DateField(auto_now=True)

    # first checks if client exists in companion model
    def save(self, *args, **kwargs):
        try:
            Nonsubscriber.objects.get(client=self.client)
            return
        except ObjectDoesNotExist:
            super(Subscriber, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.client)


class Nonsubscriber(models.Model):
    client = models.ForeignKey(Client, unique=True)
    leave_date = models.DateField(auto_now=True)

    # save method deletes record from companion model if it exists
    def save(self, *args, **kwargs):
        try:
            Subscriber.objects.delete(client=self.client)
        except:
            pass
        super(Subscriber, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.client)


class Spreadsheet(models.Model):
    document = models.FileField(upload_to='upload')
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.document)

