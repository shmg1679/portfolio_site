from django.apps import AppConfig

#each app.py are simular, just change the _name_Config(AppConfig)
class ExchangeRateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #and change name to match folder name
    name = 'exchange_rate'
