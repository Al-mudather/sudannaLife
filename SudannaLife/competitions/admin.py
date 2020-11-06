from django.contrib import admin
from .models import (
    Contest,
    Measure,
    ContestReferral,
    ContestMesasure,
    ContestGoal,
    ContestResult,
    ContestAccount,
    Contestor
)
# Register your models here.

admin.site.register(Contest)
admin.site.register(Measure)
admin.site.register(ContestReferral)
admin.site.register(ContestMesasure)
admin.site.register(ContestGoal)
admin.site.register(ContestResult)
admin.site.register(ContestAccount)
admin.site.register(Contestor)
