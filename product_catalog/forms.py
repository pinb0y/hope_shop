from django import forms

from product_catalog.models import Product

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs )
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "forms-control"


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ("product_name", "description", "price", "image", "standard")

    def clean_standard(self):
        cleaned_data = self.cleaned_data["standard"]

        if "ru-2024" not in cleaned_data:
            raise forms.ValidationError("Невалидный стандарт")

        return cleaned_data

