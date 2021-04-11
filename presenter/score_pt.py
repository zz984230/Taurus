from presenter.dash_app import *
from dash.dependencies import Input, Output
import dash_core_components as dcc
from constants.constant import *
from constants.colors import *
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px


class ScorePt(object):
    def __init__(self):
        self.__half_left_width_stl = {"width": '50%', "float": "left"}
        self.__half_right_width_stl = {"width": '50%', "float": "right"}

    def set_layout(self):
        return dbc.Row(
            [
                dbc.Col([
                    dcc.Graph(id="score_radar")
                ], style=self.__half_left_width_stl),
                dbc.Col([
                    dcc.Graph(id="score_bar")
                ], style=self.__half_right_width_stl),
            ],
            style={"height": PAGE_HEIGHT}
        )

    def render(self, df, cols):
        @app.callback(Output("score_bar", "figure"), Input("score-collapse-0", "active"))
        def score_bar_chart(active):
            fig = px.bar(df, x=SCORELLER, y=FINAL_SCORE, color=SCORELLER)
            return fig

        @app.callback(Output("score_radar", "figure"), Input("score-collapse-0", "active"))
        def score_radar_chart(active):
            flavors = cols[1:-1]
            fig = go.Figure()
            [fig.add_trace(go.Scatterpolar(
                r=df[flavors][df[SCORELLER] == scoreller].values.tolist()[0],
                theta=flavors,
                fill='toself',
                opacity=0.8,
                name=scoreller,
            )) for scoreller in df[SCORELLER]]

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True
                    ),
                ),
                showlegend=True,
                paper_bgcolor=WHITE_SMOKE,
            )
            return fig
