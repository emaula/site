from django.test import TestCase
from .models import Year, Subject
from .models import Classroom
from django.contrib.auth.models import User


class YearTest(TestCase):
    def test_year_with_string_input(self):
        year = Year(year="2º ano")
        self.assertEquals(
            str(year),
            "2º ano",
        )

    def test_year_with_numeric_input(self):
        year = Year(year="8")
        self.assertEquals(
            str(year),
            "8",
        )


class SubjectTest(TestCase):
    def test_subject_with_string_input(self):
        subject = Subject(subject="História")
        self.assertEquals(
            str(subject),
            "História",
        )


class ProfessorTest(TestCase):
    def test_professor_with_str(self):
        professor = User.objects.create_user(
            username='ana_maria',
            email='ana_maria@test.com',
            password='top_secret')

        self.assertEquals(
            str(professor),
            "ana_maria",
        )

    def test_professor_with_int(self):
        professor = User.objects.create_user(
            username='421_maria',
            email='ana_maria@test.com',
            password='top_secret')

        self.assertEquals(
            str(professor),
            "421_maria",
        )


class ClassroomTest(TestCase):
    def test_classroom_title_with_string(self):
        classroom = Classroom.objects.create(
            title="Revolução Francesa e suas consequências",
            summary="Antecedentes, desenrolar e reflexos na sociedade",
            created_date="2017-06-30",
            published_date="2017-06-30",
            views=0,
        )

        self.assertEquals(
            str(classroom),
            "Revolução Francesa e suas consequências",
        )
