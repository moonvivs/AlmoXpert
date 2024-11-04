from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session,relationship, declarative_base


engine = create_engine('sqlite:///almoxarifado.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Esmalte(Base):
    __tablename__ = 'esmalte'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False, index=True)
    marca = Column(String(40), nullable=False, index=True)
    quantidade = Column(Integer, nullable=False, index=True)

    # Representação classe
    def __repr__(self):
        return '<Nome: {} Marca: {} Quantidade: {}>'.format(self.nome, self.marca, self.quantidade)

    # função para salvar no banco

    def save(self):
        db_session.add(self)
        db_session.commit()

    # função para deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_esmalte = {
            'id_esmalte': self.id,
            'nome': self.nome,
            'marca': self.marca,
            'quantidade': self.quantidade
        }
        return dados_esmalte


class Funcionario(Base):
    __tablename__ = 'funcionario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, index=True)
    cpf = Column(String(11), nullable=False, index=True, unique=True)
    senha = Column(String(30), nullable=False, index=True)

    # Representação classe
    def __repr__(self):
        return '<Nome: {} CPF: {} Senha: {}>'.format(self.nome, self.cpf, self.senha)

    # função para salvar no banco

    def save(self):
        db_session.add(self)
        db_session.commit()

    # função para deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_funcionario = {
            'id_funcionario': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'senha': self.senha
        }
        return dados_funcionario


class Entrega(Base):
    __tablename__ = 'entrega'
    id = Column(Integer, primary_key=True)
    nome_esmalte = Column(String(50), nullable=False, index=True)

    esmalte_id = Column(Integer, ForeignKey('esmalte.id'))
    esmalte = relationship("Esmalte")

    # Representação classe
    def __repr__(self):
        return '<Nome do Esmalte: {} >'.format(self.nome_esmalte)

    # função para salvar no banco

    def save(self):
        db_session.add(self)
        db_session.commit()

    # função para deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_entrega = {
            'id_entrega': self.id,
            'nome_esmalte': self.nome_esmalte
        }
        return dados_entrega


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
