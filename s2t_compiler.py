import pandas as pd


class S2tObj:

    def __init__(self, df):
        try:
            df.__class__ = pd.core.frame.DataFrame
        except TypeError:
            print('Use pandas Dataframe please')
        else:
            self.stencil = df
            self.len = len(df.index)
            self.report = []



    def fit(
            self,
            tab_name_oracle=None,
            tab_name_hive=None,
            tab_comment=None,
            col_name=None,
            col_comment=None,
            col_index=None,
            col_type=None,
            nullable=None
    ):








#
# class SimpleTable:
#     """
#     base class for compile source-to-target document
#     """
#     def __init__(self,
#                  stencil_df,
#                  # tab_name_col=self.stencil_df.columns[0],
#                  # tab_comment_col=self.stencil_df.columns[1],
#                  # col_name_col=stencil_df.columns[2],
#                  # col_comment_col=stencil_df.columns[3]
#                  tab_name_col=None,
#                  tab_comment_col=None,
#                  col_name_col=None,
#                  col_comment_col=None):
#         """
#         Init source-to-target document
#         :param fresh_df: pd.DataFrame
#         """
#         # self.fresh_df = fresh_df.drop_duplicates()
#         try:
#             stencil_df.__class__ == pd.core.frame.DataFrame
#         except TypeError:
#             print('Use pandas Dataframe please')
#         else:
#             self.stencil_df = stencil_df
#             self.len = self.stencil_df.index
#             self.source_sheet = None
#             self.target_sheet = None
#             self.mapping_sheet = None
#             self.history_sheet = None
#
#     def init_S2T(self):
#         """"""
#
#
#     def prettify(self) -> pd.core.frame.DataFrame:
#         """
#         Remove all whitespace symbols from table names and  column names
#         :return: pd.core.frame.DataFrame
#         """
#         pass
#
#
#     def analyse(self):
#         """
#
#         :return:
#         """
#         pass
#
#
#     # Дополнить фильтр только таблиц с именами таблиц и атрибутов
#     # def prettify(self, cols=[]):
#     #     """
#     #     Strip whitespace symbols and change all values to uppercase
#     #     :return:
#     #     """
#     #     for col in cols:
#     #         if col in self.stencil_df.columns:
#     #             self.stencil_df[col] = self.stencil_df[col].str.strip('\s+').str.upper()
#
#     def init_s2t(self,
#                  tab_name,
#                  tab_comment,
#                  attr,
#                  attr_comment,
#                  data_type=None,
#                  not_null=None):
#         """
#
#         :param tab_name: pandas array with table's names
#         :param tab_comment: pandas array with table's descriptions
#         :param attr: pandas array with attribute's names
#         :param attr_comment: pandas array with attribute's descriptions
#         :param data_type: pandas array with attribute's data types
#         :param not_null: pandas array with (boolean)
#         :return: source_to_target document as pandas DataFrame
#         """
#         self.tab_name = tab_name
#         self.tab_comment = tab_comment
#         self.attr = attr
#         self.attr_comment = attr_comment
#         self.data_type = data_type
#         self.not_null = not_null
