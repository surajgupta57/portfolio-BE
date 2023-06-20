



def cv_upload_path(instance, filename):
    return f"cv/{filename}"

def skill_logo_upload_path(instance, filename):
    return f"skill/logo_{filename}"

def testimonial_upload_photo(instance, filename):
    return f"testimonial/{instance.name}/logo_{filename}"

def aboutme_upload_logo(instance, filename):
    return f"about_me_section/logo_{filename}"

def service_upload_icon(instance, filename):
    return f"service_section/icon_{filename}"

def project_upload_logo(instance, filename):
    return f"project_section/logo_{filename}"

def jumbo_upload_image(instance, filename):
    return f"jumbo_section/logo_{filename}"
