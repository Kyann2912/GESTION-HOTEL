import psycopg2

try:
    conn = psycopg2.connect(
        user="postgres",
        password="29122003",
        host="localhost",
        port="5432",
        database="Hotel"
    )
    cur = conn.cursor()

    # Afficher la version de PostgreSQL 
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("Version : ", version, "\n")
  
    # Créer la table Client
    # cur.execute("""
    #     CREATE TABLE IF NOT EXISTS Stock (
    #         Id_clt SERIAL PRIMARY KEY,
    #         Nom VARCHAR(255),
    #         Prix VARCHAR(255)
    #     );
    # """)
    
    # Committer les changements
    conn.commit()
  
    # Vérifier que la table a été créée
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    # tables = cur.fetchall()
    # print("Tables dans le schéma public:", tables)

    # Fermeture de la connexion à la base de données
    cur.close()
    conn.close()
    print("La connexion PostgreSQL est fermée")

except (Exception, psycopg2.Error) as error:
    print("Erreur lors de la connexion à PostgreSQL", error)
