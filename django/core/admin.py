from django.contrib import admin

from core.models import (
    Movie, Person, Role, MovieImage)


class DirectorInline(admin.StackedInline):
    model = Movie
    fk_name = 'director'
    verbose_name = 'director'
    verbose_name_plural = 'directors'
    extra = 1


class RoleInline(admin.StackedInline):
    model = Role
    extra = 1
    autocomplete_fields = (
        'person', 'movie')


class MovieAdmin(admin.ModelAdmin):
    inlines = [
        RoleInline,
    ]
    list_display = (
        'title', 'year', 'rating')
    list_filter = (
        'rating',
    )
    fields = (
        ('title', 'year', ),
        ('runtime', 'rating'),
        'plot',
        'director',
        'writers',
        'website',
    )
    autocomplete_fields = (
        'writers', 'director')
    search_fields = ('title', )


class WriterInline(admin.StackedInline):
    model = Movie.writers.through
    verbose_name = 'writer'
    verbose_name_plural = 'wrote'
    extra = 1
    autocomplete_fields = ('movie', )


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'born', 'died',)
    inlines = [
        RoleInline,
        WriterInline,
    ]
    search_fields = (
        'last_name', 'first_name',)

    def name(self, obj):
        return "{} {}".format(
            obj.first_name,
            obj.last_name)


admin.site.register(Movie, MovieAdmin)


admin.site.register(Person, PersonAdmin)

admin.site.register(MovieImage)