from pydantic import BaseModel, ConfigDict
from typing import Optional
#les etudiants de base : ce qui est commun a la creation et a la lecture
class EtudiantsBase(BaseModel):
    nom:str
    prenom:str
    age:int
    sexe:str
    filiere:str
#le shema pour la creation (POST)
#il herite de EtudiantBase donc il contient tout ce qu il y a au dessus
class EtudiantsCreate(EtudiantsBase):
    pass
#pour modifier (tout est facultatif)
class EtudiantsUpdate(EtudiantsBase):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    age: Optional[int] = None
    sexe: Optional[str] = None
    filiere: Optional[str] = None
#le shema pour la reponse (ce que l'api renvoie)
class Etudiants(EtudiantsBase):
    id:int
    model_config = ConfigDict(from_attributes=True) #permet a pydantic de lire les objets SQLALchemy