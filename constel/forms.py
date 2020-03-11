from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Veiculo


class FormCadastraUsuario(UserCreationForm):
    """
    Formulário de cadastro de novo usuário ativo, exige senha.
    """

    username = forms.IntegerField(
        required=True,
        label='Matrícula',
        help_text='Insira o número da sua matrícula (crachá)'
    )
    first_name = forms.CharField(max_length=30, help_text='Obrigatório.', label='Nome')
    last_name = forms.CharField(max_length=100, help_text='Obrigatório.', label='Sobrenome')
    email = forms.EmailField(max_length=254, help_text='Obrigatório. Informe um endereço válido de email.')
    modelo = forms.CharField(max_length=30, label='Modelo do veículo', help_text='Obrigatório.')
    placa = forms.CharField(max_length=8, label='Placa do veículo', help_text='Obrigatório.')
    cor = forms.CharField(max_length=100, label='Cor do veículo', help_text='Obrigatório.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class FormCadastraUsuarioPassivo(forms.ModelForm):
    """
    Formulário de cadastro de novo usuário passivo. Não exige senha,
    serve para cadastrar usuários que não necesstam logar no sistema.
    """

    username = forms.IntegerField(
        required=True,
        label='Matrícula',
        help_text='Insira o número da sua matrícula (crachá)'
    )
    first_name = forms.CharField(max_length=30, help_text='Obrigatório.', label='Nome')
    last_name = forms.CharField(max_length=100, help_text='Obrigatório.', label='Sobrenome')
    email = forms.EmailField(max_length=254, help_text='Obrigatório. Informe um endereço válido de email.')
    modelo = forms.CharField(max_length=30, label='Modelo do veículo', help_text='Obrigatório.')
    placa = forms.CharField(max_length=8, label='Placa do veículo', help_text='Obrigatório.')
    cor = forms.CharField(max_length=100, label='Cor do veículo', help_text='Obrigatório.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class FormCadastrarVeiculo(forms.ModelForm):
    """
    Formulário de cadastro de veículos de funcionários existentes
    """

    class Meta:
        model = Veiculo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormCadastrarVeiculo, self).__init__(*args, **kwargs)

        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name')
        users_name = [(i.id, '%s - %s %s' % (i.username, i.first_name.title(), i.last_name.title())) for i in users]
        self.fields['user'] = forms.ChoiceField(choices=users_name, label='Funcionário')

    def clean(self):
        self.cleaned_data['user'] = User.objects.get(id=int(self.cleaned_data['user']))


class FormLogin(forms.Form):
    """
    Formulário de login de usuário
    """

    username = forms.CharField(max_length=150, label='Matrícula')
    password = forms.CharField(widget=forms.PasswordInput)

    widgets = {
        'password': forms.PasswordInput(),
    }


class DateInput(forms.DateInput):
    input_type = 'date'


class FormDataInicialFinalFuncionario(forms.Form):
    """
    Formulário que permite selecionar uma data inicial e uma final
    """

    data_inicial = forms.DateField(widget=DateInput(), required=False)
    data_final = forms.DateField(widget=DateInput(), required=False)
    funcionario = forms.CharField(
        label='Funcionário',
        help_text='Insira alguma informação do funcionário',
        required=False
    )

    def clean(self):
        form_data = self.cleaned_data

        if form_data['data_inicial'] >= form_data['data_final']:
            self.errors['data_inicial'] = ['A data inicial não pode ser mais recente que a data final']

        return form_data


class FormDataInicialFinal(forms.Form):
    """
    Formulário que permite selecionar uma data inicial e uma final
    """

    data_inicial = forms.DateField(widget=DateInput(), required=False)
    data_final = forms.DateField(widget=DateInput(), required=False)

    def clean(self):
        form_data = self.cleaned_data

        if form_data['data_inicial'] >= form_data['data_final']:
            self.errors['data_inicial'] = ['A data inicial não pode ser mais recente que a data final']

        return form_data
