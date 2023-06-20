



def user_profile_picture_upload_path(instance, filename):
    return f"user/profile_picture/user_{instance.user.username}/{filename}"
