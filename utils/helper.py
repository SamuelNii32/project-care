import datetime


def unsplash_image(image_id: str, image_size: str):
    return f'https://source.unsplash.com/{image_id}/{image_size}'


def refresh_data():
    sd = datetime.datetime(2022, 12, 8)
    ed = sd + datetime.timedelta(days=30)
    n = datetime.datetime.now()
    if n >= ed:
        return True
    else:
        return False
