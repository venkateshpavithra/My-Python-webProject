from django.db import models

# Create your models here.
class register_table(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    password=models.CharField(max_length=20)
    profile_picture=models.FileField(upload_to='documents')
    
    
    def __str__(self):
        return self.first_name+" "+self.last_name
    
    
class student_table(models.Model):
    student_name=models.CharField(max_length=100)
    roll_number=models.CharField(max_length=100)
    email_id=models.EmailField()
    department=models.CharField(max_length=100)
    mobile_number=models.CharField(max_length=100)
    student_batch=models.CharField(max_length=100)
    logger_id=models.IntegerField()
    
    def __str__(self):
        return self.roll_number
    
class teachingstaff_table(models.Model):
    name_of_the_faculty=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    email_id=models.EmailField()
    logger_id=models.IntegerField()
    
      
    def __str__(self):
        return self.name_of_the_faculty
    
    
class nonteachingstaff_table(models.Model):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    qualification=models.EmailField()
    age=models.CharField(max_length=100)
    pay_level=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    logger_id=models.IntegerField()
    
    def __str__(self):
        return self.name
    
class researchdepartment_table(models.Model):
    name_of_the_principle_investigator=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    sanctioned_letter_number_with_date=models.CharField(max_length=100)
    project_title=models.CharField(max_length=100)
    duration_of_the_project=models.CharField(max_length=100)
    total_sanctioned_amount=models.CharField(max_length=100)
    logger_id=models.IntegerField()
    
    def __str__(self):
        return self.project_title
    
    
class internationalrelations_table(models.Model):
    name_of_the_student=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    academic_year=models.CharField(max_length=100)
    roll_number=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    mobile_number=models.CharField(max_length=100)
    logger_id=models.IntegerField()
    
    def __str__(self):
        return self.email_id
    
    
    
    
    
    
    
    
    