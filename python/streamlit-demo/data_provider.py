import pandas as pd

#pass chat  text to GPT to formulate response
def create_query(input_text:str):
    return {"start_date": "20231031", "metric": "VEGA", "filters": [{"filter_field": "Asset", "filter_value": "AAPL"}]}

def query_risk(input_text:str, df:pd.DataFrame):
    query = create_query(input_text)
    filtered_df = df[df[query["filters"][0]["filter_field"]]==query["filters"][0]["filter_value"]]
    riskValue = filtered_df[filtered_df["Metric"]==query["metric"]]["RiskValue"].sum()
    return {"content":f"Your Vega risk to AAPL is {riskValue}","source":"RiskStore"}
