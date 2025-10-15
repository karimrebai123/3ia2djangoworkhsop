from django.contrib import admin
from .models import Conference,Submission,organizing_committe
# Register your models here.
admin.site.site_title="Gestion Conference 25/26"
admin.site.site_header="Gestion conferences"
admin.site.index_title="django App conference"
#admin.site.register(Conference)
admin.site.register(Submission)
admin.site.register(organizing_committe)

class SubmissionInline(admin.StackedInline):
    model = Submission
    extra= 1
    readonly_fields=("submission_date",)



@admin.register(Conference)
class AdminConferenceModel(admin.ModelAdmin):
    list_display=("name","theme","start_date","end_date","duration")
    ordering=("start_date",)
    list_filter=("theme",)
    search_fields=("description","name")
    date_hierarchy="start_date"
    fieldsets=(
        ("information generale",{
            "fields":("conferance_id","name","theme","description")
        }),
        ("logistics info",{
            "fields":("location","start_date","end_date")
        })
    ) 
    readonly_fields=("conferance_id",)#car conference_id est un cle primaire 
    def duration(self,objet):
        if objet.start_date and objet.end_date:
            return (objet.end_date-objet.start_date).days
        return "rien a signaler"
    duration.short_description="Duration (days)"
    inlines=[SubmissionInline]