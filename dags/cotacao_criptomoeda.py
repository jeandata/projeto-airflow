from include.controller import obter_cotacao, add_cotacao
from airflow.sdk import  dag, task
from datetime import datetime


# Define the basic parameters of the DAG, like schedule and start_date
@dag(
    dag_id="cotacao_criptomoedas",
    description="ETL para extração e tratamento dos valores de criptomoedas",
    start_date=datetime(2025, 10, 14),
    schedule="* * * * *",
    catchup=False )

def main():

    @task
    def extrair_criptomoeda():
        moeda_schema = obter_cotacao()
        if moeda_schema:
            print(f"Adicionando a nova cotação da criptomoeda:{moeda_schema.criptomoeda} ao banco de dados")
        else:
            print(f"Não foi possível adicionar a nova cotação")
        return moeda_schema
    
    @task
    def carregar_no_banco(schema):
        add_cotacao(schema)

    t1 = extrair_criptomoeda()
    t2 = carregar_no_banco(t1)

    t1 >> t2

main()