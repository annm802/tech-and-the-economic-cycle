
import pandas as pd
def string_to_datetime(the_dataframe, datetime_column):
  '''
  This converts a datetime column that is in the string format into a datetime format

  :the_dataframe: The dataframe containing the datetime_column
  :datetime_column: column that is in the string format

  returns: an updated dataframe with the datetime_column in the "datetime" format

  example:

  string_to_datetime(df, 'date')
  '''
  the_dataframe[datetime_column] = pd.to_datetime(the_dataframe[datetime_column])

  return the_dataframe

def date_range_filter(the_dataframe, datetime_column, datetime_range):

  '''
  This returns data instances collected past the specified datetime range

  :the_dataframe: The dataframe containing the datetime_column- string format
  :datetime_column: datetime column- this has to be in the datetime format
  :datetime_range: yyyy-mm-dd


  returns: a dataframe of instances that occurred after the given datetime range

  example:

  date_range_filter(df, "date", "2005-01-01" )
  '''
  the_dataframe = the_dataframe.loc[(the_dataframe[datetime_column] >= datetime_range)]

  return the_dataframe

def extra_white_spaces(the_dataframe, doc_column):
  '''
   This text data without any extra white spaces

  :the_dataframe: The dataframe
  :doc_column: column with text data

  returns: a dataframe with a doc_column that has single spaces

  example:

  extra_white_spaces(df, "abstracts" )
  '''
  the_dataframe[doc_column] = the_dataframe[doc_column].str.strip()

  return the_dataframe

def label_dictionary(adf, theme_column):
  '''
  This assigns unique numbers to labels in a dataframe

  :adf: a dataframe
  :theme_column: a column in the dataframe that contains names of the themes

  returns a dictionary {label_1:1, label_2:2, ... , label_n:n}
  '''
  labellist=sorted(list(set(adf[theme_column].unique())))

  labels={label:i for i,label in enumerate(labellist)}
  return labels


def reverse_idx(adict):
  '''
  This creates a reverse of the labels dictionary obtained in the previous function

  :adict: a dictionary in the form {label_1:1, label_2:2, ... , label_n:n}

  return a dictionary in the form {1:label_1, 2:label_2, ... , n:label_n}
  '''

  reverse_idx= {}
  for key,value in adict.items():
    reverse_idx[value]= key
  return reverse_idx

def map_labels(df, label_column, labeldict):
  '''
  This maps a dictionary onto a column

  :df: a dataframe
  :label_column: a column of labels
  :labeldict: a dictionary in the form {label_1:1, label_2:2, ... , label_n:n} or {1:label_1, 2:label_2, ... , n:label_n}

  returns a dataframe with an updated label_column showing the values of the labeldict, instead of the keys
  '''
  df[label_column] = df[label_column].map(labeldict)

  return df

def bust_phases(a_dataframe,date_column):
  '''
  This returns a new dataframe with data instances that fall within the bust phase of the economic cycle 2008-2023
  ''' 
  first_bust = a_dataframe.loc[(a_dataframe[date_column] >= '2008-01-01')
                     & (a_dataframe[date_column] <= '2009-12-31')]
  second_bust = a_dataframe.loc[(a_dataframe[date_column] >= '2020-01-01')
                     & (a_dataframe[date_column] <= '2020-12-31')]
  bust_phases =  pd.concat([first_bust,second_bust], axis=0)
  bust_phases = bust_phases.sort_values(by = date_column)
  bust_phases = bust_phases.reset_index(drop= True)

  return bust_phases

def boom_phases(a_dataframe,date_column):
  '''
  This returns a new dataframe with data instances that fall within the boom phase of the economic cycle 2008-2023
  ''' 
  first_bust = a_dataframe.loc[(a_dataframe[date_column] >= '2008-01-01')
                     & (a_dataframe[date_column] <= '2009-12-31')]
  second_bust = a_dataframe.loc[(a_dataframe[date_column] >= '2020-01-01')
                     & (a_dataframe[date_column] <= '2020-12-31')]
  bust_phases =  pd.concat([first_bust,second_bust], axis=0)
  bust_phases = bust_phases.sort_values(by=)
  bust_phases = bust_phases.reset_index(drop= True)

  first_peak = doc_topics.loc[(a_dataframe[date_column] >= '2010-01-01')
                     & (a_dataframe[date_column] <= '2010-12-31')]
  second_peak = doc_topics.loc[(a_dataframe[date_column] >= '2021-01-01')
                  & (a_dataframe[date_column] <= '2021-06-30')]

  first_stability= a_dataframe.loc[(a_dataframe[date_column]>= '2005-01-01')
                  & (a_dataframe[date_column] <= '2007-12-31')]
  second_stability = a_dataframe.loc[(a_dataframe[date_column]>= '2010-12-31')
                  & (a_dataframe[date_column]<= '2019-12-31')]
  third_stability = a_dataframe.loc[(a_dataframe[date_column] >= '2021-07-31')
                  & (a_dataframe[date_column] <= '2023-03-31')]

  booms=  pd.concat([first_stability, first_peak, second_stability, second_peak, third_stability ], axis=0)
  booms= booms.sort_values(by = date_column)
  booms = booms.reset_index(drop= True)

  return booms
