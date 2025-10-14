import requests
from .db import SessionLocal, engine, Base
from .models import Cotacao
from .schema import MoedaSchema

Base.metadata.create_all(bind=engine)

def obter_cotacao() -> MoedaSchema:
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        dados = data['data'].values() 
        #Dicionários em Python têm métodos próprios para extrair suas partes. 
        # Existe um método para pegar as chaves (.keys()), um para pegar os pares de chave-valor (.items()), 
        # e um para pegar apenas os valores (.values()).
        dado_final = list(dados)
        return MoedaSchema(criptomoeda = dado_final[1], valor = dado_final[0], moeda = dado_final[2])
    else:
        return None

def add_cotacao(moeda_schema: MoedaSchema) -> Cotacao:
    with SessionLocal() as db:
        db_cotacao = Cotacao(criptomoeda=moeda_schema.criptomoeda, moeda=moeda_schema.moeda, valor=moeda_schema.valor)
        db.add(db_cotacao)
        db.commit()
        db.refresh(db_cotacao)
    return db_cotacao