from sqlalchemy.orm import Session

from model.models import Desafiados


class DesafiadosRepository:
    @staticmethod
    def findAll(db: Session) -> list[Desafiados]:
        return db.query(Desafiados).all()

    @staticmethod
    def save(db: Session, desafiados: Desafiados) -> Desafiados:
        if desafiados.id:
            db.merge(desafiados)
        else:
            db.add(desafiados)
        db.commit()
        return desafiados

    @staticmethod
    def existsId(db: Session, id: int) -> bool:
        return db.query(Desafiados).filter(Desafiados.id == id).first() is not None

    @staticmethod
    def delete(db: Session, id: int) -> None:
        curso = db.query(Desafiados).filter(Desafiados.id == id).first()
        if curso is not None:
            db.delete(curso)
            db.commit()
