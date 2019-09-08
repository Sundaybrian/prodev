from django.apps import AppConfig


class AwardsConfig(AppConfig):
    name = 'awards'

    def ready(self):

        print('rating signal is ready')
        # import awards.signals






