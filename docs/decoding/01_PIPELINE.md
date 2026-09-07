# Pipeline de décodage — statut réel

## Fenêtre

Fenêtre utilisée : premiers 36 chiffres de π en comptant le `3` initial et en ignorant le point décimal.

## Provenance

La découverte a été **exploratoire**.

Les règles finales n'étaient pas preregistrées avant de voir les résultats. Certaines frontières et grammaires ont été découvertes au cours du travail puis verrouillées.

La formulation correcte est donc :

> **reproductible ex post sous les règles publiées**, pas « protocole fixé à l'avance ».

Toute ancienne phrase affirmant le contraire est archivée comme erreur de provenance.

## Transformation finale

1. sélectionner la fenêtre;
2. renverser la séquence pour la lecture de découverte;
3. appliquer les segmentations/grammaires finales;
4. utiliser A1Z26 pour les valeurs `1–26`;
5. traiter `0` comme `O` lorsque le token l'exige, tout en conservant `0` dans `B0UM` comme trace numérique;
6. ne pas anagrammer ni réordonner les lettres produites;
7. conserver `GIHECEF` et `JNON` entiers;
8. arrêter le décodage publié à `88` parce qu'aucun bloc cohérent supplémentaire n'a été stabilisé sous cette lentille.

## Séquence renversée de travail

```text
88 20597238 334626483239 7985356 29514 13
```

La séquence conceptuelle est rapportée dans l'ordre correspondant aux positions originales du début de π :

```text
M → BIEN → GIHECEF → JNON → B0UM → SIZE
```

Cette distinction entre **ordre matériel de la chaîne renversée** et **ordre conceptuel des régions originales** doit toujours être explicitée.

## Interdictions pour les tests futurs

Une fois un test prospectif déclaré :

- pas de nouvelle langue ajoutée après résultat;
- pas de nouveau traitement du zéro;
- pas de nouvelles règles locales;
- pas de déplacement de fenêtre;
- pas de nouveau stop choisi après inspection;
- pas de nouvelle abstraction sémantique non prévue.
