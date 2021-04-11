from presenter.dash_app import *
from constants.colors import *
from constants.constant import *
from dash.dependencies import Input, Output
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


class GlobalPt(object):
    def __init__(self, logo_file, bg_file, kind_pt, score_pt):
        self.__logo_file = logo_file
        self.__bg_file = bg_file
        self.__kind_pt = kind_pt
        self.__score_pt = score_pt
        self.__labels = ['咖啡品类', '咖啡品鉴', '咖啡评分']
        self.__clicked_button_id = ""
        self.__button_group = []

    def __init_layout(self):
        self.__left_layout = dbc.Col(id='left_layout', xs=1, style=dict(background=GAINSBORO, height=PAGE_HEIGHT))
        self.__right_layout = dbc.Col(
            html.Img(
                src=self.__bg_file,
                style={"height": "100%", "width": "100%"}
            ),
            id='right_layout',
            style=dict(background=SILVER, height=PAGE_HEIGHT)
        )

    def set_global_layout(self):
        self.__init_layout()
        add_layout(html.Div(
            children=[
                dbc.Row(
                    dbc.Navbar(
                        [
                            dbc.Col(html.Img(src=self.__logo_file, height="40px")),
                            dbc.Col(dbc.NavbarBrand("Taurus")),
                            dbc.Col()
                        ],
                        color=LIMBO_BLACK,
                        dark=True,
                    ),
                    style=dict(background=LIMBO_BLACK)
                ),
                dbc.Row(
                    [
                        self.__left_layout,
                        self.__right_layout,
                    ],
                    no_gutters=True,
                    style=dict(height=PAGE_HEIGHT)
                )
            ],
        ))

        return self

    def __set_each_left_layout(self, i, button_group):
        return dbc.Row(
            [
                dbc.Button(self.__labels[i], id=f"collapse-button-{i}", color="dark", outline=True, block=True,
                           style={"border-style": "none"}),
                dbc.Collapse(button_group, id=f"collapse-{i}", style={"width": "100%"})
            ]
        )

    def set_left_layout(self):
        self.__button_group = [
            [
                dbc.Button("Yirgacheffe", id="kind-collapse-0", block=True),
            ],
            [
                dbc.Button("Yirgacheffe", id="tastes-collapse-0", block=True),
            ],
            [
                dbc.Button("Yirgacheffe", id="score-collapse-0", block=True),
            ]
        ]

        self.__left_layout.children = [
            self.__set_each_left_layout(i, dbc.ButtonGroup(
                self.__button_group[i],
                vertical=True,
                style={"width": "inherit"}
            )) for i in range(len(self.__labels))
        ]
        return self

    def get_left_div(self):
        return self.__left_layout

    def get_right_div(self):
        return self.__right_layout

    def render(self):
        @app.callback(Output("right_layout", "children"),
                      [Input("kind-collapse-0", "active"), Input("score-collapse-0", "active")])
        def set_score_layout(kind_active, score_active):
            ctx = dash.callback_context
            if not ctx.triggered:
                return self.__right_layout.children
            else:
                button_id = ctx.triggered[0]["prop_id"].split(".")[0]

            if kind_active and button_id == "kind-collapse-0":
                return self.__kind_pt.set_layout()
            elif score_active and button_id == "score-collapse-0":
                return self.__score_pt.set_layout()

            return self.__right_layout.children

        @app.callback([Output(f"score-collapse-{i}", "active") for i in range(len(self.__button_group[2]))],
                      [Input(f"score-collapse-{i}", "n_clicks") for i in range(len(self.__button_group[2]))])
        def score_button_click(*args):
            ctx = dash.callback_context
            if not ctx.triggered:
                return [False for _ in range(len(args))]
            else:
                button_id = ctx.triggered[0]["prop_id"].split(".")[0]

            index = 0
            for k, v in enumerate(args):
                if v and button_id == f"score-collapse-{k}":
                    index = k

            return [True if index == i else False for i in range(len(args))]

        @app.callback([Output(f"kind-collapse-{i}", "active") for i in range(len(self.__button_group[0]))],
                      [Input(f"kind-collapse-{i}", "n_clicks") for i in range(len(self.__button_group[0]))])
        def kind_button_click(*args):
            ctx = dash.callback_context
            if not ctx.triggered:
                return [False for _ in range(len(args))]
            else:
                button_id = ctx.triggered[0]["prop_id"].split(".")[0]

            index = 0
            for k, v in enumerate(args):
                if v and button_id == f"kind-collapse-{k}":
                    index = k

            return [True if index == i else False for i in range(len(args))]

        @app.callback([Output(f"collapse-button-{i}", "active") for i in range(len(self.__labels))],
                      [Input(f"collapse-button-{i}", "n_clicks") for i in range(len(self.__labels))])
        def click(*args):
            ctx = dash.callback_context
            if not ctx.triggered:
                return [False for _ in range(len(args))]
            else:
                button_id = ctx.triggered[0]["prop_id"].split(".")[0]

            index = 0
            for k, v in enumerate(args):
                if v and button_id == f"collapse-button-{k}":
                    index = k

            return [True if index == i else False for i in range(len(args))]

        @app.callback([Output(f"collapse-{i}", "is_open") for i in range(len(self.__labels))],
                      [Input(f"collapse-button-{i}", "n_clicks") for i in range(len(self.__labels))])
        def collapse(*args):
            ctx = dash.callback_context
            if not ctx.triggered:
                return [False for _ in range(len(args))]
            else:
                button_id = ctx.triggered[0]["prop_id"].split(".")[0]

            index = 0
            for k, v in enumerate(args):
                if v and button_id == f"collapse-button-{k}":
                    index = k

            return [True if index == i else False for i in range(len(args))]

        return self
