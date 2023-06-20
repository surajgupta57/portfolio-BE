def user_country_photo_upload_path(instance, filename):
    return f"user/country/{instance.slug}/{filename}"

def user_states_photo_upload_path(instance, filename):
    return f"user/states/{instance.slug}/{filename}"

def user_city_photo_upload_path(instance, filename):
    return f"user/city/{instance.slug}/{filename}"

def user_district_photo_upload_path(instance, filename):
    return f"user/district/{instance.slug}/{filename}"

def user_district_region_photo_upload_path(instance, filename):
    return f"user/districtregion/{instance.slug}/{filename}"