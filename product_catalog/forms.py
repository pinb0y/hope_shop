from django import forms

from product_catalog.models import Product

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs )
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "forms-control"



class ProductForm(StyleFormMixin, forms.ModelForm):
    taboo_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                   "радар"]

    class Meta:
        model = Product
        fields = "__all__"

    def clean_product_name(self):
        cleaned_data = self.cleaned_data["product_name"]
        for word in self.taboo_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f"слово <{word}> нельзя использовать в имени")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]
        for word in self.taboo_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f"слово <{word}> нельзя использовать в описании")
        return cleaned_data

