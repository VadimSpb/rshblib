import pandas as pd


class S2tObj:

    def __init__(self):
        self.phys_model = None
        self.source_sheet = None
        self.target_sheet = None
        self.mapping_sheet = None
        self.len = None
        self.info = None
        self._lens = []

    def _check_pd_series(self, series=None):
        if type(series) is None:
            return None
        elif type(series) == pd.core.series.Series:
            self._lens.append(len(series.index))
            return series
        elif type(series) in [str, int, float]:
            series = str(series)
            return pd.Series([series for _ in range(self.len)])
        else:
            print('Use pandas.core.series.Series. Input data was changed to None')
            return None

    def form(self,
             source_db='Oracle',
             source_schema='cftf02',
             target_db='ODS',
             tab_name_source=None,
             tab_name_target=None,
             tab_comment=None,
             col_name=None,
             col_comment=None,
             col_index=None,
             col_type=None,
             data_length=None,
             nullable=None
             ):
        self.len = tab_name_source.size
        source_db = self._check_pd_series(source_db),
        source_schema = self._check_pd_series(source_schema),
        target_db = self._check_pd_series(target_db),
        tab_name_source = self._check_pd_series(tab_name_source),
        tab_name_target = self._check_pd_series(tab_name_target),
        tab_comment = self._check_pd_series(tab_comment),
        col_name = self._check_pd_series(col_name),
        col_comment = self._check_pd_series(col_comment),
        col_index = self._check_pd_series(col_index),
        col_type = self._check_pd_series(col_type),
        data_length = self._check_pd_series(data_length),
        nullable = self._check_pd_series(nullable)
        if len(set(self._lens)) > 1:
            print(f'All pd.series should have the same length, but {self._lens} are now')

        # Init source sheet:
        self.source_sheet = pd.DataFrame()
        self.source_sheet['Система-источник'] = source_db
        self.source_sheet['Схема в системе-источнике'] = source_schema
        self.source_sheet['Наименование таблицы'] = tab_name_source
        self.source_sheet['Наименование атрибута'] = col_name
        self.source_sheet['Комментарий к атрибуту'] = col_comment
        self.source_sheet['Тип данных'] = col_type
        self.source_sheet['РК'] = ''
        self.source_sheet['Not Null'] = nullable
        self.source_sheet['Описание таблицы'] = tab_comment
        self.source_sheet['Схема таблицы приёмника'] = target_db
        self.source_sheet['Таблица-приёмник'] = tab_name_target
        self.source_sheet['Набор данных'] = ''
        self.source_sheet['Поле набора данных'] = ''

        # Init target's tables sheet:
        self.target_sheet = pd.DataFrame()

        tabs = (
            self.source_sheet[['Схема таблицы приёмника', 'Таблица-приёмник', 'Описание таблицы']]
                .groupby('Таблица-приёмник').nth(0, dropna='any')
                .reset_index()
        )
        self.target_sheet['База данных'] = target_db
        self.target_sheet['Целевая схема данных'] = source_schema
        self.target_sheet['Наименование таблицы'] = tabs['Таблица-приёмник']
        self.target_sheet['Краткое описание таблицы'] = tabs['Описание таблицы']
        self.target_sheet['Расширенное описание таблицы'] = ''
        self.target_sheet['Обработка ошибок'] = ''
        self.target_sheet['Дополнительные описания и руководства'] = ''

        # Init mapping sheet:
        self.mapping_sheet = pd.DataFrame()
        # source columns
        self.mapping_sheet['Наименование'] = tab_name_source
        self.mapping_sheet['Код атрибута '] = col_name
        self.mapping_sheet['Описание атрибута'] = col_comment
        self.mapping_sheet['Тип данных'] = col_type
        self.mapping_sheet['Комментарий'] = ''
        self.mapping_sheet['Алгоритм'] = ''
        # target columns
        self.mapping_sheet['Схема'] = target_db
        self.mapping_sheet['Таблица'] = tab_name_target
        self.mapping_sheet['Код атрибута'] = col_index
        self.mapping_sheet['Атрибут'] = col_name
        self.mapping_sheet['Описание атрибута'] = col_comment
        self.mapping_sheet['Расширенное описание атрибута'] = ''
        self.mapping_sheet['Тип данных'] = col_type
        self.mapping_sheet['Длина'] = data_length
        self.mapping_sheet['PK'] = ''
        self.mapping_sheet['FK'] = ''
        self.mapping_sheet['Not Null'] = nullable
        self.mapping_sheet['Проверка'] = ''
        self.mapping_sheet['Отслеживание новых значений'] = ''
        self.mapping_sheet['Ссылка на атрибут сущности'] = ''
        # status columns
        self.mapping_sheet['Статус'] = ''
        self.mapping_sheet['Версия'] = ''

        # Init physical model:
        self.phys_model = pd.DataFrame()

        self.phys_model['Схема данных'] = pd.Series([source_schema for _ in range(self.len)])
        self.phys_model['Наименование таблицы'] = tab_name_source
        self.phys_model['Наименование атрибута'] = col_name
        self.phys_model['Описание атрибута'] = col_comment
        self.phys_model['Тип данных атрибута'] = col_type
        self.phys_model['PK'] = ''
        self.phys_model['FK'] = ''
        self.phys_model['UK'] = ''
        self.phys_model['Not Null'] = nullable
        self.phys_model['Описание таблицы'] = tab_comment
        self.phys_model['Ссылка на сущность БТ'] = ''
        self.phys_model['Ссылка на атрибут БТ'] = ''
