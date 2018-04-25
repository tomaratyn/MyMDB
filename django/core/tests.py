from django.test import TestCase
from django.test.client import \
    RequestFactory
from django.urls.base import reverse

from core.models import Movie
from core.views import MovieList


class MovieListPaginationTestCase(
    TestCase):
    ACTIVE_PAGINATION_HTML = """
    <li class="page-item active">
      <a href="{}?page={}" class="page-link">{}</a>
    </li>
    """

    def setUp(self):
        for n in range(15):
            Movie.objects.create(
                title='Title {}'.format(
                    n),
                year=1990 + n,
                runtime=100,
            )

    def testFirstPage(self):
        movie_list_path = reverse(
            'core:MovieList')
        request = RequestFactory().get(
            path=movie_list_path)
        response = MovieList.as_view()(
            request)
        self.assertEqual(
            200,
            response.status_code)
        self.assertTrue(
            response.context_data[
                'is_paginated'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(
                movie_list_path, 1, 1),
            response.rendered_content)

# class PersonTests(TestCase):
#     def test_stuff(self):
#         movie = Movie.objects.create(
#             title='Title',
#             year=1990,
#             runtime=100,
#         )
#         john = Person.objects.create(
#             first_name='john doe',
#             last_name='john doe',
#             born=date(1980, 1, 1),
#         )
#         jane = Person.objects.create(
#             first_name='jane doe',
#             last_name='jane doe',
#             born=date(1980, 1, 1),
#         )
#         james = Person.objects.create(
#             lastname='james doe',
#             born=date(1980, 1, 1),
#         )
#         Actor.objects.create(movie=movie, person=john, billing='actor')
#         Actor.objects.create(movie=movie, person=jane, billing='actor')
#         Actor.objects.create(movie=movie, person=james, billing='actor')
#         movie.save()
#         pprint(Actor.objects.filter(movie=movie))
