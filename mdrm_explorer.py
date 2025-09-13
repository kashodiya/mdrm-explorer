
import pandas as pd
import dash
from dash import dcc, html, Input, Output, State, dash_table
import plotly.express as px
import plotly.graph_objects as go

# Read the CSV file with proper encoding
# Skip the first row which contains "PUBLIC"
print("Loading MDRM data...")
df = pd.read_csv('/workspace/MDRM_CSV.csv', skiprows=1, encoding='utf-8')
print(f"Loaded {len(df)} rows of data")

# Initialize the Dash app
app = dash.Dash(__name__, title="MDRM Explorer")

# Define the layout
app.layout = html.Div([
    html.H1("Micro Data Reference Manual (MDRM) Explorer"),
    
    html.Div([
        html.Div([
            html.H3("About MDRM"),
            html.P("""
                The Micro Data Reference Manual (MDRM) is a catalog of micro and macro data collected from 
                depository institutions and other respondents. The data are organized into reports, or data series, 
                and consist primarily of financial and structure data.
            """),
            html.P("""
                Each data series has a four-letter mnemonic for data transmission and storage. Each variable 
                within a data series is assigned a number (usually 4 digits). The combination (e.g., SVGL2170) 
                references a specific data item on a specific series.
            """),
        ], style={'width': '100%', 'marginBottom': '20px'}),
        
        html.Div([
            html.H3("Search and Filter"),
            html.Div([
                html.Div([
                    html.Label("Mnemonic:"),
                    dcc.Dropdown(
                        id='mnemonic-dropdown',
                        options=[{'label': m, 'value': m} for m in sorted(df['Mnemonic'].unique())],
                        placeholder="Select a mnemonic",
                    ),
                ], style={'width': '30%', 'display': 'inline-block', 'marginRight': '10px'}),
                
                html.Div([
                    html.Label("Item Code:"),
                    dcc.Input(
                        id='item-code-input',
                        type='text',
                        placeholder="Enter item code",
                    ),
                ], style={'width': '30%', 'display': 'inline-block', 'marginRight': '10px'}),
                
                html.Div([
                    html.Label("Item Type:"),
                    dcc.Dropdown(
                        id='item-type-dropdown',
                        options=[
                            {'label': 'Financial/reported (F)', 'value': 'F'},
                            {'label': 'Derived (D)', 'value': 'D'},
                            {'label': 'Percentage (P)', 'value': 'P'},
                            {'label': 'Rate (R)', 'value': 'R'},
                            {'label': 'Structure (S)', 'value': 'S'},
                            {'label': 'Projected (J)', 'value': 'J'},
                        ],
                        placeholder="Select item type",
                    ),
                ], style={'width': '30%', 'display': 'inline-block'}),
            ], style={'marginBottom': '10px'}),
            
            html.Div([
                html.Label("Reporting Form:"),
                dcc.Dropdown(
                    id='reporting-form-dropdown',
                    options=[{'label': rf, 'value': rf} for rf in sorted(df['Reporting Form'].dropna().unique())],
                    placeholder="Select a reporting form",
                ),
            ], style={'marginBottom': '10px'}),
            
            html.Div([
                html.Label("Confidentiality:"),
                dcc.RadioItems(
                    id='confidentiality-radio',
                    options=[
                        {'label': 'All', 'value': 'all'},
                        {'label': 'Public (N)', 'value': 'N'},
                        {'label': 'Confidential (Y)', 'value': 'Y'},
                    ],
                    value='all',
                    inline=True
                ),
            ], style={'marginBottom': '10px'}),
            
            html.Button('Search', id='search-button', n_clicks=0, style={'marginTop': '10px'}),
            html.Button('Reset', id='reset-button', n_clicks=0, style={'marginTop': '10px', 'marginLeft': '10px'}),
        ], style={'width': '100%', 'marginBottom': '20px'}),
        
        html.Div([
            html.H3("Results"),
            html.Div(id='results-count'),
            dash_table.DataTable(
                id='results-table',
                columns=[
                    {'name': 'Mnemonic', 'id': 'Mnemonic'},
                    {'name': 'Item Code', 'id': 'Item Code'},
                    {'name': 'Item Name', 'id': 'Item Name'},
                    {'name': 'Item Type', 'id': 'ItemType'},
                    {'name': 'Reporting Form', 'id': 'Reporting Form'},
                    {'name': 'Confidentiality', 'id': 'Confidentiality'},
                    {'name': 'Start Date', 'id': 'Start Date'},
                    {'name': 'End Date', 'id': 'End Date'},
                ],
                page_size=10,
                style_table={'overflowX': 'auto'},
                style_cell={
                    'textAlign': 'left',
                    'padding': '5px',
                    'whiteSpace': 'normal',
                    'height': 'auto',
                },
                style_header={
                    'backgroundColor': 'lightgrey',
                    'fontWeight': 'bold'
                },
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(248, 248, 248)'
                    }
                ],
                filter_action="native",
                sort_action="native",
            ),
        ], style={'width': '100%', 'marginBottom': '20px'}),
        
        html.Div([
            html.H3("Item Details"),
            html.Div(id='item-details', style={'whiteSpace': 'pre-wrap', 'border': '1px solid #ddd', 'padding': '10px', 'backgroundColor': '#f9f9f9'})
        ], style={'width': '100%'}),
        
        html.Div([
            html.H3("Statistics"),
            dcc.Tabs([
                dcc.Tab(label="Mnemonics Distribution", children=[
                    dcc.Graph(id='mnemonics-chart')
                ]),
                dcc.Tab(label="Item Types Distribution", children=[
                    dcc.Graph(id='item-types-chart')
                ]),
                dcc.Tab(label="Confidentiality Distribution", children=[
                    dcc.Graph(id='confidentiality-chart')
                ]),
            ])
        ], style={'width': '100%', 'marginTop': '20px'}),
    ], style={'margin': '0 auto', 'maxWidth': '1200px', 'padding': '20px'})
])

# Define callbacks
@app.callback(
    [Output('results-table', 'data'),
     Output('results-count', 'children'),
     Output('mnemonics-chart', 'figure'),
     Output('item-types-chart', 'figure'),
     Output('confidentiality-chart', 'figure')],
    [Input('search-button', 'n_clicks'),
     Input('reset-button', 'n_clicks')],
    [State('mnemonic-dropdown', 'value'),
     State('item-code-input', 'value'),
     State('item-type-dropdown', 'value'),
     State('reporting-form-dropdown', 'value'),
     State('confidentiality-radio', 'value')]
)
def update_results(search_clicks, reset_clicks, mnemonic, item_code, item_type, reporting_form, confidentiality):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'reset-button':
        filtered_df = df.head(10)  # Just show first 10 rows on reset
        count_text = f"Showing first 10 rows (total dataset: {len(df)} rows)"
    else:
        # Apply filters
        filtered_df = df.copy()
        
        if mnemonic:
            filtered_df = filtered_df[filtered_df['Mnemonic'] == mnemonic]
        
        if item_code:
            filtered_df = filtered_df[filtered_df['Item Code'].str.contains(item_code, na=False, case=False)]
        
        if item_type:
            filtered_df = filtered_df[filtered_df['ItemType'] == item_type]
        
        if reporting_form:
            filtered_df = filtered_df[filtered_df['Reporting Form'] == reporting_form]
        
        if confidentiality != 'all':
            filtered_df = filtered_df[filtered_df['Confidentiality'] == confidentiality]
        
        # Limit to 1000 rows for performance
        if len(filtered_df) > 1000:
            count_text = f"Found {len(filtered_df)} rows (showing first 1000)"
            filtered_df = filtered_df.head(1000)
        else:
            count_text = f"Found {len(filtered_df)} rows"
    
    # Create charts
    # Mnemonics chart
    top_mnemonics = df['Mnemonic'].value_counts().head(10)
    mnemonics_fig = px.bar(
        x=top_mnemonics.index, 
        y=top_mnemonics.values,
        labels={'x': 'Mnemonic', 'y': 'Count'},
        title='Top 10 Most Common Mnemonics'
    )
    
    # Item Types chart
    item_types = df['ItemType'].value_counts()
    item_types_fig = px.pie(
        values=item_types.values, 
        names=item_types.index,
        title='Distribution of Item Types'
    )
    
    # Confidentiality chart
    conf = df['Confidentiality'].value_counts()
    conf_fig = px.pie(
        values=conf.values, 
        names=conf.index,
        title='Distribution of Confidentiality',
        color_discrete_map={'Y': 'red', 'N': 'green', 'n': 'yellow'}
    )
    
    return filtered_df.to_dict('records'), count_text, mnemonics_fig, item_types_fig, conf_fig

@app.callback(
    Output('item-details', 'children'),
    [Input('results-table', 'active_cell')],
    [State('results-table', 'data')]
)
def display_item_details(active_cell, data):
    if active_cell and data:
        row = data[active_cell['row']]
        mnemonic = row['Mnemonic']
        item_code = row['Item Code']
        
        # Get the full row from the original dataframe
        item_data = df[(df['Mnemonic'] == mnemonic) & (df['Item Code'] == item_code)]
        
        if not item_data.empty:
            item = item_data.iloc[0]
            details = f"""
MDRM Identifier: {item['Mnemonic']}{item['Item Code']}
Item Name: {item['Item Name']}
Reporting Form: {item['Reporting Form']}
Item Type: {item['ItemType']}
Confidentiality: {item['Confidentiality']}
Start Date: {item['Start Date']}
End Date: {item['End Date']}

Description:
{item['Description']}

Series Glossary:
{item['SeriesGlossary']}
            """
            return details
    
    return "Select a row from the results table to view details"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=56085)
