import pandas as pd


class SimpleTable:
    """
    base class for compile source-to-target document
    """
    def __init__(self, fresh_df):
        """
        Init source-to-target document
        :param fresh_df: pd.DataFrame
        """
        self.fresh_df = fresh_df.drop_duplicates()
        self.stencil_df = self.fresh_df
        self.len = self.fresh_df.index
        self.source_sheet = None
        self.target_sheet = None
        self.mapping_sheet = None
        self.history_sheet = None

    # Дополнить фильтр только таблиц с именами таблиц и атрибутов
    # def prettify(self, cols=[]):
    #     """
    #     Strip whitespace symbols and change all values to uppercase
    #     :return:
    #     """
    #     for col in cols:
    #         if col in self.stencil_df.columns:
    #             self.stencil_df[col] = self.stencil_df[col].str.strip('\s+').str.upper()

    def init_s2t(self,
                 tab_name,
                 tab_comment,
                 attr,
                 attr_comment,
                 data_type=None,
                 not_null=None):
        """

        :param tab_name: pandas array with table's names
        :param tab_comment: pandas array with table's descriptions
        :param attr: pandas array with attribute's names
        :param attr_comment: pandas array with attribute's descriptions
        :param data_type: pandas array with attribute's data types
        :param not_null: pandas array with (boolean)
        :return: source_to_target document as pandas DataFrame
        """
        self.tab_name = tab_name
        self.tab_comment = tab_comment
        self.attr = attr
        self.attr_comment = attr_comment
        self.data_type = data_type
        self.not_null = not_null
