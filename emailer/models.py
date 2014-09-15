from django.db import models


class EmailTemplate(models.Model):
    name = models.CharField(max_length=100, default='Default Email Template')
    subject = models.CharField(max_length=100, blank=True)
    text = models.TextField(blank=True)
    html = models.TextField(blank=True)
    attachment = models.FileField(upload_to='uploads', blank=True)

    def __unicode__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=100, default='Default Campaign', unique=True)

    def __unicode__(self):
        return self.name



class TimeDelta(models.Model):
    campaign = models.ForeignKey(Campaign)
    email = models.ForeignKey(EmailTemplate)
    delta = models.IntegerField()

    def __unicode__(self):
        return ": ".join(['Day '+str(self.delta), self.email.name])


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
            campaign = Campaign.objects.get(name='Default Campaign')
            Subscriber.objects.create(client=self, campaign=campaign)

    def __unicode__(self):
        return (self.email or self.fax)


class Subscriber(models.Model):
    client = models.OneToOneField(Client, unique=True)
    campaign = models.ForeignKey(Campaign)
    join_date = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=100, blank=True)
    last_delta = models.IntegerField(default=0)
    last_activity = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.url = "http://drssrealestate.com/unsubscribe/%s" % self.client.slug
        super(Subscriber, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.client)


class Spreadsheet(models.Model):
    document = models.FileField(upload_to='uploads')
    date = models.DateTimeField(auto_now=True)
    campaign = models.ForeignKey(Campaign)

    def __unicode__(self):
        return str(self.document)

