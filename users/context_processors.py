from applications.models import Notification


def notifications(request):
    if request.user.is_authenticated:
        unread_list = list(
            Notification.objects.filter(user=request.user, is_read=False)
            .order_by("-created_at")
            [:50]
        )

        return {
            "notifications": unread_list,
            "notifications_count": len(unread_list),
        }

    return {"notifications": [], "notifications_count": 0}