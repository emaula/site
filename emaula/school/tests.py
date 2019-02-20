from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from .views import home_page, colaborate, team, about_project, tos
from .models import Year, Subject
from .models import Classroom
from django.contrib.auth.models import User
from django.template.loader import render_to_string


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/school/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(
            b'<title>EmAula.xyz | Planeje e compartilhe suas aulas!</title>',
            response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))


class TeamPageTest(TestCase):
    def test_team_url_resolves_to_team_page_view(self):
        found = resolve('/school/team/')
        self.assertEqual(found.func, team)

    def test_team_page_returns_correct_html(self):
        request = HttpRequest()
        response = team(request)
        expected_html = render_to_string('school/team.html')
        self.assertEqual(response.content.decode(), expected_html)


class ColaboratePageTest(TestCase):
    def test_colaborate_url_resolves_to_colaborate_page_view(self):
        found = resolve('/school/colaborate/')
        self.assertEqual(found.func, colaborate)

    def test_colaborate_page_returns_correct_html(self):
        request = HttpRequest()
        response = colaborate(request)
        expected_html = render_to_string('school/colaborate.html')
        self.assertEqual(response.content.decode(), expected_html)


class AboutProjectPageTest(TestCase):
    def test_about_url_resolves_to_about_page_view(self):
        found = resolve('/school/about/')
        self.assertEqual(found.func, about_project)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = about_project(request)
        expected_html = render_to_string('school/about.html')
        self.assertEqual(response.content.decode(), expected_html)


class ToSPageTest(TestCase):
    def test_tos_url_resolves_to_tos_page_view(self):
        found = resolve('/school/tos/')
        self.assertEqual(found.func, tos)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = tos(request)
        expected_html = render_to_string('school/tos.html')
        self.assertEqual(response.content.decode(), expected_html)


class YearTest(TestCase):
    def test_year_with_string_input(self):
        year = Year(year="2º ano")
        self.assertEqual(
            str(year),
            "2º ano",
        )

    def test_year_with_numeric_input(self):
        year = Year(year="8")
        self.assertEqual(
            str(year),
            "8",
        )


class SubjectTest(TestCase):
    def test_subject_with_string_input(self):
        subject = Subject(subject="História")
        self.assertEqual(
            str(subject),
            "História",
        )


class ProfessorTest(TestCase):
    def test_professor_with_str(self):
        professor = User.objects.create_user(
            username='ana_maria',
            email='ana_maria@test.com',
            password='top_secret')

        self.assertEqual(
            str(professor),
            "ana_maria",
        )

    def test_professor_with_int(self):
        professor = User.objects.create_user(
            username='421_maria',
            email='ana_maria@test.com',
            password='top_secret')

        self.assertEqual(
            str(professor),
            "421_maria",
        )


class ClassroomTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.classroom = Classroom.objects.create(
            title="Revolução Francesa e suas consequências",
            summary="Antecedentes, desenrolar e reflexos na sociedade",
            created_date="2017-06-30",
            published_date="2017-06-30",
            views=0,
        )

    def test_classroom_title_with_string(self):
        self.assertEqual(
            str(self.classroom),
            "Revolução Francesa e suas consequências",
        )
