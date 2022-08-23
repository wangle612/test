import streamlit as st
import numpy as np
import time
import pandas as pd


# markdown
st.markdown('Streamlit Demo Ceshi')

# 设置网页标题
st.title('一个傻瓜式构建可视化 web的 Python 神器 -- streamlit',anchor=None)

# 展示一级标题
st.header('1. 安装')

st.text('和安装其他包一样，安装 streamlit 非常简单，一条命令即可')
code1 = '''pip3 install streamlit'''
st.code(code1, language='bash')


# 展示一级标题
st.header('2. 使用')

# 展示二级标题
st.subheader('2.1 生成 Markdown 文档')

# 纯文本
st.text('导入 streamlit 后，就可以直接使用 st.markdown() 初始化')

# 展示代码，有高亮效果
code2 = '''import streamlit as st
st.markdown('Streamlit Demo')'''
st.code(code2, language='python')




progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")

st.latex('a=b/c')
st.caption('这有一支未来牌香烟ZheYeBuShi')

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('第%d列' % (i+1) for i in range(5))
)

st.table(df)
st.dataframe(df.style.highlight_max(axis=1))




col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "8%")
col3.metric("Humidity", "86%", '4%')



chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)
st.pyplot(chart_data)
st.bokeh_chart(chart_data)
st.altair_chart(chart_data)
st.altair_chart(chart_data)
st.vega_lite_chart(chart_data)
st.plotly_chart(chart_data)
st.pydeck_chart(chart_data)
st.graphviz_chart(chart_data)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)


