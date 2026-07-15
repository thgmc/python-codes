import requests
import polars as pl


def get_json_serie() -> pl.DataFrame | None:
    codigo_Serie = 4391
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_Serie}/dados/ultimos/10?formato=json"
    response = requests.get(url)
    if response.status_code == 200:
        return pl.DataFrame(response.json())
    else:
        return None