# Основы программирования на Python

Добро пожаловать на курс основ программирования на языке программирования Python :snake:

# Цели курса

Этот курс преследует несколько основных целей:

Курс долен предоставить подробное и наглядное изложение основных аспектов языка 
программирования Python. Курс имеет модульную структуру и построен по принципу 
"от простого к сложному". В самом начале предлагается ознакомиться с достоинствами и
недостатками Python как одного из инструментов разработки программного обеспечения, 
а также с его основными принципами. В последующих частях приводится описание основных 
синтаксических конструкций и инструментов, которые предоставляет Python в стандартной 
библиотеке. Таким образом, можно сразу перейти к нужному материалу или пропустить 
часть известного.

Курс должен служить структурированным пособием для специалистов, которые только 
начали изучать программирование и, в частности, Python. По завершению этого курса 
студент должен овладеть навыками написания собственных программ на Python, 
а также чтения чужого кода.

Курс является частью образовательной программы по основам программирования и должен 
облегчить доступ студентов к полезным материалам. Однако, он направлен не только 
на студентов, но и будет полезен для людей, решивших начать изучения Python. 

# Для кого предназначен этот курс?

Курс направлен на студентов инженерных специальностей, которые хотят начать 
изучения Python. Проходить курс могут не только студенты, изучающие в программирование 
в рамках учебного заведения, но и любой желающий в удобном для себя темпе, в этом 
случае необходимо самостоятельно выполнять примеры и задания. Для прохождения курса 
не требуется дополнительных знаний других языков или самого Python, однако, они будут, 
несомненно, полезны.

# С чего начать?

Вы можете использовать курс как справочник, выполняя примеры в вашей рабочей среде. 
О том, какое дополнительной программное обеспечение потребуется для прохождения 
курса будет описано в первой теме "Введение в Python". Также вы можете клонировать 
репозиторий в вашу локальную директорию, выполнив следующие команды в командной 
строке :octocat: :

```cmd
git clone https://github.com/redb0/python-bp.git
```

Настоятельно рекомендуется выполнять каждый пример самостоятельно, а также модифицировать код. 

# Поддержка

Если вы увлеченно интересуетесь Python, подумайте над тем, чтобы стать участником проекта. 
Если вы хотите принять участие в проекте создайте ```issues``` и предложите новую 
тему/задание/пример/литературу или исправление ошибок.

Пожалуйста, прочтите наш [кодекс поведения](CODE_OF_CONDUCT.md) и [правила коллективного участия](CONTRIBUTING.md). Там 
описаны инструкции по открытию ```issues```, стандарты кодирования и прочие правила.

# Содержание

1. [**Введение в Python**](python_pd/01_intro/00_overview.md)
    <!-- - [О Python](python_pd\01_introduction\introduction.md#o-python)
    - [Почему стоит изучать Python](python_pd\01_introduction\introduction.md#почему-стоит-изучать-python?)
    - Недостатки Python
    - Принципы Python
    - Руководство по написанию кода
    - О примерах кода
    - Необходимое ПО и зависимости
    - Проверка кода на соответствие стандарту
    - Python и командная строка -->
    <!-- - Виртуальное окружение -->
    <!-- - Полезные ссылки -->
2. [**Синтаксис**](python_pd/02_syntax/00_overview.md)
    - [Простые типы данных (числа | логический | NoneType | строки)](python_pd/02_syntax/01_simple_types.ipynb)
    - [Переменные и выражения](python_pd/02_syntax/02_variables.ipynb)
    - [Управляющие конструкции](python_pd/02_syntax/03_control_structures.ipynb)
    - [Кратко о функциях](python_pd/02_syntax/04_functions.ipynb)
    - [Типизация](python_pd/02_syntax/05_dtyping.ipynb)
3. [**Коллекции**](python_pd/03_collections/00_overview.md)
    - [Базовые коллекции](python_pd/03_collections/basic_collections/00_overview.md) 
    ([str](python_pd/03_collections/basic_collections/01_string.ipynb) | 
    [list](python_pd/03_collections/basic_collections/02_list.ipynb) | 
    [dict](python_pd/03_collections/basic_collections/03_dict.ipynb) | 
    [tuple](python_pd/03_collections/basic_collections/04_tuple.ipynb) | 
    [set](python_pd/03_collections/basic_collections/05_set.ipynb))
    - [Изменяемые и неизменяемые типы данных](python_pd/03_collections/01_im_mutable_and_copy.ipynb)
    - [Включения в список | словарь | множество | кортеж](python_pd/03_collections/02_comprehensions.ipynb)
    - [Модуль ```collections```](python_pd/03_collections/03_collections.ipynb)
    - [Итераторы](python_pd/03_collections/04_iter.ipynb)
    - [Модуль ```itertools```](python_pd/03_collections/05_itertools.ipynb)
4. [**Функции**](python_pd/04_functions/00_overview.md)
    - [Аргументы функций](python_pd/04_functions/01_args.ipynb)
    - [Возвращаемое значение](python_pd/04_functions/02_return.ipynb)
    - [Анонимные функции](python_pd/04_functions/03_lambda.ipynb)
    - [Области видимости](python_pd/04_functions/04_legb.ipynb)
    - [Замыкания](python_pd/04_functions/06_closures.ipynb)
    - [Декораторы](python_pd/04_functions/07_decorators.ipynb)
    - [Генераторы](python_pd/04_functions/08_generators.ipynb)
    - [Модуль ```functools```](python_pd/04_functions/09_functools.ipynb)
    - [Исключения](python_pd/04_functions/10_exceptions.ipynb)
5. [**Файлы**](python_pd/05_files/00_overview.md)
    - [Файлы. Чтение и запись](python_pd/05_files/01_files.ipynb)
    - [Модуль ```io```](python_pd/05_files/02_io.ipynb)
    - [Менеджер контекста](python_pd/05_files/03_cmanagers.ipynb)
    - Модули для работы с разными форматами 
    ([```txt```](python_pd/05_files/01_files.ipynb) | 
    [```json```](python_pd/05_files/04_json.ipynb) | 
    [```csv```](python_pd/05_files/05_csv.ipynb) | 
    [```pickle```](python_pd/05_files/06_pickle.ipynb))
    - Работа с путями 
    ([```os.path```](python_pd/05_files/07_os_path.ipynb) | 
    [```pathlib```](python_pd/05_files/08_pathlib.ipynb))
6. [**Классы**](python_pd/06_classes/00_overview.md)
    - [Классы и экземпляры класса](python_pd/06_classes/01_class.md)
    - [Атрибуты класса и экземпляра](python_pd/06_classes/02_attr.md)
    - [Методы](python_pd/06_classes/03_methods.md)
    - [Наследование](python_pd/06_classes/04_inheritance.md)
    - ["Магические" методы](python_pd/06_classes/05_magic.md)
    - [Протоколы](python_pd/06_classes/06_protocols.md)
    - [Утиная типизация](python_pd/06_classes/07_duck_typing.md)
    - [Дескрипторы и свойства](python_pd/06_classes/08_property.md)
    - [Декораторы классов](python_pd/06_classes/09_decorators.md)
    - [Абстрактные классы](python_pd/06_classes/10_abc.md)
    - [Метаклассы](python_pd/06_classes/11_meta.md)
7. [**Импорт**](python_pd/07_import/00_overview.md)
    - Модули и пакеты
    - Абсолютный и относительный импорт
    - Циклический импорт
    - Система импорта
    - Поиск модулей и пакетов
8. [**Примеры плохого кода**](python_pd/badcode.ipynb)