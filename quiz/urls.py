from django.contrib import admin
from django.urls import path
from quiz_app.views import *
from natijaapp.views import QuizSaveView,Delete_ResultView,ResultView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(),name='index'),
    path('result/', ResultView.as_view(),name='result'),
    path('signup/', SignupView.as_view(),name='signup'),
    path('login/', LoginView.as_view(),name='login'),
    path('add_question/', Add_QuestionView.as_view(),name='add_question'),
    path('add_quiz/', Add_QuizView.as_view(),name='add_quiz'),
    path('add_options/<int:son>/', Add_OptionsView.as_view(),name='add_options'),
    path('delete_question/<int:son>/', Delete_QuestionView.as_view(),name='delete_question'),
    path('delete_quiz/<int:son>/', Delete_QuizView.as_view(),name='delete_quiz'),
    path('delete_result/<int:son>/', Delete_ResultView.as_view(),name='delete_result'),
    path('logout/', Logout, name='logout'),
    path('<int:pk>/', QuizView.as_view(), name='quiz'),
    path('<int:pk>/data/', QuizDataView.as_view(), name='quiz-data'),
    path('<int:pk>/save/', QuizSaveView.as_view(), name='quiz-save'),
]
