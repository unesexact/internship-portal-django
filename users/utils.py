def is_company(user):
    return hasattr(user, 'profile') and user.profile.user_type == 'company'


def is_student(user):
    return hasattr(user, 'profile') and user.profile.user_type == 'student'