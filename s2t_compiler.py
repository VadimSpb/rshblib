import pandas as pd


class S2tObj:

    def __init__(self):
        self.phys_model = None
        self.source_sheet = None
        self.target_sheet = None
        self.mapping_sheet = None
        self.len = None
        self.info = None

        #
        # try:
        #     df.__class__ = pd.core.frame.DataFrame
        # except TypeError:
        #     print('Use pandas Dataframe please')
        # else:
        #     self.stencil = df
        #     self.len = len(df.index)
        #     self.report = []

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

        # Init source sheet:
        self.source_sheet = pd.DataFrame()
        self.source_sheet['Система-источник'] = pd.Series([source_db for _ in range(self.len)])
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
        self.target_sheet['База данных'] = pd.Series([target_db for _ in range(len(tabs.index))])
        self.target_sheet['Целевая схема данных'] = target_db
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
