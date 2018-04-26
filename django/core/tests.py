from django.contrib.auth.models import \
    User
from django.test import TestCase
from django.test.client import \
    RequestFactory
from django.urls.base import reverse

from core.forms import VoteForm
from core.models import Movie, Vote
from core.views import MovieList, \
    CreateVote


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


class VoteFormTestCase(TestCase):

    def setUp(self):
        self.correct_user = User.objects.create_user(
            username='correct',
            email='correct@example.org',
            password='unittest',
        )
        self.wrong_user = User.objects.create_user(
            username='wrong',
            email='wrong@example.org',
            password='unittest',
        )
        self.movie = Movie.objects.create(
            title='Title {}'.format(1),
            year=1990,
            runtime=100,
        )

    def testUserManipulationOnCreateFails(self):
        self.assertEqual(0, Vote.objects.filter(user=self.correct_user).count())
        self.assertEqual(0, Vote.objects.filter(user=self.wrong_user).count())
        form = VoteForm(
            initial={
                'user': self.correct_user
            },
            data={
                'user': self.wrong_user.id,
                'movie': self.movie.id,
                'value': Vote.UP
            })
        self.assertFalse(form.is_valid())

    def testVoteCreatedWithGoodData(self):
        self.assertEqual(0, Vote.objects.filter(user=self.correct_user).count())
        self.assertEqual(0, Vote.objects.filter(user=self.wrong_user).count())
        form = VoteForm(
            initial={
                'user': self.correct_user.id,
                'movie': self.movie.id,
            },
            data={
                'value': Vote.UP
            })
        self.assertTrue(form.is_valid(), form.errors)
        form.save()
        self.assertEqual(1, Vote.objects.filter(user=self.correct_user).count())
        self.assertEqual(0, Vote.objects.filter(user=self.wrong_user).count())


class CreateVoteViewTestCase(TestCase):

    def test_POST_request(self):
        initial_vote_count = Vote.objects.count()
        movie = Movie.objects.create(
            title='Title {}'.format(1),
            year=1990,
            runtime=100,
        )
        self.user = User.objects.create_user(
            username='correct',
            email='correct@example.org',
            password='unittest',
        )

        request = RequestFactory().post(
            reverse('core:CreateVote', kwargs={'movie_id': movie.id}),
            data={
                'movie': movie.id,
                'value': Vote.UP,
            },
        )
        request.user = self.user
        view = CreateVote.as_view()
        response = view(request, movie_id=movie.id)
        self.assertEqual(302, response.status_code)
        self.assertEqual(initial_vote_count + 1, Vote.objects.count())

