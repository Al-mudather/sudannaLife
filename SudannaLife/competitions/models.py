from django.db import models
from SudannaLife.categories.models import Category
from SudannaLife.account.models import User, Country
from django.utils.translation import gettext_lazy as _
import django.utils.timezone as timeZone

######################################################
##TODO:         contest model                   ##
######################################################

class Contest(models.Model):
    ar_title = models.CharField(max_length=255)
    en_title = models.CharField(max_length=255, blank=True, null=True)
    
    ar_description = models.TextField(blank=True, null=True)
    en_description = models.TextField(blank=True, null=True)
    categories = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    logo = models.CharField(max_length=255, blank=True, null=True)
    slogan = models.CharField(max_length=255, blank=True, null=True)

    #TODO: Date Time
    start_at = models.DateTimeField(default=timeZone.now)
    end_at = models.DateTimeField(default=timeZone.now)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.ar_title or self.en_title
    
    class Meta:
        verbose_name = _('contest')
        verbose_name_plural = _('contestes')
        ordering = ('ar_title', 'en_title')

######################################################
##TODO:         measures model                      ##
######################################################
 

class Measure(models.Model):
    ar_title = models.CharField(max_length=255)
    en_title = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.ar_title or self.en_title
    
    class Meta:
        verbose_name = _('measure')
        verbose_name_plural = _('measures')
        ordering = ('ar_title', 'en_title')

######################################################
##TODO:         contest Referral model               ##
######################################################
 

class ContestReferral(models.Model):
    contest = models.ForeignKey(Contest, blank=True, null=True, on_delete=models.CASCADE)
    #TODO: Create the referal model
    # contest = models.ForeignKey(contest, blank=True, null=True, on_delete=models.CASCADE)
    weight = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.weight
    
    class Meta:
        verbose_name = _('contest Referral')
        verbose_name_plural = _('contest Referrals')
        ordering = ('weight',)

######################################################
##TODO:         contest Mesasure model                   ##
######################################################
 

class ContestMesasure(models.Model):
    contest = models.ForeignKey(Contest, blank=True, null=True, on_delete=models.CASCADE)
    measure = models.ForeignKey(Measure, blank=True, null=True, on_delete=models.CASCADE)
    weight = models.FloatField(blank=True, null=True)
    is_required = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.is_required
    
    class Meta:
        verbose_name = _('contest Mesasure')
        verbose_name_plural = _('contest Mesasures')
        ordering = ('weight',)


######################################################
##TODO:         contest goals model                  ##
######################################################
 

class ContestGoal(models.Model):
    ar_title = models.CharField(max_length=255)
    en_title = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.ar_title or self.en_title
    
    class Meta:
        verbose_name = _('contest Goal')
        verbose_name_plural = _('contest Goals')
        ordering = ('ar_title', 'en_title')

######################################################
##TODO:         contest Result model                 ##
######################################################
 

class ContestResult(models.Model):
    contest_mesasure = models.ForeignKey(ContestMesasure, blank=True, null=True, on_delete=models.CASCADE)
    #TODO: connect with the referee model
    # referee = models.ForeignKey(referee, blank=True, null=True, on_delete=models.CASCADE)
    weight = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.weight
    
    class Meta:
        verbose_name = _('contest Result')
        verbose_name_plural = _('contest Results')
        ordering = ('weight',)

class ContestAccount(models.Model):
    ar_title = models.CharField(max_length=255)
    en_title = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    slogan = models.CharField(max_length=255, blank=True, null=True)
    #TODO: Connect with the state model
    # state = models.ForeignKey(State, blank=True, null=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.ar_title or self.en_title
    
    class Meta:
        verbose_name = _('contest Account')
        verbose_name_plural = _('contest Sccounts')
        ordering = ('ar_title', 'en_title')

class Contestor(models.Model):
    fname = models.CharField(max_length=256, blank=True)
    rest_name = models.CharField(unique=True, max_length=256, blank=True)
    email = models.EmailField(blank=True, null=True)
    avatar = models.CharField(unique=True, max_length=256, blank=True)
    phone = models.CharField(unique=True, max_length=256, blank=True)
    password = models.CharField(unique=True, max_length=256, blank=True)
    
    account = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)    

    def __str__(self):
        return self.fname

    class Meta:
        verbose_name = _('Contestor')
        verbose_name_plural = _('Contestors')
        ordering = ('fname',)