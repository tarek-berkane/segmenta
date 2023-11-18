from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

from apps.user.models import User, Supervisor, Client


class SupervisorAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user: User):
        print(user.role)
        if not user.role == User.Role.SUPERVISOR:
            raise ValidationError(
                self.error_messages["invalid_login"],
                code="invalid_login",
                params={"username": self.username_field.verbose_name},
            )


class SupervisorCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        # Check if the form is being used for an update view
        if kwargs.get("instance"):
            # If it is, remove the "password" field
            self.fields.pop("password")

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def save(self, commit=True):
        data = self.cleaned_data
        if user := self.instance:
            user.username = data["username"]
            user.email = data["email"]
            user.save()
            return user
        else:
            user = Supervisor.objects.create_user(
                data["username"], data["email"], data["password"]
            )
            return user


class ClientAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if name == "password":
                field.widget.attrs["placeholder"] = "************"
            else:
                field.widget.attrs["placeholder"] = "Username"

    def confirm_login_allowed(self, user: User):
        print(user.role)
        if not user.role == User.Role.CLIENT:
            raise ValidationError(
                self.error_messages["invalid_login"],
                code="invalid_login",
                params={"username": self.username_field.verbose_name},
            )


class ClientCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def save(self, commit=...):
        data = self.cleaned_data
        user = Client.objects.create_user(
            data["username"], data["email"], data["password"]
        )
        return user
