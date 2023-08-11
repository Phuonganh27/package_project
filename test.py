from dataExplorer import DataExplorer

data_explorer = DataExplorer(file_name='./survey_results_public.csv')

data_explorer.summary()
data_explorer.missing_data_info()
data_explorer.histogram()
data_explorer.heat_map()
