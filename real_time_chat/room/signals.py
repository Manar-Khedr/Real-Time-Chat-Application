from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=User)
@receiver(post_delete, sender=User)
def update_user_list(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "user_list_group",
        {
            "type": "user_list_update",
            "users": [user.username for user in User.objects.all()],
        },
    )
