from django.apps import AppConfig


class cbitryConfig(AppConfig):
    name = 'cbitry'

    def ready(self):
    	import cbitry.signals
