# online_market

<p>Этот проект я разрабатывал исключительно для повышения своих навыков в области  Django</p>

<p>В проекте имеется 6 приложений(кроме той что с коробки - market): market, product, users, basket, orders, reviews, apiload.
</p>

<h4>Product</h4>
<p>Это приложение необходимо для отоброжения и хранения всех товаров имеющихся в магазине. Доступен по url /', то что видят пользователт при переходе на странцу. 
    Здесь имеются 3 модели: Product для хранения товаров, Product_type для хранения списка типов продуктов, ProductPhoto для хранения фотографий товаров,
    Product_rating для храния средней оценки товаров от всех рпользователей.
    <img src="">    
</p>

<p>В таблице "Product" 11 полей:<br>
id - уникальный индентификатор,<br>
name - наименование товара типа CharField, с максимальной длиной 255 символа,<br>
slug - уникальный слаг для создания индивидуального url для каждого товара,<br>
product_type - тип товара с внешним ключем ForeignKeyс таблицей "Product_type,<br>
old_price - обычная цена товара типа IntegerField,<br>
new_price - скидочная цена IntegerField, если таковая имеетя
count - количество товаров на складеIntegerField,<br>
description - описание товара TextField,<br>
date_create - дата создания записи,<br>
date_update - дата обновления записи,<br>
available = BooleanField, True, если товар доступен для продажи,<br>
</p>
<p>ProductType имеет 3 поля:<br>
id - уникальный индентификатор,<br>
name - имя типа товара CherField,<br>
slug - уникальный слаг типа товара,<br>
</p>
<p>В ProductPhoto 5 полей:<br>
id - уникальный индентификатор,<br>
id_product - внешний ключ к таблице "Product",<br>
photo - путь к фотографии продукта типа ImageField,<br>
date_add - дата добавления,<br>
date_update - дата последнего изменения,<br> 
</p>
<p>"Product rating" имеет 3 поля:<br>
id - уникальный индентификатор,<br>
product - внешний ключ OneToOneField с таблицей "Product",<br>
rating - рейтинг продукта DecimalField,<br>
</p>

<p>В product имеется 2 view: ProductList для отображения списка всех товаров, show_product для отображения странцы конкретного товара, доступный через '<slug:product_slug>/ </p>


<h4>Users</h4>

<p>Тут всего одна модель: CustomUser. В нем есть переопределеный метод "save" для сжатия фото пользователя преред сохранием на сервере </p>

<p> CustomUser переопределенная модель от "AbstrctUser", помимо имеющихся моделй добавлены 3 поля:<br>
    photo - хранит путь к фотографии пользователя,<br>
    phone_number - поле для номера телефона,<br>
    phoneNumberRegex - валидатор для поля "phone_number",<br>
</p>
<p>Список доступных url: /users/ + :<br>
    <img src="">
</p>

<p>Есть 5 view:<br>
    класс RegisterUser - для регистрации новых пользователей,<br>
    класс LoginUser - для авторизации пользователей,<br>
    logout_user - для выхода из системы,<br>
    profile_updfdate - для редактирования профиля,<br> 
    класс ResetPasswordView - для сброса пароля<br>
</p>

<h4>basket</h4>

<p>Тут одна модель Shoping_cart c 7-ю полями:<br>
id - уникальный индентификатор,<br>
id_user - внешний ключ ForeignKey к таблице "CustomUser",<br>
id_product - внешний ключ ForeignKey к таблице "Product",<br>
quantity - количестов данных товаров в корзине с ограничением > 0<br>
dete_crete - дата добавления записи,<br>
date_update -  дата обновления записи,<br>
</p>

<p>В приложении 5 url: /cart/ + :<br>
    <img src="">
</p>
<p>
basket_view - для отбражения корзины,<br>
basket_add - для добавления нового товара в корзину,<br>
basket_delete - для удаления товара из корзины,<br>
basket_increment_count - для увеличения количества определенного товара в корзине,<br>
basket_decrement_count - для уменьшения количества определенного товара в корзине,<br>
</p>

<h4>Orders</h4>

<p>
В этом приложении есть 3 модели: Order_data, Orders_inform, Orders_status_types<br>
Order_data содержит 8 полей:<br>
id - уникальный индентификатор,<br>
user - ForeignKey к таблице "CustomUser",<br>
personal_order_id - номер по счету заказ для данного пользователя,<br>
full_order_id - полный уникальный индентификатор заказа,<br>
status - внешний ключ статуса заказа к таблице "Orders_status_types",<br>
date_create - дата создания записи,<br>
date_update - дата обновления записи,<br>
total_price - полная стоимость заказа,<br>

</p>









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



