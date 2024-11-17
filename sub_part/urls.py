from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('index2/<int:id>',views.index2,name='index2'),

    path('student/<int:id>',views.student,name='student'),
    path('studentaddlist/<int:id>',views.studentaddlist,name='studentaddlist'),
    path('StudentEdit/<int:id>/<int:row_id>',views.StudentEdit,name='StudentEdit'),
    
    path('Teachingstaff/<int:id>',views.Teachingstaff,name='Teachingstaff'),
    path('teachingstaffadd/<int:id>',views.teachingstaffadd,name='teachingstaffadd'),
    path('TeachingStaffEdit/<int:id>/<int:row_id>',views.TeachingStaffEdit,name='TeachingStaffEdit'),
    
    path('nonteachingstaff/<int:id>',views.nonteachingstaff,name='nonteachingstaff'),
    path('nonteachingstaffadd/<int:id>',views.nonteachingstaffadd,name='nonteachingstaffadd'),
    path('nonteachingstaffedit/<int:id>/<int:row_id>',views.nonteachingstaffedit,name='nonteachingstaffedit'),

    #path('AdmissionDepartment',views.AdmissionDepartment,name='AdmissionDepartment'),
    #path('AdmissionEdit',views.AdmissionEdit,name='AdmissionEdit'),
    #path('PlacementAndTrainingCell',views.PlacementAndTrainingCell,name='PlacementAndTrainingCell'),
    #path('PlacementandTrainingEdit',views.PlacementandTrainingEdit,name='PlacementandTrainingEdit'),
    #path('Departments',views.Departments,name='Departments'),
    #path('DepartmentEdit',views.DepartmentEdit,name='DepartmentEdit'),
    #path('Laboratory',views.Laboratory,name='Laboratory'),
    #path('LaboratoryEdit',views.LaboratoryEdit,name='LaboratoryEdit'),
    #path('swo',views.swo,name='swo'),
    #path('swoEdit',views.swoEdit,name='swoEdit'),
    #path('exam',views.exam,name='exam'),
    #path('examEdit',views.examEdit,name='examEdit'),
    #path('paymentdepartment',views.paymentdepartment,name='paymentdepartment'),
    #path('PaymentDepartmentEdit',views.PaymentDepartmentEdit,name='PaymentDepartmentEdit'),
    #path('GamesandNGO',views.GamesandNGO,name='GamesandNGO'),
    #path('GamesandNGOedit',views.GamesandNGOedit,name='GamesandNGOedit'),
    #path('Nationalcadetcorps',views.Nationalcadetcorps,name='Nationalcadetcorps'),
    #path('NationalcadetcorpsEdit',views.NationalcadetcorpsEdit,name='NationalcadetcorpsEdit'),
    #path('DispensaryRoom',views.DispensaryRoom,name='DispensaryRoom'),
    #path('DispensaryEdit',views.DispensaryEdit,name='DispensaryEdit'),

    #path('NewsandArticle',views.NewsandArticle,name='NewsandArticle'),
    #path('NewsandArticleEdit',views.NewsandArticleEdit,name='NewsandArticleEdit'),

    path('InternationalRelations/<int:id>',views.InternationalRelations,name='InternationalRelations'), 
    path('internationalrelationsadd/<int:id>',views.internationalrelationsadd,name='internationalrelationsadd'), 
    path('InternationalRelationsEdit/<int:id>/<int:row_id>',views.InternationalRelationsEdit,name='InternationalRelationsEdit'),  

    path('ResearchDepartment/<int:id>',views.ResearchDepartment,name='ResearchDepartment'),  
    path('researchdepartmentadd/<int:id>',views.researchdepartmentadd,name='researchdepartmentadd'),
    path('ResearchDepartmentEdit/<int:id>/<int:row_id>',views.ResearchDepartmentEdit,name='ResearchDepartmentEdit'),  

    path('aditamissionadd',views.aditamissionadd,name='aditamissionadd'),
    path('register_form_submission',views.register_form_submission,name='register_form_submission'),
    path('login_form_submission',views.login_form_submission,name='login_form_submission'),
    path('logout',views.logout,name='logout'),

    path('add_student_form_submission/<int:id>',views.add_student_form_submission,name='add_student_form_submission'),
    path('edit_student_data_form_submission/<int:id>/<int:row_id>',views.edit_student_data_form_submission,name='edit_student_data_form_submission'),
    path('delete_student_data/<int:id>/<int:row_id>',views.delete_student_data,name='delete_student_data'),

    path('add_teachingstaff_form_submission/<int:id>',views.add_teachingstaff_form_submission,name='add_teachingstaff_form_submission'),
    path('edit_teachingstaff_data_form_submission/<int:id>/<int:row_id>',views.edit_teachingstaff_data_form_submission,name='edit_teachingstaff_data_form_submission'),
    path('delete_teachingstaff_data/<int:id>/<int:row_id>',views.delete_teachingstaff_data,name='delete_teachingstaff_data'),

     path('add_nonteachingstaff_form_submission/<int:id>',views.add_nonteachingstaff_form_submission,name='add_nonteachingstaff_form_submission'),
    path('edit_nonteachingstaff_data_form_submission/<int:id>/<int:row_id>',views.edit_nonteachingstaff_data_form_submission,name='edit_nonteachingstaff_data_form_submission'),
    path('delete_nonteachingstaff_data/<int:id>/<int:row_id>',views.delete_nonteachingstaff_data,name='delete_nonteachingstaff_data'),

    path('add_researchdepartment_form_submission/<int:id>',views.add_researchdepartment_form_submission,name='add_researchdepartment_form_submission'),
    path('edit_researchdepartment_data_form_submission/<int:id>/<int:row_id>',views.edit_researchdepartment_data_form_submission,name='edit_researchdepartment_data_form_submission'),
    path('delete_researchdepartment_data/<int:id>/<int:row_id>',views.delete_researchdepartment_data,name='delete_researchdepartment_data'),

    path('add_internationalrelations_form_submission/<int:id>',views.add_internationalrelations_form_submission,name='add_internationalrelations_form_submission'),
    path('edit_internationalrelations_data_form_submission/<int:id>/<int:row_id>',views.edit_internationalrelations_data_form_submission,name='edit_internationalrelations_data_form_submission'),
    path('delete_internationalrelations_data/<int:id>/<int:row_id>',views.delete_internationalrelations_data,name='delete_internationalrelations_data'),
]

