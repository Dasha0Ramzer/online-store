from django import forms

from catalog.models import Product


FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'picture', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем CSS-классы к полям формы
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['picture'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower() or word.lower() in description.lower():
                raise forms.ValidationError(f"Нельзя использовать слово: {word}")

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 1:
            raise forms.ValidationError("Цена не может быть отрицательной или равной 0.")
        return price

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if picture:
            if picture.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError("Размер файла не должен превышать 5MB.")
            if not picture.content_type in ['image/jpeg', 'image/png']:
                raise forms.ValidationError("Файл должен быть в формате JPEG или PNG.")
        return picture