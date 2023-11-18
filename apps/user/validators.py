from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

from apps.user.models import User


def validate_is_supervisor_id(user_id: int):
    try:
        user = User.objects.get(id=user_id)
        validate_is_supervisor(user)
    except ObjectDoesNotExist as e:
        raise ValidationError(
            _("No User exist with id = %(id)"),
            params={"id": user_id},
        )


def validate_is_supervisor(user: User):
    if user.role != User.Role.SUPERVISOR:
        raise ValidationError(
            _(f"User %(value)s is not {User.Role.SUPERVISOR}"),
            params={"value": user.username},
        )
