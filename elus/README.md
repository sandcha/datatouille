## Exploration des données du Répertoire national des élus (RNE)

Données : [RNE sur data.gouv.fr](https://www.data.gouv.fr/fr/datasets/repertoire-national-des-elus-1)

### Prérequis

Python :

```shell
pyenv install 3.10.5
pyenv local 3.10.5
```

### Exécuter les scripts

Dans un terminal Shell, installer les dépendances : 

```shell
cd elus/
poetry install
```

Puis, exécuter le script souhaité : 
* `poetry run python explore_conseillers_municipaux.py`
* ou `poetry run python explore_collectivites_statut_particulier.py`
