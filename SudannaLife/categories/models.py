from django.db import models

######################################################
##TODO:         category model                   ##
######################################################
 

class category(models.Model):
    #TODO: Customer information
    ar_title = models.CharField(max_length=255)
    en_title = models.CharField(max_length=255, blank=True, null=True)
    
    ar_description = models.TextField(blank=True, null=True)
    en_description = models.TextField(blank=True, null=True)

    #TODO: Date Time
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.ar_title or self.en_title
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('ar_title','en_title')
