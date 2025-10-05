from django.contrib import admin
from .models import Experience, Education, Certificate

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'is_current', 'order')
    list_filter = ('is_current',)
    ordering = ('order', '-start_date')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year')
    ordering = ['-year']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'issue_date')
    list_filter = ('issuer',)
    ordering = ['-issue_date']