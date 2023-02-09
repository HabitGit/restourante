<h3>Readme написан чисто для себя</h3>

<ul><h3>Инструкции:</h3>
<li>Первый запуск приложения должен начинаться прямо со страницы регистрации;                                                   +</li>
<li>первый зарегистрировавшийся пользователь автоматически получает admin permission;                                           +</li>
<li>после чего попадает на страницу настройки ресторана. Условно /settings.                                                     +</li>

<li>СТРАНИЦА SETTINGS:                                                                                                          
Страница должна делиться на вкладки, условно это будет: settings/profile; settings/admin; settings/settings;                
settings/restaurant.                                                                                                            +</li>                                                                                                       

<li>SETTINGS/PROFILE:
Где должны находиться все пользовательские настройки, условно настройки модели User.</li>

<li>SETTINGS/ADMIN:
Где должно находиться управление всеми пользователями : регистрация нового пользователя;
                                                        полный список всех пользователей;
                                                        настройка каждого пользователя;
                                                        *вкладка с оповещениями об изменениях пользователей;
* - когда любой пользователь ниже уровня админ захочет изменить о себе информацию в приложении, к примеру изменить имя,
запрос на изменение имени будет приходить администраторам на страницу где они должны подтвердить изменения, только после
этого данные изменятся.</li>

<li>SETTINGS/SETTINGS:
Настройка самого приложения, настройки внешнего вида и прочее.</li>

<li>SETTINGS/RESTAURANT:
Настройки ресторана, где будет настраиваться сам зал и карты меню кухни, и меню бара. Предполагаю, что графического
интерфейса с нарисованными столами разного цвета в зависимости от заказа быть не должно, вместо этого будет что то
похожее на кнопки, которые будут появляться после совершения заказа, на которых будет написано: стол 1, стол 2 и т.д.<\li>

<li>1. Главная страница - страница авторизации. После авторизации пользователь попадает на страницу
связанную с его правами доступа.</li>
<li>2. Создать модели связанные с моделью User, прописать пермишен по типу модели, if администратор то попадаешь
на /admin url, elif обслуживающий персонал то /service, elif персонал кухни то /kitchen.</li>


<li>СТРАНИЦА SERVICE :
Начинается со страницы, в центре которой большое поле, на котором отображаются существующие заказы, где нибудь по краям
кнопка "новый заказ", так же должно присутствовать изменение заказа, закрытие заказа. Так же, рассчитать заказ (закрыть
его посредством оплаты заказа) может любой, но закрыть без оплаты только администратор. Сделать так, что бы уведомление
приходило в аккаунт админа, что бы он мог удаленно подтвердить удаление, и ему не пришлось идти через весь зал.</li>
</ul>


Установлено в проект:
django
psycopg2 для postgreSQL DB
djangorestframework


26.1.; Коротко на ближайшие задачи:
Прописать страницу с регистрацией пользователя                                                                            +
При переходе на главную страницу сайта '', прописать вью:                                                                 +
Если количество юзеров в моделе юзерс = 0 (в тестовом варианте <= 1 так как будет создан суперюзер для работы) то:        +
Мы будем переадресованы на страницу регистрации где создадим первого пользователя. Посколько количество юзеров = 0,       +
то первый созданный пользователь автоматически попадет в группу администраторов с правами доступа администратора.         +
Предварительно создать группу и назвать Admins, выдать ей права полного доступа.                                          +

27.1; Сделать переход после регистрации на страницу авторизации. При выходе из системы сделать переход на другую страницу +
