from pandas import read_csv

# Exploration des collectivité à statut particulier pour identifier les listes d'élus.
# Nous avons besoin du code du département pour chaque élu.


# Définition "collectivité à statut particulier" : 
# Une collectivité à statut particulier est, en France, une collectivité territoriale
# qui, en application de l'article 72 de la Constitution, ne relève pas des trois catégories
#  que sont les communes, les départements et les régions, 
# sans pour autant être une collectivité d'outre-mer régie par l'article 74 de la Constitution.
# Src : https://fr.wikipedia.org/wiki/Collectivit%C3%A9_%C3%A0_statut_particulier


# Liste des collectivités à statut particulier selon l'INSEE :
# https://www.insee.fr/fr/information/3528272
# sachant qu' "une numérotation spécifique a été introduite" :
# La Ville de Paris (75C)
# Le Département de Mayotte (976D)
# La Métropole de Lyon (69M)
# Les collectivités territoriales uniques de Martinique (972R) et de Guyane (973R)
# La Collectivité de Corse (20R)
#
# Exception : La Collectivité européenne d’Alsace (6AE) 
# suit la numérotation spécifique mais n'est pas une collectivité
#  à statut particulier au sens de l’article 72 de la Constitution.


# Code officiel géographique (COG) 01.2023,
# Collectivités territoriales ayant les compétences départementales selon l'INSEE 
# https://www.insee.fr/fr/information/6800675 :
PATH_COG_COLLECTIVITES_COMPETENCES_DEPARTEMENTALES="./v_ctcd_2023.csv"
# Mais le fichier contient aussi les conseils départementaux
# en plus des collectivités territoriales à statut particulier
# et les départements ne sont pas cités (la région l'est).
# Colonnes :
# CTCD = Code de la collectivité
# REG = Code de la région
# TNCC = Type de nom en clair
# NCC = Nom en clair (majuscules)
# NCCENR = Nom en clair (typographie riche)
# LIBELLE = Nom en clair (typographie riche) avec article


# Liste des membres des assemblées des collectivités à statut particulier selon le RNE :
PATH_RNE_COLLECTIVITES_STATUT_PARTICULIER="./rne-ma-20221216.csv"
# N'inclut pas : 
# * La Ville de Paris (75C)
# * Le Département de Mayotte (976D)
# Inclut la Nouvelle-Calédonie sachant que d'après https://fr.wikipedia.org/wiki/Collectivit%C3%A9_%C3%A0_statut_particulier : 
# "La Nouvelle-Calédonie, en raison de son statut sui generis, 
# est parfois considérée comme une « collectivité à statut particulier d'outre-mer »,
# mais relève du titre XIII de la Constitution et non de l'article 72."


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
# ['Saint-Pierre-Et-Miquelon' 'Polynésie Française' 'Corse' 'Guyane'
#  'Saint-Barthélemy' 'Saint-Martin' 'Wallis Et Futuna' 'Nouvelle-Calédonie']
# ['975' '987' '94' '973' '977' '978' '986' '988']


