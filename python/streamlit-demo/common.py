from dataclasses import dataclass
import pandas as pd

@dataclass
class Query:
    prompt: str

@dataclass
class QueryResponse:
    content:str
    source:str = None
    df:pd.DataFrame = None

    def create_response(self):
        return {"content":self.content,"source":self.source}