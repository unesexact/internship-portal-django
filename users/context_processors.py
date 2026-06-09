from applications.models import Notification


def notifications(request):
    if request.user.is_authenticated:
        unread = Notification.objects.filter(user=request.user, is_read=False).order_by(
            "-created_at"
        )

        return {"notifications": unread, "notifications_count": unread.count()}
    return {"notifications": [], "notifications_count": 0}
