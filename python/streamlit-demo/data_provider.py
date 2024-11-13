import pandas as pd
from common import Query, QueryResponse

#pass chat  text to GPT to formulate response
def create_query(input_text:str):
    return {"start_date": "20231031", "metric": "VEGA", "filters": [{"filter_field": "Asset", "filter_value": "AAPL"}]}

def query_risk(query:Query, df:pd.DataFrame):
    query = create_query(query.prompt)
    filtered_df = df[df[query["filters"][0]["filter_field"]]==query["filters"][0]["filter_value"]]
    riskValue = filtered_df[filtered_df["Metric"]==query["metric"]]["RiskValue"].sum()
    return QueryResponse(content=f"Your Vega risk to AAPL is {riskValue}", source="RiskStore")
