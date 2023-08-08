# online_market






<h2> Отправка пиьсма на почту для сброса пароля</h2>

<p>В данном проекте для рассылки я использовал почту @yandex.ru далее пропишу все необходимые шаги для этого</p>

<p>Для начала вам необходимо прописать следующие строчки в settings.py
        <ul>
            <li>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</li>
            <li>EMAIL_HOST = 'smtp.yandex.ru'</li>
            <li>EMAIL_PORT = 465</li>
            <li>EMAIL_USE_TLS = False</li>
            <li>EMAIL_USE_SSL = True</li>
            <li>EMAIL_HOST_USER = EMAIL_USER</li>
            <li>EMAIL_HOST_PASSWORD = EMAIL_PASSWORD</li>
            <li>DEFAULT_FROM_EMAIL = EMAIL_HOST_USER</li>
            <li>SERVER_EMAIL = EMAIL_HOST_USER</li>
            <li>EMAIL_ADMIN = EMAIL_HOST_USER</li>
        </ul>
    Где EMAIL_USER ваша переменная из .env с логином почты, с которой будет совершаться рассылка,
    а EMAIL_PASSWORD пароль почты приложений, далее покажу как его сгененрировать.
</p>

<p>     Для получения пароля нужно войти на почту yandex, в разделе "Управление аккаунтом"->Безопасность" 
    найти поле "Пароли приложений", далее "Почта", ввести имя пароля, а затем скопировать сгенерированный пароль. 
    <br>
    Также нужно перейти по пути "Настройки->Все настройки->Почтовые программы" и проставить все галки<div class=""></div>
</p>


<p>
    В файле users/urls.py добавить следующие адреса:<br>
    <code>
        path('password-reset-confirm/&ltuidb64&gt/&lttoken&gt/',
            auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),<br>
            name='password_reset_confirm'),<br>
       
        path('password-reset-complete/',<br>
            auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),<br>
            name='password_reset_complete'),<br>
    </code>
</p> 

<p> 
    
<code>
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password-reset.html'
    email_template_name = 'users/password-reset-email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')    
</code>
</p>





---------------------------------------
sql query for card-photo element:
"""
    select name, old_price, count, ph.photo  from product_product pr
    inner join ( 
        select distinct on (id_product_id) * from product_productphoto) as ph on pr.id = ph.id_product_id  
"""

with django orm:
"""
    ProductPhoto.objects.select_related('id_product').distinct('id_product')
"""
-----------------------------------------



