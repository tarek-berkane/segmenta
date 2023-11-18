from typing import List

from django.core.files.base import ContentFile

from apps.storage.models import ImageTemporary, Image, ImageBase
from apps.user.models import Supervisor


def move_temporary_image(
    image_temporary: ImageTemporary,
    commit=True,
    delete_temporary=True,
):
    image = Image(add_by=image_temporary.add_by)

    with image_temporary.image.open() as f:
        image_name = f.name.split("/")[-1]
        image.image.save(image_name, content=ContentFile(f.read()), save=commit)

    if delete_temporary:
        image_temporary.delete()

    return image


def move_temp_images(temp_images: List[ImageTemporary]):
    images = []
    for temp_image in temp_images:
        images.append(
            move_temporary_image(temp_image, commit=False, delete_temporary=True)
        )
    if images:
        images[0].main_image = True
    Image.objects.bulk_create(images)


def move_temp_images_by_id(temp_images_id: List[int]):
    temp_images = ImageTemporary.objects.filter(id__in=temp_images_id)
    move_temp_images(temp_images)
