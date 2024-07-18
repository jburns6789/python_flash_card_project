# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html


# pandas.DataFrame.to_dict
# DataFrame.to_dict(orient='dict', *, into=<class 'dict'>, index=True)[source]
# Convert the DataFrame to a dictionary.
#
# The type of the key-value pairs can be customized with the parameters (see below).
#
# Parameters:
# orientstr {‘dict’, ‘list’, ‘series’, ‘split’, ‘tight’, ‘records’, ‘index’}
# Determines the type of the values of the dictionary.
#
# ‘dict’ (default) : dict like {column -> {index -> value}}
#
# ‘list’ : dict like {column -> [values]}
#
# ‘series’ : dict like {column -> Series(values)}
#
# ‘split’ : dict like {‘index’ -> [index], ‘columns’ -> [columns], ‘data’ -> [values]}
#
# ‘tight’ : dict like {‘index’ -> [index], ‘columns’ -> [columns], ‘data’ -> [values], ‘index_names’ -> [index.names], ‘column_names’ -> [column.names]}
#
# ‘records’ : list like [{column -> value}, … , {column -> value}]
#
# ‘index’ : dict like {index -> {column -> value}}

