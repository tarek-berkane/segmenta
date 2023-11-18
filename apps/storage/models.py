from django.db import models
from django.contrib.auth import get_user_model

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# ==============
# IMAGES
# ==============
class ImageBase(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ImageTemporary(ImageBase):
    add_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="temporary_images"
    )
    image = models.ImageField(upload_to="temporary/")


class Image(ImageBase):
    add_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="images/")
    # product = models.ForeignKey(
    #     Product, on_delete=models.CASCADE, related_name="images"
    # )

    # main_image = models.BooleanField(default=False)

    # mini_book_cover = ImageSpecField(
    #     source="image",
    #     processors=[ResizeToFill(220, 300)],
    #     format="JPEG",
    #     options={"quality": 80},
    # )

    # big_book_cover = ImageSpecField(
    #     source="image",
    #     processors=[ResizeToFill(340, 510)],
    #     format="JPEG",
    #     options={"quality": 100},
    # )

    # def set_main_image(self):
    #     images = Image.objects.filter(product_id=self.product_id)
    #     for image in images:
    #         if image.pk == self.pk:
    #             image.main_image = True
    #         else:
    #             image.main_image = False

    #     Image.objects.bulk_update(images, ["main_image"])
