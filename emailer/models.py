from django.db import models


class Client(models.Model):
    email = models.EmailField()
    slug = models.CharField(max_length=50)
    fax = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if self.email and self.email != '':
            self.slug = str(abs(hash(self.email)))
            super(Client, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email


class EmailTemplate(models.Model):
    name = models.CharField(max_length=100)
    html = models.TextField()

    def __unicode__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    time_delta_1 = models.IntegerField()
    time_delta_2 = models.IntegerField()
    time_delta_3 = models.IntegerField()
    time_delta_4 = models.IntegerField()
    time_delta_5 = models.IntegerField()
    ad_infinitum = models.BooleanField()
    email_template_1 = models.ForeignKey(EmailTemplate)
    email_template_2 = models.ForeignKey(EmailTemplate)
    email_template_3 = models.ForeignKey(EmailTemplate)
    email_template_4 = models.ForeignKey(EmailTemplate)
    email_template_5 = models.ForeignKey(EmailTemplate)

    def __unicode__(self):
        return self.name


class Subscriber(models.Model):
    client = models.ForeignKey(Client, unique=True)
    campaign = models.ForeignKey(Campaign)
    join_date = models.DateField(auto_now=True)


class Nonsubscriber(models.Model):
    client = models.ForeignKey(Client, unique=True)
    leave_date = models.DateField(auto_now=True)

