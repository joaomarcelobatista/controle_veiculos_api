from pydantic import BaseModel
from typing import Optional, List
from model.veiculo import Veiculo


class ErrorSchema(BaseModel):
    """ Define como uma mensagem de eero será representada
    """
    message: str


class VeiculoSchema(BaseModel):
    """ Define deve ser representado como um novo veículo a ser inserido.
    """
    nome: str = "João da Silva"
    setor: Optional[str] = "Departamento de RH"
    placa: str = "KKK1234"


class VeiculoBuscaSchema(BaseModel):
    """ Define que a busca será feita com base na placa do veículo.
    """
    placa: str = "KKK1234"


class ListagemVeiculosSchema(BaseModel):
    """ Define como uma listagem de veículos será retornada.
    """
    veiculos:List[VeiculoSchema]


class VeiculoViewSchema(BaseModel):
    """ Define como um veículo será mostrado."""

    nome: str = "João da Silva"
    setor: Optional[str] = "Departamento de RH"
    placa: str = "KKK1234"
    

class VeiculoDeleteSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção."""
    
    message: str
    placa: str

def apresenta_veiculo(veiculo: Veiculo):
    """ Retorna uma representação do veiculo seguindo o schema definido em
        VeiculoViewSchema.
    """
    return {
        "nome": veiculo.nome,
        "setor": veiculo.setor,
        "placa": veiculo.placa,
        
    }

def apresenta_veiculos(veiculos: List[Veiculo]):
    """ Retorna uma representação do veículo seguindo o schema definido em
        VeiculoViewSchema.
    """
    result = []
    for veiculo in veiculos:
        result.append({
            "nome": veiculo.nome,
            "setor": veiculo.setor,
            "placa": veiculo.placa,
        })

    return {"veiculos": result}


