from django import forms

from .models import *


class FormCadastraFerramenta(forms.ModelForm):

    class Meta:
        model = Ferramenta
        fields = ['nome', 'descricao', ]

    def __init__(self, *args, **kwargs):
        super(FormCadastraFerramenta, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs.update({'class': 'form-control'})


class FormEntradaFerramenta(forms.ModelForm):

    class Meta:
        model = FerramentaEntrada
        fields = ['ferramenta', 'quantidade', 'valor', 'observacao', ]

    def __init__(self, *args, **kwargs):
        super(FormEntradaFerramenta, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs.update({'class': 'form-control'})


class FormSaidaFerramenta(forms.ModelForm):

    class Meta:
        model = FerramentaSaida
        fields = ['user_to', 'ferramenta', 'quantidade', 'observacao', ]

    def __init__(self, *args, **kwargs):
        super(FormSaidaFerramenta, self).__init__(*args, **kwargs)

        self.fields['ferramenta'].queryset = Ferramenta.objects.filter(
            quantidade__quantidade__gt=0
        ).order_by('nome')

        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name')
        users_name = [(i.id, '%s - %s %s' % (i.username, i.first_name.title(), i.last_name.title())) for i in users]
        self.fields['user_to'] = forms.ChoiceField(
            choices=users_name,
            label='Funcionário',
        )

        for key in self.fields.keys():
            self.fields[key].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        form_data = self.cleaned_data
        form_data['user_to'] = User.objects.get(id=int(form_data['user_to']))

        estoque = FerramentaQuantidade.objects.get(ferramenta=form_data['ferramenta']).quantidade
        retirada = form_data['quantidade']

        if (estoque - retirada) < 0:
            self._errors['quantidade'] = ['Não há esta quantidade de ferramentas disponível em estoque!']

        return form_data
