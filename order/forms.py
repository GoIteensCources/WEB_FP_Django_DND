from django import forms


class CheckoutForm(forms.Form):
    shipping_name = forms.CharField(max_length=100, label='Ім\'я отримувача',
                                    widget=forms.TextInput(attrs={'placeholder': 'Іван Шевченко'}))
    shipping_city = forms.CharField(max_length=100, label='Місто доставки',
                                    widget=forms.TextInput(attrs={'placeholder': 'Харків'}))
    shipping_street = forms.CharField(max_length=255, label='Вулиця доставки',
                                      widget=forms.TextInput(attrs={'placeholder': 'вул. Хрещатик, 1'}))
    shipping_zip_code = forms.CharField(max_length=20, label='Поштовий індекс',
                                        widget=forms.TextInput(attrs={'placeholder': '61000'}))
    shipping_country = forms.CharField(max_length=100, label='Країна', initial='Україна',
                                       widget=forms.TextInput(attrs={'placeholder': 'Україна'}))
    coment = forms.CharField(label='Коментар до замовлення', required=False,
                             widget=forms.Textarea(attrs={'placeholder': 'Додайте коментар до замовлення...',
                                                          'rows': 3}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})