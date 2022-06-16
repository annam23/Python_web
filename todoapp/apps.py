from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class TodoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todoapp'

    verbose_name = _("Треккер задач")
