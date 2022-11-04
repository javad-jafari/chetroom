from importlib import import_module
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from django.core.management.color import no_style
from django.core.management.sql import emit_post_migrate_signal, sql_flush
from django.db import DEFAULT_DB_ALIAS, connections
from user.models import CustomUser, Saller

class Command(BaseCommand):


    def add_arguments(self, parser):
        pass

    def handle(self, **options):
        
        try :
            for i in range(1,11):
                user=CustomUser(username=f'user{i}')
                user.set_password("1234")
                user.save()
            print("******* users added succesfully ***************")
        except:
            raise 'something get wrong in adding users'
        
        try:
            user = CustomUser.objects.all()[1:7]
            for j in range(1,6):
                s = Saller(name=f"saller {j}", user=user[j])
                s.save()
            print("******* sallers added succesfully ***************")
        except:
            raise 'something get wrong in adding sallers'
            