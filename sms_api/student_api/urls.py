from django.urls import path, include
from . import views 
# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('course/', views.CourseListView.as_view(), name="course"),
    path('student/', views.StudentApiView.as_view(), name="student"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('tutor/', views.TutorListView.as_view(), name="tutor"),
    # path('user/', views.CreateNewUser.as_view(), name="new_user"),
    # path('token_login/', obtain_auth_token, name="token_logn")
    path('course/<int:pk>/', views.CourseDetail.as_view(), name="course"),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name="student")
    
]