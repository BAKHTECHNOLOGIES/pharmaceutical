from django.contrib import admin
from .models import OurTrainer,PharmaceuticalCompany,TrainingProgram,Application
admin.site.register(OurTrainer)
admin.site.register(PharmaceuticalCompany)
admin.site.register(TrainingProgram)
admin.site.register(Application)
