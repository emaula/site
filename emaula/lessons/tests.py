from django.test import TestCase
from .models import Link, Image, Text, Video, Audio


# LINK TESTS
class LinkTest(TestCase):
    def test_str(self):
        link = Link(url='https://www.google.com',
                    name='Google',
                    access_date='30/06/2017')

        self.assertEqual(
            str(link),
            'Google - https://www.google.com',
        )


# IMAGE TESTS
class ImageTest(TestCase):
    def test_str(self):
        image = Image(image_path='media/foo.jpg')

        self.assertEqual(
            str(image),
            'media/foo.jpg',
        )


# TEXT TESTS
class TextTest(TestCase):
    def test_str(self):
        text = Text(title='This is a test', text='Testing the text')

        self.assertEqual(
            str(text),
            'This is a test',
        )


# VIDEO TESTS
class VideoTest(TestCase):
    def test_str(self):
        video = Video(video='https://www.youtube.com/watch?v=CAUom6E7Wp8',
                      title='História da África')

        self.assertEqual(
            str(video),
            'História da África - https://www.youtube.com/watch?v=CAUom6E7Wp8',
        )


# AUDIO TESTS
class AudioTest(TestCase):
    def test_str(self):
        audio = Audio(
            audio='https://soundcloud.com/salto\
            sounds/rap-das-armas-gregor-salto-2017-remix',
            title='Rap das Armas')

        self.assertEqual(
            str(audio),
            'Rap das Armas - https://soundcloud.com/salto\
            sounds/rap-das-armas-gregor-salto-2017-remix',
        )
