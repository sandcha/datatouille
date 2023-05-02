from pandas import read_csv


# Liste des collectivités à statut particulier selon l'INSEE :
# https://www.insee.fr/fr/information/3528272
# La Ville de Paris (75C)
# Le Département de Mayotte (976D)
# La Métropole de Lyon (69M)
# Les collectivités territoriales uniques de Martinique (972R) et de Guyane (973R)
# La Collectivité de Corse (20R)

# Exception : La Collectivité européenne d’Alsace (6AE) 
# n'est pas une collectivité à statut particulier
# au sens de l’article 72 de la Constitution.


# Liste des membres des assemblées des collectivités à statut particulier selon le RNE :
PATH_RNE_COLLECTIVITES_STATUT_PARTICULIER="./rne-ma-20221216.csv"


# Code officiel géographique (COG) 01.2023,
# Collectivités territoriales ayant les compétences départementales selon l'INSEE 
# (conseils départementaux et collectivités territoriales à statut particuler) :
PATH_COG_COLLECTIVITES_COMPETENCES_DEPARTEMENTALES="./v_ctcd_2023.csv"


membres_collectivites_particulieres=read_csv(
    PATH_RNE_COLLECTIVITES_STATUT_PARTICULIER,
    encoding="utf-8",
    sep='\t'
    )

print(membres_collectivites_particulieres.head())
print(membres_collectivites_particulieres.columns)

filtre_departement_inconnu=membres_collectivites_particulieres["Code du département"].isna()
membres_colstatpart_departement_inconnu=membres_collectivites_particulieres[filtre_departement_inconnu][
    [
        # "Code du département",
        "Code de la collectivité à statut particulier",
        "Libellé de la collectivité à statut particulier",
        # "Code de la circonscription métropolitaine"
    ]
]

print("RNE - Liste des collectivités à statut particulier mais à département non défini :")
print(membres_colstatpart_departement_inconnu["Libellé de la collectivité à statut particulier"].unique())
print(membres_colstatpart_departement_inconnu["Code de la collectivité à statut particulier"].unique())
