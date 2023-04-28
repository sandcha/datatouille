from pandas import read_csv


# https://www.data.gouv.fr/fr/datasets/repertoire-national-des-elus-1
PATH_RNE_CONSEILLERS_MUNICIPAUX="./rne-cm-20221216.csv"

conseillers_municipaux=read_csv(
    PATH_RNE_CONSEILLERS_MUNICIPAUX,
    dtype={
        "Code du département": str,
        "Libellé du département": str,
        "Code de la collectivité à statut particulier": str,
        "Libellé de la collectivité à statut particulier": str,
        "Code de la commune": str,
        "Libellé de la commune": str,
        "Nom de l'élu": str,
        "Prénom de l'élu": str,
        "Code sexe": str,
        "Date de naissance": str,
        "Code de la catégorie socio-professionnelle": str,
        "Libellé de la catégorie socio-professionnelle": str,
        "Date de début du mandat": str,
        "Libellé de la fonction": str,
        "Date de début de la fonction": str,
        "Code nationalité": str
    },
    encoding="utf-8",
    sep='\t'
    )

print(conseillers_municipaux.head())
print(conseillers_municipaux.columns)
print(conseillers_municipaux["Code du département"])

CODE_INSEE_CAYENNE="97302"
LIBELLE_CAYENNE="Cayenne"
filtre_cayenne=conseillers_municipaux["Libellé de la commune"] == LIBELLE_CAYENNE
conseillers_municipaux_cayenne=conseillers_municipaux[filtre_cayenne][
        [
            "Code de la commune",
            # "Libellé de la commune",
            "Nom de l'élu",
            "Prénom de l'élu",
            "Libellé de la fonction",
            "Date de début de la fonction"
            ]
        ].copy()

print(conseillers_municipaux_cayenne)


# http://www.ville-cayenne.fr/vos-elus-du-conseil-municipal/
conseillers_municipaux_site_ville_cayenne=[
    ("LEONCE", "Chester"),
    ("LIE KON WAH", "Laurent"),
    ("CHIN-TEN-FUNG", "Georgina"),  # CHIN TEN FUNG sur site
    ("HORTH", "Auguste"),
    ("SANITE", "Arlette"),
    ("BAFAU", "Serge"),
    ("SAINT-HILAIRE", "Fabiola"),
    ("COLIN", "Nadine"),
    ("CLERVAUX", "Xavier"),
    ("VICTOR", "Patricia"),
    ("SAHA", "Erick"),
    ("CEPRIKA", "Ruth"),
    ("CHINON", "Claire"),
    ("MATHIAS", "Faviana Sandrine"),
    ("ARGOUBI ÉPOUSE CHOUCHANE", "Awatef"),
    ("CALUMEY", "Louis-Mike"),
    ("HIDAIR", "Laura"),
    ("CONTOUT", "Jean-Yves"),
    ("SILEBERT", "Rolande"),
    ("ROLDAN", "Steve"),
    ("PHINÉRA-HORTH", "Marie-Laure"),  # PHINERA-HORTH sur site
    ("LOE-MIE", "Roland"),
    ("ROBO CASSILDE", "Magali"),
    ("ROBO AYANNE", "Sadia"),
    ("MANCEE", "Mikael"),
    ("RUIZ", "Sébastien"),
    ("NAISSO", "Tineffa"),
    ("LETARD", "Oswald"),
    ("CHEN-TUNG", "Kenny"),
    ("FABIEN", "Frantz")
]

noms_cayenne=[nom_prenom[0] for nom_prenom in conseillers_municipaux_site_ville_cayenne]
# print(noms_cayenne)

print("🔹 Listés sur site en tant que conseillers municipaux et présents au RNE")
filtre_existe_site=conseillers_municipaux_cayenne["Nom de l'élu"].isin(noms_cayenne)
print(conseillers_municipaux_cayenne[filtre_existe_site])

print("🔸 Ecarts entre listés sur site en tant que conseillers municipaux et présents au RNE")
filtre_absent_site=~conseillers_municipaux_cayenne["Nom de l'élu"].isin(noms_cayenne)
print(conseillers_municipaux_cayenne[filtre_absent_site])
