from django.core.management import call_command

def my_job():
  try:
  	call_command("dbbackup")
  except:
  	pass