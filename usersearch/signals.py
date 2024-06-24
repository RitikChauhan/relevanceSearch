from django.core.management import call_command
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from usersearch.models import Candidate


@receiver(post_save, sender=Candidate)
@receiver(post_delete, sender=Candidate)
def rebuild_search_index(sender, instance, **kwargs):
    print("signal triggered----------------------")
    call_command("rebuild_search_index", "--rebuild")