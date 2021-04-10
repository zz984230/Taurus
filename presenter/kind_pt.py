from presenter.dash_app import *
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from constants.colors import *
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


class KindPt(object):
    def __init__(self, base_layout, kind_pic_file):
        self.__base_layout = base_layout
        self.__kind_pic_file = kind_pic_file
        self.__half_left_width_stl = dict(width='50%', height="850px", float='left')
        self.__half_right_width_stl = dict(width='50%', float='right')

    def __set_layout(self):
        card_content = [
            dbc.CardHeader("Cafe Information"),
            dbc.CardBody(
                [
                    html.H5("耶加雪啡G1", className="card-title"),
                    dcc.Markdown('''
                    - 种植地：Yirgacheffe，Ethiopia
                    - 种植者：Aricha Kebele
                    - 品种：原始古老野生品种
                    - 海拔：1700-2100 meters
                    - 采收季：October-December
                    - 处理法：Natural
                    - 烘焙度：浅烘
                    '''),
                ]
            ),
        ]

        return dbc.Row(
            [
                dbc.Col([
                    dbc.Card(card_content, color=DARK_GRAY, inverse=True, style={"height": "50%"}),
                    dcc.Graph(id="kind_radar", style={"height": "50%"})
                ], style=self.__half_left_width_stl),
                dbc.Col([
                    html.Img(
                        src=self.__kind_pic_file,
                        style={"position": "absolute", "height": "100%"}
                    ),
                ], style=self.__half_right_width_stl),
            ],
            no_gutters=True,
            style={"height": "850px"}
        )

    def render(self, df):
        @app.callback(Output("right_layout", "children"),
                      Input("kind-collapse-0", "active"))
        def set_balance_layout(active):
            children = self.__set_layout()
            if active:
                return children

            return self.__base_layout.children

        @app.callback(Output("kind_radar", "figure"), Input("kind-collapse-0", "active"))
        def kind_radar_chart(active):
            fig = go.Figure(data=go.Scatterpolar(
                r=list(df['score']),
                theta=list(df['label']),
                fill='toself',
                opacity=0.8
            ))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True
                    ),
                ),
                showlegend=False,
                paper_bgcolor=DARK_GRAY
            )
            return fig
