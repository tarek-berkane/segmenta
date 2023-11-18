from django.views import generic
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages


from apps.storage.models import ImageTemporary, Image
from apps.storage.services import move_temporary_image


@require_http_methods(["POST"])
@login_required
@user_passes_test(lambda user: user.role == user.Role.SUPERVISOR)
def upload_image(request):
    files = request.FILES
    temp_image = ImageTemporary.objects.create(
        image=files["images"], add_by=request.user
    )
    return HttpResponse(temp_image.pk)


# @require_http_methods(["POST"])
# @login_required
# @user_passes_test(lambda user: user.role == user.Role.SUPERVISOR)
# def add_product_image(request, pk, next_page=None, set_cover=False):
#     image_id = request.POST.get("images")
#     image_temp = ImageTemporary.objects.get(pk=image_id)

#     product_image = move_temporary_image(image_temp)
#     if set_cover:
#         product_image.set_main_image()

#     if next_page == "product_photo":
#         messages.add_message(request, messages.SUCCESS, "Image added")
#         return HttpResponseRedirect(
#             reverse_lazy("dashboard:products-images", kwargs={"pk": product.pk})
#         )

#     messages.add_message(request, messages.SUCCESS, "Book cover update")
#     return HttpResponseRedirect(
#         reverse_lazy("dashboard:products-detail", kwargs={"pk": product.pk})
#     )


class DashboardImageDeleteView(generic.DeleteView):
    model = Image
    template_name = "dashboard/storage/image_delete.html"

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Image delete")

        print(self.object.product_id)
        return reverse_lazy(
            "dashboard:products-images", kwargs={"pk": self.object.product_id}
        )
