from django.contrib import admin

# Register your models here.

from . models import register_table,student_table,teachingstaff_table,nonteachingstaff_table,researchdepartment_table,internationalrelations_table

admin.site.register(register_table)
admin.site.register(student_table)
admin.site.register(teachingstaff_table)
admin.site.register(nonteachingstaff_table)
admin.site.register(researchdepartment_table)
admin.site.register(internationalrelations_table)



