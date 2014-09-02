from django.db import models


class Spreadsheet(models.Model):
    spreadsheet = models.FileField(upload_to='not required')
    date = models.DateField(auto_now=True)

    def __unicode__(self):
        return unicode(self.date)


class EmailTemplate(models.Model):
    path = models.FilePathField()
    template = models.FileField(upload_to='not required')

    def __unicode__(self):
        return self.template


class ClientFax(models.Model):
    fax = models.CharField(max_length=14, primary_key=True)

    def __unicode__(self):
        return self.fax


class ClientEmail(models.Model):
    email = models.EmailField()
    cust_id = models.CharField(primary_key=True, max_length=50)

    def save(self, *args, **kwargs):
        self.cust_id = str(abs(hash(self.email)))
        super(ClientEmail, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    time_delta_1 = models.IntegerField()
    time_delta_2 = models.IntegerField()
    time_delta_3 = models.IntegerField()
    time_delta_4 = models.IntegerField()
    time_delta_5 = models.IntegerField()
    repeat_forver = models.BooleanField()

    def __unicode__(self):
        return self.name


class EmailSubscriber(models.Model):
    subscriber = models.ForeignKey(ClientEmail, unique=True)
    campaign = models.ForeignKey(Campaign)
    start_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.subscriber.email


class EmailNonsubscriber(models.Model):
    nonsubscriber = models.ForeignKey(ClientEmail, unique=True)

    def __unicode__(self):
        return self.nonsunscriber.email


class FaxSubscriber(models.Model):
    subscriber = models.ForeignKey(ClientFax, unique=True)
    campaign = models.ForeignKey(Campaign)
    start_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.subscriber.fax


class FaxNonsubscriber(models.Model):
    nonsubscriber = models.ForeignKey(ClientFax, unique=True)

    def __unicode__(self):
        return self.nonsunscriber.fax
