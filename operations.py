from sqlalchemy.orm import Session
import models, schemas
#Recuperer un etudiant par son id
def get_etudiant(db: Session, etudiant_id: int):
    #"""Recuperer un etudiant par son id"""
    return db.query(models.etudiants).filter(models.etudiants.id == etudiant_id).first()
#Recuperer tous les etudiants
#def get_etudiants(db: Session)
#return db.query(models.Etudiants).all()
#recuperer tous les etudiants sans  surcharger le serveur 
# cette fois ci en limitant le nombre d etudiants a afficher
def get_etudiants_all_limit(db: Session, skip: int = 0, limit: int = 10):
    #on retourne une liste d étudiants avec une limite pour ne pas surcharger le serveur
    return db.query(models.etudiants).offset(skip).limit(limit).all() 
#4 creer un nouvel etudiant
def create_etudiant(db: Session, etudiant: schemas.EtudiantsCreate):
    #on transforme le shema pydantic en un objet SQLAlchemy
    db_etudiant = models.etudiants(
        nom=etudiant.nom,
        prenom=etudiant.prenom,
        age=etudiant.age,
        sexe=etudiant.sexe,
        filiere=etudiant.filiere
    )
    db.add(db_etudiant) #on ajoute l etudiant a la session
    db.commit() #on valide la transaction pour enregistrer l etudiant dans la base de donnees
    db.refresh(db_etudiant) #on rafraichit l objet pour recuperer son id genere par la base de donnees
    return db_etudiant
#supp un etudiant
def delete_etudiant(db: Session, etudiant_id: int):
    #on cherche dabord si l etudiant existe dans la base de donnees
    db_etudiant = db.query(models.etudiants).filter(models.etudiants.id == etudiant_id).first()
    if db_etudiant:
        #si on la trouve on demande sa suppression
        db.delete(db_etudiant)
        #on valide laction dans mariadb our que ca soit permanent
        db.commit()
        #on confirme que la suppression a reussi en essayant de recuperer a nouveau l etudiant
        return True
    return False #on signale que l etudiant n a pas ete trouve pour la suppression il existe pas