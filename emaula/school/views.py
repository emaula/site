from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import ProfessorForm, ProfileForm
from .models import Classroom, Professor


def home_page(request):
    return render(request, 'school/index.html')


# class IndexView(generic.TemplateView):
#     template_name = 'school/index.html'


def team(request):
    return render(request, 'school/team.html')


def colaborate(request):
    return render(request, 'school/colaborate.html')


def about_project(request):
    return render(request, 'school/about.html')


def tos(request):
    return render(request, 'school/tos.html')


class ClassroomListView(generic.ListView):
    model = Classroom

    def get_queryset(self):
        return Classroom.objects.filter(
            published_date__lte=timezone.now()).order_by('title')


class ClassroomDetailView(generic.DetailView):
    model = Classroom

    def class_detail(request, pk):
        one_classroom = get_object_or_404(Classroom, pk=pk)
        return render(request,
                      'school/class_detail.html',
                      {'one_classroom': one_classroom})


class ProfessorListView(generic.ListView):
    model = Professor

    professor_list = Professor.objects.all().order_by('first_name')

    def get_queryset(self):
        return self.professor_list


class ProfessorDetailView(generic.DetailView):
    model = Professor

    def professor_detail(request, pk):
        one_professor = get_object_or_404(Professor, pk=pk)
        return render(request,
                      'school/professor_detail.html',
                      {'one_professor': one_professor})


@login_required
def professor_lessons_list(request, pk):
    # Pega o id do user:
    one_user = get_object_or_404(User, pk=pk)
    # Transforma o id do user em id do prof:
    one_professor = Professor.objects.get(user=one_user)
    # Retorna os objetos relacionados a aquele professor
    lessons_prof = Classroom.objects.all().filter(author=one_professor)

    return render(request,
                  'school/professor_lessons_list.html',
                  {'lessons_prof': lessons_prof})


@login_required
def sitestatus(request):
    # Status do sistema
    all_professors = Professor.objects.all().count()
    all_professors_all_classes = Classroom.objects.all().count()
    all_professors_all_published_classes = Classroom.objects.filter(
        published_date__lte=timezone.now()).count()
    return render(request,
                  'school/sitestatus.html',
                  context={
                      'all_professors': all_professors,
                      'all_professors_all_classes': all_professors_all_classes,
                      'all_professors_all_published_classes':
                      all_professors_all_published_classes})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = ProfessorForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_staff = True
            g, created = Group.objects.get_or_create(name='school_staff')
            g.user_set.add(user)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = ProfessorForm()
        profile_form = ProfileForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})
