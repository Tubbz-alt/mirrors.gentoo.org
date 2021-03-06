from django.db import models
from mirrors.choices import STATUS_CHOICES
from international.models import Country


class Contacts(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(blank=True, verbose_name='URL')

    def __unicode__(self):
        return self.name


class ContactEmail(models.Model):
    contact = models.ForeignKey(Contacts)
    email = models.EmailField(unique=True)
    bugzilla = models.BooleanField(default=False)

    def __unicode__(self):
        return self.email


class Providers(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True)
    url = models.URLField(blank=True, verbose_name='URL')

    def __unicode__(self):
        return self.name


class MirrorAlias(models.Model):
    alias = models.CharField(max_length=255, blank=True, null=True)


class MirrorBugs(models.Model):
    number = models.IntegerField(blank=True, verbose_name="Mirror Bug")


class MirrorURL(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="URL")
    alias = models.ForeignKey(MirrorAlias, null=True)
    http = models.BooleanField(default=False, verbose_name="HTTP")
    rsync = models.BooleanField(default=False, verbose_name="Rsync")
    ftp = models.BooleanField(default=False, verbose_name="FTP")
    ipv4 = models.BooleanField(default=False, verbose_name="IPv4")
    ipv6 = models.BooleanField(default=False, verbose_name="IPv6")
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='Working')


class Mirror(models.Model):
    bugs = models.ManyToManyField(MirrorBugs, null=True)
    country = models.ForeignKey(Country)
    contacts = models.ManyToManyField(Contacts, null=True)
    provider = models.ForeignKey(Providers, null=True)

    class Meta:
        abstract = True


class PortageMirror(Mirror):
    url = models.OneToOneField(MirrorURL)


class DistfilesMirror(Mirror):
    url = models.OneToOneField(MirrorURL)
