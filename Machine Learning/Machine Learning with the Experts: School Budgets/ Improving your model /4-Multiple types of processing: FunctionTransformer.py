# Import FunctionTransformer
from sklearn.preprocessing import FunctionTransformer

# Obtain the text data: get_text_data
get_text_data = ____(lambda x: x['____'], validate=False)

# Obtain the numeric data: get_numeric_data
get_numeric_data = ____(lambda ____: ____[[____, ____]], validate=False)

# Fit and transform the text data: just_text_data
just_text_data = get_text_data.fit_transform(____)

# Fit and transform the numeric data: just_numeric_data
just_numeric_data = ____

# Print head to check results
print('Text Data')
print(just_text_data.head())
print('\nNumeric Data')
print(just_numeric_data.head())
