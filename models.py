from sqlalchemy import Column, Integer, String
from database import Base
# on definis notre classe qui va correspondre
# a notre table etudiant dans la base de donnees
class etudiants(Base):
    #le nom exact dans mysql
    __tablename__ = "etudiant"
    #on va definir les colonnes de notre table etudiant
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(20), nullable=False)
    prenom = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    sexe = Column(String(10), nullable=False)
    filiere = Column(String(30), nullable=False)