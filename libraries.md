# Краткий обзор стандартной библиотеки Python

Стандартная библиотеку Python обширна. Она содержит большое количество
полезных модулей, позволяющих решить множество задач. С этим связано
одно из преимуществ Python: батарейки в комплекте. Ознакомиться с
перечнем модулей стандартной библиотеки можно по ссылке:
https://docs.python.org/3/library/index.html

В стандартной библиотеке Вы сможете найти:

1) полезные типы данных
(`collections` | `datetime` | `enum` | `decimal` и другие);
2) элементы функционального программирования
(`itertools` | `functools` | `operator`);
3) библиотеки для сериализации/десериализации данных и работе с файлами
(`json` | `csv` | `xml` | `pickle` | `shelve` | `sqlite3` | `zlib` и другие);
4) инструменты для работы с ОС
(`os` | `io` | `argparse` | `logging` и другие);
5) модули для параллельных вычислений
(`threading` | `multiprocessing` | `subprocess` | `asyncio`);
6) инструменты для работы с сетью
(`asyncio` | `socket` | `ssl` | `email` | `html` | `urllib` | `uuid`);
7) вспомогательные инструменты
(`typing` | `pydoc` | `doctest` | `unittest` | `timeit` | `venv`);
8) модули кастомизации импорта
(`importlib`);
9) и много интересных специализированных модулей
(`parser` | `ast` | `symbol` и другие).

Некоторые из них были рассмотрены в соответствующих главах курса.

# Подборка полезных сторонних покетов

Сайт pypi.org с каталогом сторонних пакетов:
https://pypi.org/

## 1. Веб

- django ([офф. сайт](https://www.djangoproject.com/), [github](https://github.com/django/django))
- Tornado ([офф. сайт](https://www.tornadoweb.org/en/stable/), [github](https://github.com/tornadoweb/tornado))
- Brython ([офф. сайт](https://brython.info/), [github](https://github.com/brython-dev/brython))
- Pyodide ([github](https://github.com/iodide-project/pyodide))
- Requests ([офф. сайт](https://requests.readthedocs.io/en/master/), [github](https://github.com/psf/requests))

## 2. Десктоп

- PyQt5 ([github](https://github.com/PyQt5))
- PySide6 ([офф. сайт](https://wiki.qt.io/Qt_for_Python), [github](https://github.com/PySide))

## 3. Мобилки

- kivy ([офф. сайт](https://kivy.org/#home), [github](https://github.com/kivy/kivy))
- qpython ([офф. сайт](https://www.qpython.com/), [github](https://github.com/qpython-android/qpython/releases))

## 4. Разработка игр

- Pygame ([офф. сайт](https://www.pygame.org/news), [github](https://github.com/pygame/pygame))
- pyxel ([github](https://github.com/kitao/pyxel?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more))
- RenPy ([офф. сайт](https://www.renpy.org/), [github](https://github.com/renpy/renpy))

## 5. Что-то посчитать

- numpy ([офф. сайт](https://numpy.org/), 
         [github](https://github.com/numpy/numpy), 
         [документация](https://numpy.org/doc/stable/),
         [туториал](https://numpy.org/doc/stable/user/tutorials_index.html))
- sympy ([офф. сайт](https://www.sympy.org/en/index.html), 
         [github](https://github.com/sympy/sympy), 
         [документация](https://docs.sympy.org/latest/index.html),
         [туториал](https://docs.sympy.org/latest/tutorial/index.html))
- scipy ([офф. сайт](https://www.scipy.org/), 
         [github](https://github.com/scipy/scipy/), 
         [документация](https://docs.scipy.org/doc/),
         [туториал](https://docs.scipy.org/doc/scipy/reference/tutorial/index.html))
- Theano ([github](https://github.com/Theano/Theano)) - еще одна библиотека для вычислений (разработка прекращена)
- PyDSTool ([офф. сайт](https://pydstool.github.io/PyDSTool/FrontPage.html), 
            [github](https://github.com/robclewley/pydstool), 
            [документация](https://pydstool.github.io/PyDSTool/ToolboxDocumentation.html), 
            [туториал](https://pydstool.github.io/PyDSTool/Tutorial.html))
- QuTiP ([офф. сайт](http://qutip.org/), 
         [github](https://github.com/qutip), 
         [документация](http://qutip.org/documentation.html), 
         [туториал](http://qutip.org/tutorials.html))

Что есть еще?
- [AstroPy](https://www.astropy.org/) - астрономия
- [PsychoPy](https://www.psychopy.org/) - нейробиология, психофизика, психология.
- [BioPython](https://biopython.org/) - биоинформатика
- [PyChem](https://pubmed.ncbi.nlm.nih.gov/16882648/) - химия
- [Shapely](https://shapely.readthedocs.io/en/stable/) - география

И еще:
- [numdifftools](https://github.com/pbrod/numdifftools) - производные в любом проявлении


## 6. Что-то визуализировать

- matplotlib ([офф. сайт](https://matplotlib.org/), 
              [github](https://github.com/matplotlib/matplotlib), 
              [документация](https://matplotlib.org/contents.html), 
              [туториал](https://matplotlib.org/tutorials/index.html))
- seaborn ([офф. сайт](https://seaborn.pydata.org/),
           [github](https://github.com/mwaskom/seaborn),
           [туториал](https://seaborn.pydata.org/tutorial.html))
- Mayavi ([офф. сайт](https://docs.enthought.com/mayavi/mayavi/), 
          [github](https://github.com/enthought/mayavi))
- manim ([github](https://github.com/3b1b/manim), 
         [документация](https://eulertour.com/docs/))
- Dash ([офф. сайт](http://dash.plotly.com/), [github](https://github.com/plotly/dash))

## 7. Как собрать данные?

- BeautifulSoup ([офф. сайт](), [github]())
- scrapy ([офф. сайт](), [github]())

## 8. А как хранить будем?

- psycopg2/3 ([офф. сайт](https://www.psycopg.org/), [github](https://github.com/psycopg/psycopg2)) - PostgreSQL
- SqlAlchemy ([офф. сайт](https://www.sqlalchemy.org/), 
              [github](https://github.com/sqlalchemy/sqlalchemy)) - PostgreSQL | MySQL | SQLite | Oracle | Microsoft SQL Server
- pyobdc ([github](https://github.com/mkleehammer/pyodbc))

## 9. Анализ данных

- pandas ([офф. сайт](https://pandas.pydata.org/), 
          [github](https://github.com/pandas-dev/pandas), 
          [документация](https://pandas.pydata.org/docs/), 
          [туториал](https://pandas.pydata.org/docs/user_guide/index.html))
- statsmodels ([офф. сайт](https://www.statsmodels.org/stable/index.html), 
               [github](https://github.com/statsmodels/statsmodels),
               [туториал](https://www.statsmodels.org/stable/user-guide.html))
- nltk ([офф. сайт](http://www.nltk.org/), [github](https://github.com/nltk/nltk))

## 10. Все для создания Skynet

- scikit-learn ([офф. сайт](https://scikit-learn.org/stable/), [github](https://github.com/scikit-learn/scikit-learn))
- xgboost ([офф. сайт](https://xgboost.readthedocs.io/en/latest/), [github](https://github.com/dmlc/xgboost))
- OpenCV ([офф. сайт](https://docs.opencv.org/master/), [github](https://github.com/skvark/opencv-python))
- pytorch ([офф. сайт](https://pytorch.org/), [github](https://github.com/pytorch/pytorch))
- tensorflow ([офф. сайт](https://www.tensorflow.org/learn), [github](https://github.com/tensorflow/tensorflow))
- keras ([офф. сайт](https://keras.io/), [github](https://github.com/keras-team/keras))

## 11. Качество кода

- pylint ([офф. сайт](https://github.com/PyCQA/pylint), [github](https://www.pylint.org/))
- flake8 ([офф. сайт](https://flake8.pycqa.org/en/latest/), [github](https://github.com/PyCQA/flake8))
- pylama ([офф. сайт](http://klen.github.io/pylama.html), [github](https://github.com/klen/pylama))
- mypy ([офф. сайт](http://www.mypy-lang.org/), [github](https://github.com/python/mypy))
- MonkeyType ([github](https://github.com/Instagram/MonkeyType))
- pyannotate ([github](https://github.com/dropbox/pyannotate))

## 12. Просто полезные штуки

- pytest ([офф. сайт](https://docs.pytest.org/en/stable/), [github](https://github.com/pytest-dev/pytest))
- virtualenv ([офф. сайт](https://virtualenv.pypa.io/en/latest/), [github](https://github.com/pypa/virtualenv))
- sphinx ([офф. сайт](https://www.sphinx-doc.org/en/master/), [github](https://github.com/sphinx-doc/sphinx))
- Jupyter ([офф. сайт](https://jupyter.org/), [github](https://jupyter.org/))
- geopy ([офф. сайт](https://geopy.readthedocs.io/en/stable/), [github](https://github.com/geopy/geopy))
- tabulate ([github](https://github.com/astanin/python-tabulate))
- Pillow ([офф. сайт](https://python-pillow.org/), [github](https://github.com/python-pillow/Pillow))

## Где применять?

1) Открытие гравитационных волн: 
    - https://numpy.org/case-studies/gw-discov/
    - https://www.youtube.com/watch?v=7mcHknWWzNI&feature=youtu.be
2) Первое фото черной дыры: 
    - https://numpy.org/case-studies/blackhole-image/
