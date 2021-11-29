import pandas as pd

df = pd.read_excel('RC_F01_01_2019_T26_11_2021.xlsx', 0, header=0, index_col=None, na_values=["NA"])

print('Import from database success!')

df['month'] = pd.DatetimeIndex(df['DT']).month
df['year'] = pd.DatetimeIndex(df['DT']).year
display(df)

import plotly.figure_factory as ff
import numpy as np

group_labels = ['2019', '2020', '3Q2021']

x1data = df.loc[df['year'] == 2019]
x2data = df.loc[df['year'] == 2020]
x3data = df.loc[df['year'] == 2021]

x1 = x1data['ruo']
x2 = x2data['ruo']
x3 = x3data['ruo']

rug_text_one = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

rug_text_two = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj',
                'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt',
                'uu', 'vv', 'ww', 'xx', 'yy', 'zz']

rug_text_three = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj',
                'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt',
                'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']

rug_text = [rug_text_one, rug_text_two, rug_text_three] # for hover in rug plot
colors = ['rgb(0, 0, 100)', 'rgb(0, 200, 200)', 'rgb(100, 0, 0)']

# Create distplot with custom bin_size
fig = ff.create_distplot(
    [x1, x2, x3], group_labels, bin_size=.2,
    rug_text=rug_text, colors=colors)

fig.update_layout(title_text='Customized Distplot')
fig.show()