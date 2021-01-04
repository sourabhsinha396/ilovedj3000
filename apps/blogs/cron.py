from django_cron import CronJobBase,Schedule
from django.core.management import call_command

class DbBackup(CronJobBase):
    RUN_EVERY_MINS = 60 * 24 * 2

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "blogs.db_backup"    # a unique code

    def do(self):
        call_command("dbbackup")