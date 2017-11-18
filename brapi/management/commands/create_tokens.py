from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Since version 3.6.4 it's possible to generate a user token using the following command:
#./manage.py drf_create_token <username>
class Command(BaseCommand):
    
    help = 'Create tokens for users'


    def handle(self, *args, **options):
       
        users = User.objects.all()
        for user in users:
            (token, created) = Token.objects.get_or_create(user=user)
            print(user.username, token.key)
        # end for

    # end def handle

# end class Command
