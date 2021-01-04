from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Court(models.Model):
    court_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200) 
    judge_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def get_court(self, obj):
        return obj.name
    get_court.short_description = 'name'
    get_court.admin_order_field = 'court_id_name'

class Jail(models.Model):
    jail_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    vehicle_count  = models.IntegerField(default=0)
    prisoners_count = models.IntegerField(default=0)
    doctors_count = models.IntegerField(default=0)
    systems_count = models.IntegerField(default=0)
    cells_count = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    def get_jail(self, obj):
        return obj.name
    get_jail.short_description = 'name'
    get_jail.admin_order_field = 'jail_id_name'
    

class Head_Jailer(models.Model):
    head_jailer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    jail_id = models.ForeignKey(Jail, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    CHOICES = (
        ("R", "Retired"),
        ("S", "In Service"),
        ("L", "On Leave"),
        ("?", "Unknown")
    )
    status = models.CharField(
        max_length=1,
        choices=CHOICES,
        default="?"
    )
  
    date_in = models.DateTimeField()  
    date_out = models.DateTimeField() 
    username = models.CharField(max_length=200)
    password  = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="images/")
    def get_picture(self):
        return mark_safe('<img src="{}" width="100" height="100" />' .format(self.picture.url))
    get_picture.short_description = 'Image'    
    def __str__(self):
        return self.name
    def get_head_jailer(self, obj):
        return obj.name
    get_head_jailer.short_description = 'name'
    get_head_jailer.admin_order_field = 'head_jailer_id_name'


class Jailer(models.Model):
    jailer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    jail_id = models.ForeignKey(Jail, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    CHOICES = (
        ("R", "Retired"),
        ("S", "In Service"),
        ("L", "On Leave"),
        ("?", "Unknown")
    )
    status = models.CharField(
        max_length=1,
        choices=CHOICES,
        default="?"
    )
  
    date_in = models.DateTimeField() 
    date_out  = models.DateTimeField() 
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="images/")
    def get_picture(self):
        return mark_safe('<img src="{}" width="100" height="100" />' .format(self.picture.url))
    get_picture.short_description = 'Image'
    def __str__(self):
        return self.name
    def get_jailer(self, obj):
        return obj.name
    get_jailer.short_description = 'name'
    get_jailer.admin_order_field = 'jailer_id_name'


class Prisoner(models.Model):
    prisoner_id = models.AutoField(primary_key=True)
    prisoner_number = models.IntegerField()
    picture = models.ImageField(upload_to="images/")
    def get_picture(self):
        return mark_safe('<img src="{}" width="100" height="100" />' .format(self.picture.url))
    get_picture.short_description = 'Image'
    jail_id = models.ForeignKey(Jail, on_delete=models.CASCADE)
    name  = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_in = models.DateTimeField() 
    date_out = models.DateTimeField() 
    CHOICES = (
        ("J", "In Jail"),
        ("D", "Dead"),
        ("R", "Realeased"),
        ("L", "On Lose"),
        ("?","Unknown")
    )
    status = models.CharField(
        max_length=1,
        choices=CHOICES,
        default="?"
    )
   
    crime_detail = models.CharField(max_length=2000)
    case_no = models.CharField(max_length=200)
    act = models.CharField(max_length=200)
    punishment_type = models.CharField(max_length=200)
    luggage = models.CharField(max_length=200)
    height = models.FloatField() 
    weight = models.FloatField() 
    mental_health = models.CharField(max_length=200)
    behaviour = models.CharField(max_length=200)
    police_station = models.CharField(max_length=200)
    privious_records = models.CharField(max_length=20000)
    def __str__(self):
        return str(self.prisoner_number)
    def get_prisoner_num(self, obj):
        return obj.prisoner_number
    get_prisoner_num.short_description = 'prisoner_number'
    get_prisoner_num.admin_order_field = 'prisoner_id_number'


class Doctor(models.Model):  
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="images")
    def get_picture(self):
        return mark_safe('<img src="{}" width="100" height="100" />' .format(self.picture.url))
    get_picture.short_description = 'Image'
    def __str__(self):
        return self.name


class Visitor(models.Model):
    visitor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(
        max_length=1,
        choices=CHOICES,
        default="?"
    )
    address = models.CharField(max_length=2000)
    picture = models.ImageField(upload_to="images/")
    def get_picture(self):
        return mark_safe('<img src="{}" width="100" height="100" />' .format(self.picture.url))
    get_picture.short_description = 'Image'
    def __str__(self):
        return self.name

class prisoner_hearings(models.Model):
    prisoner_hearing_id = models.AutoField(primary_key=True)
    prisoner_id = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    def get_Prisoner_id(self):
        return self.prisoner_id
    get_Prisoner_id.short_description = 'Prisoner ID'
    court_id = models.ForeignKey(Court, on_delete=models.CASCADE)
    def get_court_id(self):
        return self.court_id
    get_court_id.short_description = 'Court ID'
    jailer_id = models.ForeignKey(Jailer, on_delete=models.CASCADE)
    def get_ailer_id(self):
        return self.jailer_id
    get_ailer_id.short_description = 'Jailer ID'
    head_jailer_id = models.ForeignKey(Head_Jailer, on_delete=models.CASCADE)
    def get_head_jailer_id(self):
        return self.head_jailer_id 
    get_head_jailer_id.short_description = 'Head Jailer ID'
    time_out = models.DateTimeField() 
    time_in = models.DateTimeField() 
    CHOICES = (
        ("C", "Canceled"),
        ("D", "Done"),
        ("L", "Late"),
        ("?","Unknown")
    )
    status = models.CharField(
        max_length=1,
        choices=CHOICES,
        default="?"
    )
    court_orders = models.CharField(max_length=2000)
    details = models.CharField(max_length=2000)
    

class prisoner_medications(models.Model):
    prisoner_medications_id = models.AutoField(primary_key=True)
    prisoner_id = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    def get_Prisoner_id(self):
        return self.prisoner_id
    get_Prisoner_id.short_description = 'Prisoner ID'
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def get_doctor_id(self):
        return self.doctor_id
    get_doctor_id.short_description = 'Doctor ID'
    time_in   = models.DateTimeField() 
    time_out = models.DateTimeField() 
    doctor_advise = models.CharField(max_length=200)
    health_issue = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    jail_incharge_id = models.ForeignKey(Jailer, on_delete=models.CASCADE)
    def get_jail_incharge_id(self):
        return self.jail_incharge_id
    get_jail_incharge_id.short_description = 'Jail Incharge ID'

class prisoner_hospital_visits(models.Model):
    prisoner_hospital_visit_id = models.AutoField(primary_key=True)
    prisoner_id = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    def get_Prisoner_id(self):
        return self.prisoner_id
    get_Prisoner_id.short_description = 'Prisoner ID'
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def get_doctor_id(self):
        return self.doctor_id
    get_doctor_id.short_description = 'Doctor ID'
    time_in   = models.DateTimeField() 
    time_out = models.DateTimeField() 
    doctor_advise = models.CharField(max_length=200)
    health_issue = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    hospital = models.CharField(max_length=200)
    jail_incharge_id = models.ForeignKey(Jailer, on_delete=models.CASCADE)
    def get_jail_incharge_id(self):
        return self.jail_incharge_id
    get_jail_incharge_id.short_description = 'Jail Incharge ID'


class prisoner_meetings(models.Model):
    prisoner_meetings_id = models.AutoField(primary_key=True)
    prisoner_id = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    def get_Prisoner_id(self):
        return self.prisoner_id
    get_Prisoner_id.short_description = 'Prisoner ID'
    visitor_id = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    def get_visitor_id(self):
        return self.prisoner_id
    get_visitor_id.short_description = 'Visitor ID'
    time_in = models.DateTimeField() 
    time_out = models.DateTimeField() 
    details  = models.CharField(max_length=200)
    luggage = models.CharField(max_length=200)
    jail_incharge_id  = models.ForeignKey(Jailer, on_delete=models.CASCADE)
    def get_jail_incharge_id(self):
        return self.jail_incharge_id
    get_jail_incharge_id.short_description = 'Jail Incharge ID'
    relation = models.CharField(max_length=200)
    CHOICES = (
        ("D", "Complete"),
        ("P", "Pending"),
        ("C", "Canceled"),
        ("?","Unknown")
    )
    status = models.CharField(
        max_length=1,
        choices=CHOICES,
        default="?"
    )

class prisoner_jail_shiftiting(models.Model):
    prisoner_jail_shiftiting_id = models.AutoField(primary_key=True)
    prisoner_id = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    def get_Prisoner_id(self):
        return self.prisoner_id
    get_Prisoner_id.short_description = 'Prisoner ID'
    previous_jail_id = models.ForeignKey(Jail, null=True, related_name='previous_jail_id', on_delete=models.CASCADE)
    def get_previous_jail_id(self):
        return self.previous_jail_id
    get_previous_jail_id.short_description = 'Privious Jail ID'
    new_jail_id = models.ForeignKey(Jail, on_delete=models.CASCADE,related_name='new_jail_id')
    def get_new_jail_id(self):
        return self.new_jail_id 
    get_new_jail_id .short_description = 'New Jail ID'
    court_id = models.ForeignKey(Court, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=200)
    carrier = models.CharField(max_length=200)
    jail_incharge_id = models.ForeignKey(Jailer, on_delete=models.CASCADE)
    def get_jail_incharge_id(self):
        return self.jail_incharge_id
    get_jail_incharge_id.short_description = 'Jail Incharge ID'
    CHOICES = (
        ("D", "Complete"),
        ("P", "Pending"),
        ("C", "Canceled"),
        ("?","Unknown")
    )
    status = models.CharField(
        max_length=1,
        choices=CHOICES,
        default="?"
    )

class prisoner_complaints(models.Model):
    complain_id = models.AutoField(primary_key=True)
    complain_by = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    def get_Complain_by(self):
        return self.complain_by
    get_Complain_by.short_description = 'Complain By'

    complain_details = models.CharField(max_length=2000)
    Date_of_complain = models.DateTimeField() 
    Date_of_complain_reolved = models.DateTimeField() 
    CHOICES = (
        ("R", "Resolved"),
        ("P", "Pending"),
        ("C", "Canceled"),
        ("?","Unknown")
    )
    status = models.CharField(
        max_length=1,
        choices=CHOICES,
        default="?"
    )
    resolved_by = models.ForeignKey(Jailer, on_delete=models.CASCADE)
    def get_resolved_by(self):
        return str(self.resolved_by)
    get_resolved_by.short_description = 'Complaint Resolved BY'
    def __str__(self):
        return self.complain_by

class prisoner_earnings(models.Model):
    earning_id = models.AutoField(primary_key=True)
    prisoner_id = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    def get_Prisoner_id(self):
        return str(self.prisoner_id)
    get_Prisoner_id.short_description = 'Prisoner ID'
    Date = models.DateTimeField()
    money  = models.IntegerField(default=0)
    work_details = models.CharField(max_length=2000)
    def __str__(self):
        return str(self.prisoner_id)
  

