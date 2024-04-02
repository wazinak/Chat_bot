from random import randint
from aiogram import F, types, Router
from Database.requests import get_random_cider
from buttons import create_pagination_keyboard, info_btn, basic_concepts_btn, back_btn, podacha_btn, back_podacha_btn, \
    random_btn
from info_text import text_text, users_db, lEXI_CONCEPTS, class_ciders

router = Router()


@router.callback_query(F.data == "random_value")
async def random_value(callback: types.CallbackQuery):
    await send_random_value(callback, randint(1, 316))


async def send_random_value(callback: types.CallbackQuery, id: int):
    ciders = await get_random_cider(id)
    message_text = ""
    if ciders:
        for cider in ciders:
            message_text += (f"<b>Название:</b>\n{cider.name}\n"
                             f"<b>Производитель:</b>\n{cider.manufacture}\n"
                             f"<b>Содержание алкоголя:</b> {cider.alco}\n"
                             f"<b>Сухость:</b> {cider.sour}\n"
                             f"<b>Страна:</b> {cider.country}\n"
                             f"<b>Регион:</b> {cider.region}\n"
                             f"<i>Описание:</i>\n{cider.description}\n"
                             "\n"
                             )
        await callback.answer('')
        await callback.message.edit_text(
            text=message_text,
            parse_mode="HTML",
            reply_markup=random_btn(),
        )
    else:
        await callback.answer("Информация о напитке не найдена")


@router.callback_query(F.data == "history_cider")
async def history_cider(callback: types.CallbackQuery):
    users_db['page'] = 1
    text = text_text[users_db['page']]
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard(
            'back',
            f'{users_db["page"]}/{len(text_text)}',
            'forward',
            'return'
        )
    )


@router.callback_query(F.data == "podacha_cider")
async def super_cider(callback: types.CallbackQuery):
    await callback.message.edit_text(text='Здесь нужно выбрать страну по подаче сидра:', reply_markup=podacha_btn())


@router.callback_query(F.data == "basic_concepts")
async def basic_concepts_terms(callback: types.CallbackQuery):
    keyboard = basic_concepts_btn(2, **lEXI_CONCEPTS)
    await callback.message.edit_text(text='Вот что у меня есть:', reply_markup=keyboard)


@router.callback_query(F.data == "classific_ciders")
async def basic_concepts_terms(callback: types.CallbackQuery):
    users_db['page'] = 1
    text = class_ciders[users_db['page']]
    await callback.message.edit_text(
        text=text,
        parse_mode="HTML",
        reply_markup=create_pagination_keyboard(
            'going_backward',
            f'{users_db["page"]}/{len(class_ciders)}',
            'going_forward',
            'return'
        )
    )


@router.callback_query(F.data == 'going_backward')
async def going_back(callback: types.CallbackQuery):
    if users_db['page'] > 1:
        users_db['page'] -= 1
        text = class_ciders[users_db['page']]
        await callback.message.edit_text(
            text=text,
            parse_mode="HTML",
            reply_markup=create_pagination_keyboard(
                'going_backward',
                f'{users_db["page"]}/{len(class_ciders)}',
                'going_forward',
                'return'
            )
        )
        await callback.answer()


@router.callback_query(F.data == 'going_forward')
async def going_forward(callback: types.CallbackQuery):
    if users_db['page'] < len(class_ciders):
        users_db['page'] += 1
        text = class_ciders[users_db['page']]
        await callback.message.edit_text(
            text=text,
            parse_mode="HTML",
            reply_markup=create_pagination_keyboard(
                'going_backward',
                f'{users_db["page"]}/{len(class_ciders)}',
                'going_forward',
                'return'
            )
        )
        await callback.answer()


@router.callback_query(F.data == 'back')
async def go_back(callback: types.CallbackQuery):
    if users_db['page'] > 1:
        users_db['page'] -= 1
        text = text_text[users_db['page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'back',
                f'{users_db["page"]}/{len(text_text)}',
                'forward',
                'return'
            )
        )
        await callback.answer()


@router.callback_query(F.data == 'forward')
async def go_forward(callback: types.CallbackQuery):
    if users_db['page'] < len(text_text):
        users_db['page'] += 1
        text = text_text[users_db['page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'back',
                f'{users_db["page"]}/{len(text_text)}',
                'forward',
                'return'
            )
        )
        await callback.answer()


@router.callback_query(F.data == 'return')
async def go_return(callback: types.CallbackQuery):
    await callback.message.edit_text(text="Здесь должна быть краткая информация о сидрах",
                                     reply_markup=info_btn())


@router.callback_query(F.data == 'tanin')
async def go_tanin(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text="<i>Танинность</i> – танины  - природные химические соединения, которые содержатся "
             "в кожуре и семенах яблок и груш. Научное название этих соединений – "
             "полифенолы.Терпкость и “сухой рот” – основные индикаторы танинов.",
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'terroir')
async def go_terroir(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Терруар</i> – это слово происходит от латинского – «земля», «почва». Терруар – это среда '
             'происхождения,то есть совокупность всех местных факторов, влияющих на напиток. В это понятие входят '
             'почва,'
             'на которой растет дерево, климат и расположение. А терруарные сидры – это сидры в букете которых '
             'различимы эти особенности.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'avtotoh')
async def go_avtotoh(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Автохтонность</i> – если очень просто, то можно сказать слово «коренной», то есть или сидры, '
             'которые производятся в данном регионе очень-очень давно, или деревья, которые растут на данной '
             'территории очень давно.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'artisanal')
async def go_artisanal(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Артизанальность</i> – это аналог слову «крафт», то есть это довольно локальные производства. В '
             'переводе с Французского – «кустарный», «сделанный вручную».',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'ferment')
async def go_ferment(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Ферментация</i> – это процесс в ходе которого дрожжи перерабатывают сахар в этиловый спирт. Также, '
             'в ходе процесса выделяется довольно много углекислого газа и тепла.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'mezga')
async def go_mezga(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Мезга</i> - она же жмых - яблочная мякоть, из которой был выжат весь сок.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'macerac')
async def go_macerac(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Мацерация</i> – сам процесс представляет собой настаивание, но если чуть более точно то, отжатый сок '
             'настаивается вместе со жмыхом, так как в косточках и кожуре содержится много веществ отвечающих за вкус '
             'и запах напитка.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'carbor')
async def go_carbor(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Карбонизация</i> – это процесс насыщения напитка углекислым газом. Карбонизация может быть как '
             'искусственной (газ подается под давлением в герметичную тару), так и натуральной (при розливе в бутылки '
             'добавляют новую питательную среду для дрожжей).',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'sulfat')
async def go_sulfat(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Сульфатирование</i> – это процесс заключающийся в добавлении к свежему суслу диоксида серы. '
             'Применяется диоксид серы в качестве консерванта. Он позволяет защитить продукт от окисления.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'remuiaj')
async def go_remuiaj(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Ремюаж</i>  – процедура, которая заключается в  сборе всего дрожжевого осадка у пробки. Сама суть в '
             'том, что бутылки подвешивают горлышком вниз под углом в 45 градусов и каждый 1-2 дня по чуть-чуть '
             'проворачивают. Эта процедура может продолжаться от 2 недель до 3 месяцев.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'degorjaj')
async def go_degorjaj(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Дегоржаж</i> – процесс удаления осадка из бутылки после ремюажа. Бутылку в положении горлышком вниз '
             'подмораживают, после чего при откупоривании осадок выбрасывается давлением из бутылки и ее снова '
             'закупоривают, на этот раз уже окончательно.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'kiving')
async def go_kiving(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Кивинг</i> – традиционный французский метод удаления из сидра пектина(он выделяется из яблок после '
             'их измельчения) и питательных веществ для дрожжей. В яблочный сок добавляют ферменты, которые начинают '
             'взаимодействовать с пектином и на поверхности образуется гелиевая шапка. Этот гель связывает белки и '
             'создает осадочный слой, при этом под ним абсолютно чистый сидр, но гелиевая шапка занимает около '
             '10-20%. Благодаря этому сахар уходит не весь и сидр остается сладковатым. После чего сидр разливают и '
             'он дображивает в бутылке, создавая газацию.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'pasteriz')
async def go_pasteriz(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Пастеризация</i> – это тепловая обработка при температурах меньше 100 градусов, для уничтожения '
             'болезнетворных микроорганизмов',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'mineral')
async def go_mineral(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Минеральность сидра</i> – во вкусе минеральных сидров обычно выделяются нотки солоноватости, '
             'йодистости и некоторой свежести.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'monosort')
async def go_monosort(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Моносортовые  (моносепажные) и купажированные сидры</i> – моносортовые сидры это те, в составе '
             'которых груши или яблоки только одного сорта, соответственно в купажированных сочетаются несколько '
             'сортов.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'selek_sort')
async def go_selek_sort(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Селекционные сорта</i>  – это сорта яблок, которые выводят специально, с нужными для человека '
             'свойствами, занятого определенной деятельностью с этим фруктом. То есть кислые, кисло-горькие, сладкие.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'petnat')
async def go_petnat(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Петнат</i> - от французского pét-nat или pétillant naturel, – дословно «натуральное игристое» '
             'делается по старинной технологии одиночного брожения, другими словами это дедовский метод производства. '
             'Чтобы получился петнат, достаточно укупорить любое недобродившее вино и подождать, пока первичная '
             'ферментация возобновится, например, при повышении окружающей температуры на пару градусов и завершится '
             'уже в бутылке. В закрытом сосуде выделяющийся при ферментации газ растворяется в жидкости, делая вино '
             'игристым. Все эти игристые отличает слабый перляж и невысокий алкоголь, что роднит их скорее с сидром, '
             'чем с вином, а бутылки часто укупоривают жестяной пробкой как пиво. Петнаты обычно не фильтруют, '
             'отдавая дань аутентичности производства, и вообще редко подвергают каким-либо дополнительным '
             'манипуляциям.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'perlij')
async def go_perlij(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='<i>Перляж</i> - винодельческий термин для обозначения игры пузырьков углекислого газа в бокале '
             'игристого вина, поднимающихся к поверхности стройными дорожками.',
        parse_mode="HTML",
        reply_markup=back_btn())


@router.callback_query(F.data == 'podacha_spain')
async def podacha_spain(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='Чтобы прочувствовать вкус настоящего сидра, важно соблюсти технологию не только его производства, '
             'но и подачи. В правильном процессе подачи напиток пенится и становится шипучим, из него выделяется '
             'углекислый газ. Пока он не вышел полностью, пьющий должен опустошить стакан. Залпом! Поэтому сидра '
             'наливают ровно на два пальца специальным аппаратом –  эскансиадором либо вручную. Ценители предпочитают '
             'второй вариант. Одной рукой специально обученный официант поднимает бутылку с сидром как можно выше над '
             'головой, а другую, со стаканом, опускает вниз. Считается, что «разбившийся» с полутораметровой высоты и '
             'обогащенный кислородом напиток обретает все тонкости вкуса. Чем меньше сидра при этом прольет '
             'виночерпий-человек эскансиадор, тем выше считается его квалификация. Впрочем, широкие края стакана, '
             'который по-астурийски называется «кулин», не дают промахнуться.',
        parse_mode="HTML",
        reply_markup=back_podacha_btn())


@router.callback_query(F.data == 'podacha_french')
async def podacha_french(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='Несмотря на то, что сердце французов принадлежит вину, сидр занимает не менее важную роль в жизни '
             'каждого жителя этой страны. Во Франции с большим вниманием подходят к процедуре распития яблочного '
             'игристого напитка, а соответственно и к выбору посуды. Традиционно его пили из керамических пиал BOLÉE '
             '– «БОЛЭ», но сейчас всё чаще и чаще используют винные бокалы. При этом если сидр сухой и терпкий, '
             'то его разливают в Бордо, а если он полусладкий, то скорее его подадут в бокале для белого вина. Бокалы '
             'флюте стараются не использовать потому что они не дают прочувствовать всю ароматику.',
        parse_mode="HTML",
        reply_markup=back_podacha_btn())


@router.callback_query(F.data == 'podacha_uk')
async def podacha_uk(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='Англосаксы пьют сидр из классических пивных бокалов - пинт. Этому есть своё объяснение: что англичане, '
             'что американцы традиционно позиционируют сидр, как напиток близкий к пиву. Английские сидры чаще всего '
             'сильногазированные, поэтому подаются прямо как хмельной напиток. Также сидры с Британского острова '
             'отличает их высокая питкость. Кто бы что ни говорил, но сладкий, газированный сидр пить проще, '
             'чем испанский кисляк или французский сухарь. Соответственно, выпить пол литра такого напитка не '
             'составит никакого труда – вы попросту его не заметите. Кстати, отсюда логично вытекает тот факт, '
             'что в Великобритании – самый высокий в мире уровень потребления яблочного напитка на душу населения.',
        parse_mode="HTML",
        reply_markup=back_podacha_btn())
