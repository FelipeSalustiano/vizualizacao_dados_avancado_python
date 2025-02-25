import plotly.express as px
import pandas as pd 
from dash import Dash, html, dcc

df = pd.read_csv('clientes-v3-preparado.csv')

def  cria_graficos(df):
    # Histograma 
    fig1 = px.histogram(df, x='salario', nbins=30, title='Distribuição de salário')

    # Gráfico pizza 
    fig2 = px.pie(df, names='area_atuacao', color='area_atuacao', hole=0.2, color_discrete_sequence=px.colors.sequential.RdBu)

    # Gráfico bolha 
    fig3 = px.scatter(df, x='idade', y='salario', size='anos_experiencia', color='area_atuacao', hover_name='estado', size_max=60)
    fig3.update_layout(title='Salário po Idade e Anos de Experiência')

    # Gráfico de linha 
    fig4 = px.line(df, x='idade', y='salario', color='area_atuacao', facet_col='nivel_atuacao')
    fig4.update_layout(
        title='Salário por Idade e Área de Atuação para cada nível de Educação',
        xaxis_title='Idade',
        yaxis_title='Salário'   
    )

    # Gráfico 3D
    fig5 = px.scatter_3d(df, x='estado_civil', y='salario', z='anos_experiencia', color='nivel_educacao')

    # Gráfico de barra
    fig6 = px.bar(df, x='idade', y='salario', color='nivel_atuacao', barmode='group', color_discrete_sequence=px.colors.qualitative)
    fig6.update_layout(
        title='Salário por Estado Civil e Nível de Educação',
        xaxis_title='Idade',
        yaxis_title='Saláro',
        legend_title='Nível de Educação',
        plot_bgcolor='rgba(222, 255, 253, 1)',
        paper_bgcolor='rgba(186, 245, 241, 1)'
    )
    return fig1, fig2, fig3, fig4, fig5, fig6


def cria_app(df):
    # Criando App
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6 = cria_graficos(df)
    
    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
        
    ])
    return app

df = pd.read_csv('clientes-v3-preparado.csv')

if __name__ == '__main__':
    app = cria_app(df)
    # Executa App
    app.run_server(debug=True, port=8050)