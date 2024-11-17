from django.shortcuts import render
from . models import register_table,student_table,teachingstaff_table,nonteachingstaff_table,researchdepartment_table,internationalrelations_table
from django.contrib import messages,auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
 
def register_form_submission(request):
    if request.method=='POST':
        if register_table.objects.filter(email_id=request.POST['email_id']):
            messages.error(request,'sorry this mail id has already taken',extra_tags='taken')
            return render(request, 'register.html') 
        else:
            ex1=register_table(first_name=request.POST.get('first_name'),
                               last_name=request.POST.get('last_name'),
                               email_id=request.POST.get('email_id'),
                               password=request.POST.get('password'))
                               
            if len(request.FILES) != 0:
                ex1.profile_picture = request.FILES.get('profile_picture')
            ex1.save()
            messages.error(request,'successfully registered',extra_tags='success')
            return render(request,'login.html')
        
        def login(request):
            return render(request,'login.html')
           
def login_form_submission(request):
    if register_table.objects.filter(email_id=request.POST['email_id'],password=request.POST['password']).exists():
        logger_data=register_table.objects.get(email_id=request.POST['email_id'],password=request.POST['password'])
        return render(request,'index2.html',{'logger_data':logger_data})
    else:
        messages.error(request,'sorry please check your username or password',extra_tags='failed')
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return render(request,'login.html')
            
def index2(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'index2.html',{'logger_data':logger_data})

def student(request,id):
    logger_data=register_table.objects.get(id=id)
    view_data=student_table.objects.filter(logger_id=id)
    return render(request,'student.html',{'logger_data':logger_data,'view_data':view_data})
    
def studentaddlist(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'studentaddlist.html',{'logger_data':logger_data})

def add_student_form_submission(request,id):
     logger_data=register_table.objects.get(id=id)
     ex1=student_table(student_name=request.POST.get('student_name'),
                        roll_number=request.POST.get('roll_number'),
                        email_id=request.POST.get('email_id'),
                        department=request.POST.get('department'),
                        mobile_number=request.POST.get('mobile_number'),
                        student_batch=request.POST.get('student_batch'),
                        logger_id=id)
     
     ex1.save()
     messages.error(request,'successfully added',extra_tags='success')
     view_data=student_table.objects.filter(logger_id=id)
     return render(request,'student.html',{'logger_data':logger_data,'view_data':view_data})
    


def StudentEdit(request,id,row_id):
    logger_data=register_table.objects.get(id=id)
    student_data=student_table.objects.get(id=row_id)
    return render(request,'StudentEdit.html',{'logger_data':logger_data,'student_data':student_data})

def edit_student_data_form_submission(request,id,row_id):
     logger_data=register_table.objects.get(id=id)
     student_data=student_table.objects.get(id=row_id)
     view_data=student_table.objects.filter(logger_id=id)
     
     ex1=student_table.objects.filter(id=row_id).update(student_name=request.POST.get('student_name'),
                        roll_number=request.POST.get('roll_number'),
                        email_id=request.POST.get('email_id'),
                        department=request.POST.get('department'),
                        mobile_number=request.POST.get('mobile_number'),
                        student_batch=request.POST.get('student_batch'),
                        logger_id=id)
     
     messages.error(request,'successfully updated',extra_tags='success')
     return render(request,'student.html',{'view_data':view_data,'logger_data':logger_data,'student_data':student_data})

def delete_student_data(request,id,row_id):
    logger_data=register_table.objects.get(id=id)
    view_data=student_table.objects.filter(logger_id=id)
    student_data=student_table.objects.get(id=row_id)
    student_data.delete()
    
    messages.error(request,'deleted successfully',extra_tags='success')
    return render(request,'Student.html',{'view_data':view_data,'logger_data':logger_data,'student_data':student_data})

    

def Teachingstaff(request,id):
    logger_data=register_table.objects.get(id=id)
    view_data=teachingstaff_table.objects.filter(logger_id=id)
    return render(request,'Teachingstaff.html',{'logger_data':logger_data,'view_data':view_data})


def teachingstaffadd(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'teachingstaffadd.html',{'logger_data':logger_data})


def add_teachingstaff_form_submission(request,id):
     logger_data=register_table.objects.get(id=id)
     ex1=teachingstaff_table(name_of_the_faculty=request.POST.get('name_of_the_faculty'),
                        designation=request.POST.get('designation'),
                        qualification=request.POST.get('qualification'),
                        department=request.POST.get('department'),
                        age=request.POST.get('age'),
                        experience=request.POST.get('experience'),
                        email_id=request.POST.get('email_id'),
                        logger_id=id)
     
     ex1.save()
     messages.error(request,'successfully added',extra_tags='success')
     view_data=teachingstaff_table.objects.filter(logger_id=id)
     return render(request,'Teachingstaff.html',{'logger_data':logger_data,'view_data':view_data})


def TeachingStaffEdit(request,id,row_id):
    logger_data=register_table.objects.get(id=id)
    teachingstaff_data=teachingstaff_table.objects.get(id=row_id)
    return render(request,'TeachingStaffEdit.html',{'logger_data':logger_data,'teachingstaff_data':teachingstaff_data})

def edit_teachingstaff_data_form_submission(request,id,row_id):
     logger_data=register_table.objects.get(id=id)
     teachingstaff_data=teachingstaff_table.objects.get(id=row_id)
     view_data=teachingstaff_table.objects.filter(logger_id=id)
     
     ex1=teachingstaff_table.objects.filter(id=row_id).update(name_of_the_faculty=request.POST.get('name_of_the_faculty'),
                        designation=request.POST.get('designation'),
                        qualification=request.POST.get('qualification'),
                        department=request.POST.get('department'),
                        age=request.POST.get('age'),
                        experience=request.POST.get('experience'),
                        email_id=request.POST.get('email_id'),
                        logger_id=id)
     
     messages.error(request,'successfully updated',extra_tags='success')
     return render(request,'Teachingstaff.html',{'view_data':view_data,'logger_data':logger_data,'teachingstaff_data':teachingstaff_data})

def delete_teachingstaff_data(request,id,row_id):
    logger_data=register_table.objects.get(id=id)
    view_data=teachingstaff_table.objects.filter(logger_id=id)
    teachingstaff_data=teachingstaff_table.objects.get(id=row_id)
    teachingstaff_data.delete()
    
    messages.error(request,'deleted successfully',extra_tags='success')
    return render(request,'Teachingstaff.html',{'view_data':view_data,'logger_data':logger_data,'teachingstaff_data':teachingstaff_data})


def nonteachingstaff(request,id):
    logger_data=register_table.objects.get(id=id)
    view_data=nonteachingstaff_table.objects.filter(logger_id=id)
    return render(request,'nonteachingstaff.html',{'logger_data':logger_data,'view_data':view_data})


def nonteachingstaffadd(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'nonteachingstaffadd.html',{'logger_data':logger_data})


def add_nonteachingstaff_form_submission(request,id):
     logger_data=register_table.objects.get(id=id)
     ex1=nonteachingstaff_table(name=request.POST.get('name'),
                        designation=request.POST.get('designation'),
                        qualification=request.POST.get('qualification'),
                        age=request.POST.get('age'),
                        pay_level=request.POST.get('pay_level'),
                        salary=request.POST.get('salary'),
                        logger_id=id)
     
     ex1.save()
     messages.error(request,'successfully added',extra_tags='success')
     view_data=nonteachingstaff_table.objects.filter(logger_id=id)
     return render(request,'nonteachingstaff.html',{'logger_data':logger_data,'view_data':view_data})
 

def nonteachingstaffedit(request,id,row_id):
    logger_data=register_table.objects.get(id=id)
    nonteachingstaff_data=nonteachingstaff_table.objects.get(id=row_id)
    return render(request,'nonteachingStaffEdit.html',{'logger_data':logger_data,'nonteachingstaff_data':nonteachingstaff_data})
    
     
def edit_nonteachingstaff_data_form_submission(request,id,row_id):
     logger_data=register_table.objects.get(id=id)
     nonteachingstaff_data=nonteachingstaff_table.objects.get(id=row_id)
     view_data=nonteachingstaff_table.objects.filter(logger_id=id)
     
     ex1=nonteachingstaff_table.objects.filter(id=row_id).update(name=request.POST.get('name'),
                        designation=request.POST.get('designation'),
                        qualification=request.POST.get('qualification'),
                        age=request.POST.get('age'),
                        pay_level=request.POST.get('pay_level'),
                        salary=request.POST.get('salary'),
                        logger_id=id)
     
     messages.error(request,'successfully updated',extra_tags='success')
     return render(request,'nonteachingstaff.html',{'view_data':view_data,'logger_data':logger_data,'nonteachingstaff_data':nonteachingstaff_data})

def delete_nonteachingstaff_data(request,id,row_id):
    logger_data=register_table.objects.get(id=id)
    view_data=nonteachingstaff_table.objects.filter(logger_id=id)
    nonteachingstaff_data=nonteachingstaff_table.objects.get(id=row_id)
    nonteachingstaff_data.delete()
    
    messages.error(request,'deleted successfully',extra_tags='success')
    return render(request,'nonteachingstaff.html',{'view_data':view_data,'logger_data':logger_data,'nonteachingstaff_data':nonteachingstaff_data})


 #def AdmissionDepartment(request):
    return render(request,'AdmissionDepartment.html')
 #def AdmissionEdit(request):
    return render(request,'AdmissionEdit.html')
 #def PlacementAndTrainingCell(request):
    return render(request,'PlacementAndTrainingCell.html')
 #def PlacementandTrainingEdit(request):
    return render(request,'PlacementandTrainingEdit.html')
 #def Departments(request):
    return render(request,'Departments.html')
 #def DepartmentEdit(request):
    return render(request,'DepartmentEdit.html')
 #def Laboratory(request):
    return render(request,'Laboratory.html')
 #def LaboratoryEdit(request):
    return render(request,'LaboratoryEdit.html')
 #def swo(request):
    return render(request,'swo.html')
 #def swoEdit(request):
    return render(request,'swoEdit.html')
 #def exam(request):
    return render(request,'exam.html')
 #def examEdit(request):
    return render(request,'examEdit.html')
 #def paymentdepartment(request):
    return render(request,'paymentdepartment.html')
 #def PaymentDepartmentEdit(request):
    return render(request,'PaymentDepartmentEdit.html')
 #def GamesandNGO(request):
    return render(request,'GamesandNGO.html')
 #def GamesandNGOedit(request):
    return render(request,'GamesandNGOedit.html')
 #def Nationalcadetcorps(request):
    return render(request,'Nationalcadetcorps.html')
 #def NationalcadetcorpsEdit(request):
    return render(request,'NationalcadetcorpsEdit.html')
 #def DispensaryRoom(request):
    return render(request,'DispensaryRoom.html')
 #def DispensaryEdit(request):
    return render(request,'DispensaryEdit.html')
 #def NewsandArticle(request):
    return render(request,'NewsandArticle.html')
 #def NewsandArticleEdit(request):
    return render(request,'NewsandArticleEdit.html')

def InternationalRelations(request,id):
    logger_data=register_table.objects.get(id=id)
    view_data=internationalrelations_table.objects.filter(logger_id=id)
    return render(request,'InternationalRelations.html',{'logger_data':logger_data,'view_data':view_data})


def internationalrelationsadd(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'internationalrelationsadd.html',{'logger_data':logger_data})


def add_internationalrelations_form_submission(request,id):
     logger_data=register_table.objects.get(id=id)
     ex1=internationalrelations_table(name_of_the_student=request.POST.get('name_of_the_student'),
                        department=request.POST.get('department'),
                        academic_year=request.POST.get('academic_year'),
                        roll_number=request.POST.get('roll_number'),
                        email_id=request.POST.get('email_id'),
                        mobile_number=request.POST.get('mobile_number'),
                        logger_id=id)
     
     ex1.save()
     messages.error(request,'successfully added',extra_tags='success')
     view_data=internationalrelations_table.objects.filter(logger_id=id)
     return render(request,'InternationalRelations.html',{'logger_data':logger_data,'view_data':view_data})


def InternationalRelationsEdit(request,id,row_id):
    logger_data=register_table.objects.get(id=id)
    internationalrelations_data=internationalrelations_table.objects.get(id=row_id)
    return render(request,'InternationalRelationsEdit.html',{'logger_data':logger_data,'internationalrelations_data':internationalrelations_data})
    
     
def edit_internationalrelations_data_form_submission(request,id,row_id):
     logger_data=register_table.objects.get(id=id)
     internationalrelations_data=internationalrelations_table.objects.get(id=row_id)
     view_data=internationalrelations_table.objects.filter(logger_id=id)
     
     ex1=internationalrelations_table.objects.filter(id=row_id).update(name_of_the_student=request.POST.get('name_of_the_student'),
                        department=request.POST.get('department'),
                        academic_year=request.POST.get('academic_year'),
                        roll_number=request.POST.get('roll_number'),
                        email_id=request.POST.get('email_id'),
                        mobile_number=request.POST.get('mobile_number'),
                        logger_id=id)
     
     messages.error(request,'successfully updated',extra_tags='success')
     return render(request,'InternationalRelations.html',{'view_data':view_data,'logger_data':logger_data,'internationalrelations_data':internationalrelations_data})

def delete_internationalrelations_data(request,id,row_id):
    logger_data=register_table.objects.get(id=id)
    view_data=internationalrelations_table.objects.filter(logger_id=id)
    internationalrelations_data=internationalrelations_table.objects.get(id=row_id)
    internationalrelations_data.delete()
    
    messages.error(request,'deleted successfully',extra_tags='success')
    return render(request,'InternationalRelations.html',{'view_data':view_data,'logger_data':logger_data,'internationalrelations_data':internationalrelations_data})



def ResearchDepartment(request,id):
    logger_data=register_table.objects.get(id=id)
    view_data=researchdepartment_table.objects.filter(logger_id=id)
    return render(request,'ResearchDepartment.html',{'logger_data':logger_data,'view_data':view_data})


def researchdepartmentadd(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'researchdepartmentadd.html',{'logger_data':logger_data})


def add_researchdepartment_form_submission(request,id):
     logger_data=register_table.objects.get(id=id)
     ex1=researchdepartment_table(name_of_the_principle_investigator=request.POST.get('name_of_the_principle_investigator'),
                        department=request.POST.get('department'),
                        sanctioned_letter_number_with_date=request.POST.get('sanctioned_letter_number_with_date'),
                        project_title=request.POST.get('project_title'),
                        duration_of_the_project=request.POST.get('duration_of_the_project'),
                        total_sanctioned_amount=request.POST.get('total_sanctioned_amount'),
                        logger_id=id)
     
     ex1.save()
     messages.error(request,'successfully added',extra_tags='success')
     view_data=researchdepartment_table.objects.filter(logger_id=id)
     return render(request,'ResearchDepartment.html',{'logger_data':logger_data,'view_data':view_data})


def ResearchDepartmentEdit(request,id,row_id):
    logger_data=register_table.objects.get(id=id)
    researchdepartment_data=researchdepartment_table.objects.get(id=row_id)
    return render(request,'ResearchDepartmentEdit.html',{'logger_data':logger_data,'researchdepartment_data':researchdepartment_data})
    
     
def edit_researchdepartment_data_form_submission(request,id,row_id):
     logger_data=register_table.objects.get(id=id)
     researchdepartment_data=researchdepartment_table.objects.get(id=row_id)
     view_data=researchdepartment_table.objects.filter(logger_id=id)
     
     ex1=researchdepartment_table.objects.filter(id=row_id).update(name_of_the_principle_investigator=request.POST.get('name_of_the_principle_investigator'),
                        department=request.POST.get('department'),
                        sanctioned_letter_number_with_date=request.POST.get('sanctioned_letter_number_with_date'),
                        project_title=request.POST.get('project_title'),
                        duration_of_the_project=request.POST.get('duration_of_the_project'),
                        total_sanctioned_amount=request.POST.get('total_sanctioned_amount'),
                        logger_id=id)
     
     messages.error(request,'successfully updated',extra_tags='success')
     return render(request,'ResearchDepartment.html',{'view_data':view_data,'logger_data':logger_data,'researchdepartment_data':researchdepartment_data})

def delete_researchdepartment_data(request,id,row_id):
    logger_data=register_table.objects.get(id=id)
    view_data=researchdepartment_table.objects.filter(logger_id=id)
    researchdepartment_data=researchdepartment_table.objects.get(id=row_id)
    researchdepartment_data.delete()
    
    messages.error(request,'deleted successfully',extra_tags='success')
    return render(request,'ResearchDepartment.html',{'view_data':view_data,'logger_data':logger_data,'researchdepartment_data':researchdepartment_data})

    

def aditamissionadd(request):
    return render(request,'aditamissionadd.html')



