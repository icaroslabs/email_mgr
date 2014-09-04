from django.db import models


class Client(models.Model):
    email = models.EmailField(blank=True)
    slug = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        if self.email:
            self.slug = str(abs(hash(self.email)))
            super(Client, self).save(*args, **kwargs)

    def __unicode__(self):
        return (self.email or self.fax)


class EmailTemplate(models.Model):
    name = models.CharField(max_length=100)
    html = models.TextField()

    def __unicode__(self):
        return self.name


class TimeDelta(models.Model):
    name = models.CharField(max_length=100)
    delta = models.IntegerField()
    email = models.ForeignKey(EmailTemplate)

    def __unicode__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    first_delta = models.ForeignKey(TimeDelta, related_name='first_delta')
    second_delta = models.ForeignKey(TimeDelta, related_name='second_delta')
    third_delta = models.ForeignKey(TimeDelta, related_name='third_delta')
    fourth_delta = models.ForeignKey(TimeDelta, related_name='fourth_delta')
    fifth_delta = models.ForeignKey(TimeDelta, related_name='fifth_delta')
    ad_infinitum = models.BooleanField()

    def __unicode__(self):
        return self.name


class Subscriber(models.Model):
    client = models.ForeignKey(Client, unique=True)
    campaign = models.ForeignKey(Campaign)
    join_date = models.DateField(auto_now=True)

    # first checks if client exists in companion model
    def save(self, *args, **kwargs):
        if not Nonsubscriber.objects.get(client=self.client):
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
