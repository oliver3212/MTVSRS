from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    movie_id = models.IntegerField(db_column='Movie_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300, blank=True,
                                   null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    release_date = models.DateField(db_column='Release_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Movie'


class Recommendation(models.Model):
    recommendation_id = models.IntegerField(db_column='Recommendation_ID',
                                            primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_ID')  # Field name made lowercase.
    recommendation_date = models.DateField(db_column='Recommendation_Date')  # Field name made lowercase.
    user_feedback = models.CharField(db_column='User_Feedback', max_length=20, blank=True,
                                     null=True)  # Field name made lowercase.
    show = models.ForeignKey('ShowTable', models.DO_NOTHING, db_column='Show_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recommendation'


class ShowTable(models.Model):
    show_id = models.IntegerField(db_column='Show_ID', primary_key=True)  # Field name made lowercase.
    tv_series = models.ForeignKey('TvSeries', models.DO_NOTHING, db_column='TV_Series_ID', blank=True,
                                  null=True)  # Field name made lowercase.
    movie = models.ForeignKey(Movie, models.DO_NOTHING, db_column='Movie_ID', blank=True,
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Show_Table'


class TvSeries(models.Model):
    tv_series_id = models.IntegerField(db_column='TV_Series_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300, blank=True,
                                   null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    release_date = models.DateField(db_column='Release_Date', blank=True, null=True)  # Field name made lowercase.
    number_of_episodes = models.IntegerField(db_column='Number_of_Episodes', blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TV_Series'


# TODO: We are already importing User from django.contrib.auth.models, need to merge and use one
class User(models.Model):
    user_id = models.IntegerField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=100)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    birthday = models.DateField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class Watchlist(models.Model):
    watchlist_id = models.IntegerField(db_column='Watchlist_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Watchlist'


class WatchlistShow(models.Model):
    watchlist_id = models.OneToOneField(Watchlist, models.DO_NOTHING, db_column='Watchlist_ID',
                                        primary_key=True)  # Field name made lowercase.
    show_id = models.ForeignKey(ShowTable, models.DO_NOTHING, db_column='Show_ID')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    added_date = models.DateField(db_column='Added_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WatchlistShow'
        unique_together = ('watchlist_id', 'show_id')
