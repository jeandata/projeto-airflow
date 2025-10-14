from pydantic import BaseModel, ConfigDict


class MoedaSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    criptomoeda: str
    moeda: str
    valor: float