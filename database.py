from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# définir l'URL de connexion à MariaDB
# mysql://utilisateur:mot_de_passe@hote:port/nom_de_la_base
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/bemtech"
# création du moteur SQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# créer une session locale pour effectuer des requêtes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# classe de base pour nos modèles SQLAlchemy
Base = declarative_base()
# dépendance pour récupérer la base de données dans nos routes FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
import os #pour lire le systeme
from dotenv import load_dotenv #pour charger les variables d'environnement
# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
#recuerer l url 
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL") 