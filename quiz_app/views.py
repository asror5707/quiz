from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import QuizForm, SavolForm

from .models import *


class Index(View):
    def get(self, request):
        quiz = Quiz.objects.all()
        return render(request,'index.html', {"quiz" : quiz})

class QuizView(View):
    def get(self, request,pk):
        quiz = Quiz.objects.get(id=pk)
        return render(request, 'quiz.html',{"quiz":quiz})

class QuizDataView(View):
    def get(self,request, pk):
        quiz = Quiz.objects.get(id=pk)
        savollar = Savol.objects.filter(quiz=quiz)
        questions = []
        for s in savollar:
            answers = []
            jaboblar = Javob.objects.filter(savol=s)
            for j in jaboblar:
                answers.append(j.matn)
            questions.append({str(s):answers})
        return JsonResponse({
            'data':questions,
            'time':quiz.davomiyligi,
        })




class SignupView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'signup.html')

    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        if password != confirm_password:
            return redirect('/register')

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        login(request, user)
        return redirect('/login')

class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        l = request.POST['username']
        parol = request.POST['password']
        user = authenticate(request, username=l, password=parol)
        if user is None:
            return redirect('login')
        else:
            login(request, user)
            return redirect('/')


class Add_QuestionView(View):
    def get(self,request):
        if request.user.is_authenticated:
            s = Savol.objects.all()
            forma = SavolForm()
            return render(request, 'add_question.html', {'savol1': s, 'question_forms': forma})
        else:
            return redirect('/add_question')

    def post(self,request):
        if request.user.is_authenticated:
            forma = SavolForm(request.POST)
            if forma.is_valid():
                forma.save()
            return redirect('/add_question')
        else:
            return redirect('/add_question')



class Add_QuizView(View):
    def get(self, request):
        if request.user.is_authenticated:
            q = Quiz.objects.all()
            forma = QuizForm()
            return render(request, 'add_quiz.html', {'quiz1': q, 'forms': forma})
        else:
            return redirect('/add_quiz')

    def post(self, request):
        if request.user.is_authenticated:
            forma = QuizForm(request.POST)
            if forma.is_valid():
                forma.save()
            return redirect('/add_question')
        else:
            return redirect('/add_quiz')


class Add_OptionsView(View):
    def get(self,request,son):
        question = Savol.objects.get(id=son)
        QuestionFormSet = inlineformset_factory(Savol, Javob, fields=('matn', 'togri', 'savol'), extra=4)
        formset = QuestionFormSet(instance=question)
        return render(request, "add_options.html", {'formset': formset, 'question': question})
    def post(self,request,son):
        question = Savol.objects.get(id=son)
        QuestionFormSet = inlineformset_factory(Savol, Javob, fields=('matn', 'togri', 'savol'), extra=4)
        formset = QuestionFormSet(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
            alert = True
            return render(request, "add_options.html", {'alert': alert})



class Delete_QuestionView(View):
    def get(self,request,son):
        question = Savol.objects.get(id=son)
        return render(request, "delete_question.html", {'question': question})

    def post(self,request,son):
        if request.user.is_authenticated:
            question = Savol.objects.get(id=son)
            question.delete()
            return redirect('/add_question')
        else:
            return redirect('/add_question')



class Delete_QuizView(View):

    def get(self,request,son):
        if request.user.is_authenticated:
            q = Quiz.objects.get(id=son)
            q.delete()
            return redirect('/add_quiz')
        else:
            return redirect('/add_quiz')
def Logout(request):
    logout(request)
    return redirect('login')
