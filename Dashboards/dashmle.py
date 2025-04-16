#install dash by 'pip install dash' before running this code
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from processing_function  import gcbp
df = pd.read_csv("machine_learning_engineers.csv")  

# Thay đổi giá trị cột cho dễ đọc 
df['Q3'] = df['Q3'].replace({
    'United States of America': 'USA',
    'United Kingdom of Great Britain and Northern Ireland': 'UK',
    'Iran, Islamic Republic of...': 'Iran',
    'Republic of Korea': 'South Korea',
    'United Arab Emirates': 'UAE'
})

df['Q4'] = df['Q4'].replace({
    'Doctoral degree': 'PhD',
    'Master’s degree': 'Master',
    'Bachelor’s degree': 'Bachelor',
    'I prefer not to answer': 'No answer',
    'Some college/university study without earning a bachelor’s degree': 'Some college',
    'No formal education past high school': 'High school',
    'Professional degree': 'Professional'
})

# Tạo ứng dụng Dash
app = dash.Dash(__name__)

# Tạo biểu đồ phân bố quốc gia (Q3)
country_count = df['Q3'].value_counts().reset_index()
country_count.columns = ['Country', 'Count']
fig1 = px.bar(country_count, x='Country', y='Count', labels={'index': 'Country', 'Q3': 'Number of Engineers'},
              title="Distribution of ML Engineers by Country")
degree_counts_1= df['Q4'].value_counts().reset_index()

# Biểu đồ phân bố trình độ học vấn (Q4)
degree_counts = df['Q4'].value_counts().reset_index()
degree_counts.columns = ['Education Level', 'Count']
fig2 = px.bar(degree_counts, x='Education Level', y='Count', labels={'index': 'Education Level', 'Q4': 'Number of Engineers'},
              title="Distribution of ML Engineers by Education Level")

# Biểu đồ ngôn ngữ lập trình phổ biến (Q7)
q7_cleaned = gcbp(df, 'Q7')
lang_counts = pd.DataFrame({
    'Programming Language': q7_cleaned,
    'Count': [df[lang].sum() for lang in q7_cleaned]
})
fig3 = px.bar(lang_counts, x='Programming Language', y='Count', labels={'Programming Language': 'Programming Language', 'Count': 'Number of Users'},
              title="Most Common Programming Languages Used by ML Engineers")

# Biểu đồ các framework ML phổ biến (Q16)
q16_cleaned = gcbp(df, 'Q16')
frame_counts = pd.DataFrame({
    'Framework_ML': q16_cleaned,
    'Count': [df[framework].sum() for framework in q16_cleaned]
})
fig4 = px.bar(frame_counts, x='Framework_ML', y='Count', labels={'Framework_ML': 'Framework/ML Tool', 'Count': 'Number of Users'},
              title="Most Common Frameworks/ML Tools Used by ML Engineers")

# Biểu đồ mức lương của kỹ sư ML (Q24)
salary_counts = df['Q24'].value_counts().reset_index()
salary_counts.columns = ['Salary Range', 'Count']
fig5 = px.bar(salary_counts, x='Salary Range', y='Count', labels={'Salary Range': 'Salary Range', 'Count': 'Number of Engineers'},
              title="ML Engineers Salary Distribution")
# Dashboard layout
app.layout = html.Div([
    html.H1("Machine Learning Engineers Dashboard", style={'text-align': 'center'}),
    
    html.Div([
        html.Div([dcc.Graph(figure=fig1)], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(figure=fig2)], style={'width': '48%', 'display': 'inline-block'})
    ], style={'padding': '10px'}),
    
    html.Div([
        html.Div([dcc.Graph(figure=fig3)], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(figure=fig4)], style={'width': '48%', 'display': 'inline-block'})
    ], style={'padding': '10px'}),
    
    html.Div([dcc.Graph(figure=fig5)], style={'width': '100%', 'display': 'inline-block'})
])

# Chạy ứng dụng
if __name__ == '__main__':
    app.run()
