from django.apps import AppConfig



class StudyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studyApp'

    def ready(self):
        import studyApp.signals
