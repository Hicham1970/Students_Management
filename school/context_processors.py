

def notifications(request):
    if request.user.is_authenticated:
        unread_notification = request.user.notification_set.filter(
            is_read=False)
        unread_notification_count = unread_notification.count()
        return {'unread_notification': unread_notification,
                'unread_notification_count': unread_notification_count}
    return {}
