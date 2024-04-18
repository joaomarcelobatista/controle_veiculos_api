from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
from typing import Union


Base = declarative_base()

class Veiculo(Base):
    __tablename__ = 'veiculo'

    '''Um proprietário pode ter mais de um veículo cadastrado, mas um veículo somente
    pode ter um proprietário'''
    nome = Column(String(140))
    setor = Column(String(40))
    placa = Column(String(9), primary_key=True)
    data_insercao = Column(DateTime, default=datetime.now())

    
    def __init__(self, nome:str, setor:str, placa:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria o cadastro de um veículo

        Arguments:
            nome: nome do proprietário do veículo.
            setor: setor da empresa que proprietário do veículo trabalha.
            placa: placa do veículo.
            data_insercao: data em que o veículo foi inserido no sistema.
        """
        self.nome = nome
        self.setor = setor
        self.placa = placa

        if data_insercao:
            self.data_insercao = data_insercao
