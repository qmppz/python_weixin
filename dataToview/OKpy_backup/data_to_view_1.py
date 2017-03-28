# -*- coding:utf-8 -*-


import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline
from plotly.graph_objs import *
# Generate the figure
import plotly.plotly as py
import plotly.graph_objs as go

list_articalClssfy= ['热门', '推荐',  '段子手','养身堂','私房话',\
					'八卦精','爱生活','财经迷','汽车迷','科技咖',\
					'潮人帮','辣妈帮','点赞党','旅行家','职场人',\
					'美食家','古今通','学霸族','星座控','体育迷']
list_articalNum   = [904,854,842,907,639,\
					1041,676,966,773,1011,\
					1005,850,720,624,540,\
					720,729,586,377,903]
# frequency >= 5
list_articalWordsNum=[1584,1645,1182,1810,1006,\
					1877,1241,1983,1525,1957,\
					1708,1477,1180,1169,1086,\
					1358,1347,1261,627,1751]

trace_articalNum = go.Bar(
    x=list_articalClssfy,
    y=list_articalNum,
    name='爬取文章数'
)
trace__articalWordsNum = go.Bar(
    x=list_articalClssfy,
    y=list_articalWordsNum,
    name='文章分词数'
)

data = [trace_articalNum, trace__articalWordsNum]
layout = go.Layout(
    barmode='stack',
    title="data_to_view_1 爬取文章数量与分词数量(frequency>=5)"
)

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename = 'view_html/data_to_view_1.html')

#py.iplot(fig, filename='grouped-bar')