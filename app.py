import Tracker
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


#lots of variables
# Set1pointsA = 0
# Set1pointsB = 0
# Set110%A = 0

# Set2pointsA = 0
# Set2pointsB = 0

# Set3pointsA = 0
# Set3pointsB = 0

# Set4pointsA = 0
# Set4pointsB = 0

# Set5pointsA = 0
# Set5pointsB = 0

#Tabcontent All
All = dbc.Card(
        dbc.CardBody
        ([
            dcc.Input(id="inputScore", type="number", 
                      placeholder=0, style={'marginRight':'10px'}),
            html.Div(id = "output1"),
        ])
    )#endCard

#Tabcontent set1
set1 = dbc.Card(
        dbc.CardBody
        ([
            html.P('points won: {1}'),
            html.P('predicted winning team: {A}'),
            html.P('scoring efficiency: {10%}'),
        ])
    )#endCard

set2 = dbc.Card(
        dbc.CardBody
        ([
            html.P('points won: 2'),
            html.P('predicted winning team: {A}'),
            html.P('scoring efficiency: {10%}'),
        ])
    )#endCard

set3 = dbc.Card(
        dbc.CardBody
        ([
            html.P('points won: 3'),
            html.P('predicted winning team: {A}'),
            html.P('scoring efficiency: {10%}'),
        ])
    )#endCard

set4 = dbc.Card(
        dbc.CardBody
        ([
            html.P('points won: 4'),
            html.P('predicted winning team: {A}'),
            html.P('scoring efficiency: {10%}'),
        ])
    )#endCard

set5 = dbc.Card(
        dbc.CardBody
        ([
            html.P('points won: 5'),
            html.P('predicted winning team: {A}'),
            html.P('scoring efficiency: {10%}'),
        ])
    )#endCard

app.layout = dbc.Container(
    [      
        dcc.ConfirmDialog(
        id='rules',
        message='Lorem ipsum',
        ),
        html.Br(),
        html.Img(src='assets/ball.png', 
                 style={'height':'5%', 'width':'5%'}, className = "center"),
        html.Br(),
        html.H1("Volleyball analysis app", style={'textAlign': 'center'}),
        html.Hr(),
        dbc.Button(
            "Basic volleyball rules",
            color="light",
            id="helpbutton",
            n_clicks = 0,
            className="className=d-grid gap-2 d-md-block mx-auto",
        ),
        html.Br(),
        dbc.Button(
            "Record",
            color="danger",
            id="recordbutton",
            n_clicks = 0,
            className="className=d-grid gap-2 d-md-block mx-auto",
        ),
        html.Span(id="HBoutput", style={"verticalAlign": "middle"}),
        dbc.Row([
            html.H4("Statistics"),
            dbc.Tabs
            (
                [
                    dbc.Tab(All, label="All", tab_id="All"),
                    dbc.Tab(set1, label="Set 1", tab_id="1"),
                    dbc.Tab(set2, label="Set 2", tab_id="2"),
                    dbc.Tab(set3, label="Set 3", tab_id="3"),
                    dbc.Tab(set4, label="Set 4", tab_id="4"),
                    dbc.Tab(set5, label="Set 5", tab_id="5"),
                ],
                id="tabs",
                active_tab="All",
            ),
            #html.Div(id="tab-content", className="p-4"),
            #html.P(f'points won: {pointsA}'),
            #html.P(f'predicted winning team: {A}'),
            #html.P(f'scoring efficiency: {10%}'),
        ])

    ]
)

@app.callback(
    Output("rules", "displayed"),
    [Input("helpbutton", "n_clicks")]
    )
    
def display_rules(click):
    if click:
        return True
    return False

    Output('HBoutput', 'children'),
    Input("helpButton", "n_clicks"),

@app.callback(
    Output("output1", "children"),
    [Input("inputScore", "value"),
      Input("recordbutton", "n_clicks")]
)
    
def update_output(inputScore, click):
    if click:
        click = False
        attacks = int(Tracker.track())
    else:
        attacks = 0
    if attacks == 0:
        scoringEfficienty = 0
    else:
        scoringEfficienty = int(inputScore / attacks * 100)
    #msg = html.Div('Attacks made: {}'.format(int(attacks)))
    msg = html.Div([
                    html.P(u'Points won: {}'.format(inputScore), 
                            style={'font-size': '25px'}),
                    html.P(f'Attacks made: {attacks}', 
                            style={'font-size': '25px'}),
                    html.P(f'Scoring effcienty: {scoringEfficienty}%',
                            style={'font-size': '25px'})
            ])
    return msg



def onClick(click):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    if click is None:
        return html.Div("nothing")
    else:
        return html.Div(f"Button is pressed {click} times")




if __name__ == "__main__":
    app.run_server()
