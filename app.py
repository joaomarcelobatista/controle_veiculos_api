from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Veiculo
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API do SisVeiculos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definição das tags de documentação do código:
home_tag = Tag(name="Documentação", description="Apresentação da documentação em Swagger")
veiculo_tag = Tag(name="Veículo", description="Adição, visualização e remoção de veículos de funcionários autorizados a utilizar o estacionamento particular da empresa")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para o início, para o usuário acessar a documentação."""
    return redirect('/openapi/swagger')


@app.post('/veiculo', tags=[veiculo_tag],
          responses={"200": VeiculoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_veiculo(form: VeiculoSchema):
    """Adiciona um novo veiculo ao cadastro geral.

    Retorna uma representação do veículo cadastrado.
    """
    veiculo = Veiculo(
        nome=form.nome,
        setor=form.setor,
        placa=form.placa)
    logger.debug(f"Adicionando veículo de nome: '{veiculo.nome}'")
    try:
        session = Session()
        session.add(veiculo)
        session.commit()
        logger.debug(f"Adicionado veículo de nome: '{veiculo.nome}'")
        return apresenta_veiculo(veiculo), 200

    except IntegrityError as e:
        error_msg = "Veículo de mesma placa já salvo no sistema"
        logger.warning(f"Erro ao adicionar veiculo '{veiculo.nome}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item"
        logger.warning(f"Erro ao adicionar veículo '{veiculo.nome}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/veiculos', tags=[veiculo_tag],
         responses={"200": ListagemVeiculosSchema, "404": ErrorSchema})
def get_veiculos():
    """Faz a busca por todos os veículos cadastrados na base de dados.

    Retorna uma representação da listagem de todos os veículos.
    """
    logger.debug(f"Coletando veículos ")
    session = Session()
    veiculos = session.query(Veiculo).all()
    print(veiculos)

    if not veiculos:
        return {"veiculos": []}, 200
    else:
        logger.debug(f"%d veiculos encontrados" % len(veiculos))
        print(veiculos)
        return apresenta_veiculos(veiculos), 200


@app.get('/veiculo', tags=[veiculo_tag],
         responses={"200": VeiculoViewSchema, "404": ErrorSchema})
def get_veiculo(query: VeiculoBuscaSchema):
    """Faz a busca por um veículo a partir da placa.

    Retorna uma representação dos veículos.
    """
    placa_veiculo = query.placa
    logger.debug(f"Coletando dados sobre veículo #{placa_veiculo}")
    session = Session()
    veiculo = session.query(Veiculo).filter(Veiculo.placa == placa_veiculo).first()

    if not veiculo:
        error_msg = "Veículo não encontrado no cadastro"
        logger.warning(f"Erro ao buscar veículo '{placa_veiculo}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Veículo econtrado: '{veiculo.nome}'")
        return apresenta_veiculo(veiculo), 200


@app.delete('/veiculo', tags=[veiculo_tag],
            responses={"200": VeiculoDeleteSchema, "404": ErrorSchema})
def del_veiculo(query: VeiculoBuscaSchema):
    """Deleta o cadastro de um Veículo a partir da placa informada. Utilizar esta funcionalidade quando o funcionário for desligado da empresa.

    Retorna uma mensagem de confirmação da remoção e informando a placa removida.
    """
    veiculo_placa = unquote(unquote(query.placa))
    logger.debug(f"Deletando dados sobre o veículo de placa #{veiculo_placa}")
    session = Session()
    count = session.query(Veiculo).filter(Veiculo.placa == veiculo_placa).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado veículo de placa #{veiculo_placa}")
        return {"message": "Veículo removido", "placa": veiculo_placa}
    else:
        error_msg = "Veículo não encontrado na base de dados..."
        logger.warning(f"Erro ao deletar veículo #'{veiculo_placa}', {error_msg}")
        return {"message": error_msg}, 404