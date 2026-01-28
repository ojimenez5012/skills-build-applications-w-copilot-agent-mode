from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=date(2024, 1, 1))
        Activity.objects.create(user=users[1], type='cycle', duration=45, date=date(2024, 1, 2))
        Activity.objects.create(user=users[2], type='swim', duration=25, date=date(2024, 1, 3))
        Activity.objects.create(user=users[3], type='yoga', duration=60, date=date(2024, 1, 4))

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Sprints', description='Sprint 100m x 5', difficulty='hard')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
