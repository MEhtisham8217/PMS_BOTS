from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Court,Jail,Head_Jailer,Jailer,Prisoner,Doctor,Visitor,prisoner_herarings,prisoner_jail_shiftiting,prisoner_medications,prisoner_meetings


class CourtAdmin(admin.ModelAdmin):
    list_display = ("name","location","judge_name")
    search_fields = ("name",)
    list_filter = ('location',)

class JailAdmin(admin.ModelAdmin):
    list_display = ("name","location","prisoners_count","doctors_count","systems_count","vehicle_count","cells_count")
    search_fields = ("name",)
    list_filter = ('prisoners_count',)


class Head_JailerAdmin(admin.ModelAdmin):
    list_display = ("name","address","jail_id","status","get_picture")
    list_editable = ("status",)
    readonly_fields = ('get_picture',)
    search_fields = ("name",)
    list_filter = ('status',)


class JailerAdmin(admin.ModelAdmin):
    list_display = ("name","address","jail_id","status","get_picture")
    list_editable = ("status",)
    search_fields = ("name",)
    list_filter = ('status',)
    readonly_fields = ('get_picture',)

class PrisonerAdmin(admin.ModelAdmin):
    list_display = ("prisoner_number","name","address","jail_id","status","get_picture")
    list_editable = ("status",)
    search_fields = ("Prisoner_number",)
    list_filter = ('status','jail_id',)
    readonly_fields = ('get_picture',)

class DoctorAdmin(admin.ModelAdmin):  
    list_display = ("name","address","get_picture")
    search_fields = ("name",)
    list_filter = ('address',)
    readonly_fields = ('get_picture',)

class VisitorAdmin(admin.ModelAdmin):  
    list_display = ("name","address","get_picture")
    search_fields = ("name",)
    list_filter = ('address',)
    readonly_fields = ('get_picture',)

class Prisoner_hearing_Admin(admin.ModelAdmin): 
    model = prisoner_herarings 
    list_display = ("get_Prisoner_id","get_court_id","time_out","time_in","status","court_orders")
    list_editable = ("status",)
    search_fields = ("Prisoner_id",)
    

class Prisoner_medication_Admin(admin.ModelAdmin):  
    list_display = ("get_Prisoner_id","get_doctor_id","time_out","time_in","doctor_advise")
    search_fields = ("Prisoner_id",)

class Prisoner_meetings_Admin(admin.ModelAdmin):  
    list_display = ("get_Prisoner_id","get_visitor_id","time_out","time_in","relation","status")
    list_editable = ("status",)
    search_fields = ("Prisoner_id",)

class prisoner_jail_shiftiting_Admin(admin.ModelAdmin):  
    list_display = ("get_Prisoner_id","get_previous_jail_id","get_new_jail_id","purpose","carrier","status")
    list_editable = ("status",)
    search_fields = ("Prisoner_id",)


admin.site.register(Court,CourtAdmin)
admin.site.register(Jail,JailAdmin)
admin.site.register(Head_Jailer,Head_JailerAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Jailer,JailerAdmin)
admin.site.register(Prisoner,PrisonerAdmin)
admin.site.register(Visitor,VisitorAdmin)
admin.site.register(prisoner_herarings,Prisoner_hearing_Admin)
admin.site.register(prisoner_medications,Prisoner_medication_Admin)
admin.site.register(prisoner_meetings,Prisoner_meetings_Admin)
admin.site.register(prisoner_jail_shiftiting,prisoner_jail_shiftiting_Admin)

