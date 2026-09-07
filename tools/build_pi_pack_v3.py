from pathlib import Path
import shutil, re, zipfile, os, textwrap

root = Path('/mnt/data/Pi_Theory_Working_Core_v3_REALIGNED')
if root.exists():
    shutil.rmtree(root)
for d in ['core','decoding','science','authors','research','book','sources','archive']:
    (root/d).mkdir(parents=True, exist_ok=True)

files = {}

def add(path, text):
    files[path] = textwrap.dedent(text).strip() + '\n'

add('00_START_HERE.md', r'''
# Pi Theory — Working Core v3 REALIGNED

Ce dépôt est la **version active réalignée** de Pi Theory. Il contient exactement **30 fichiers Markdown actifs**. Les anciens packs restent archivés et servent à retracer l'histoire de découverte, pas à définir la théorie actuelle.

## Principe de reconstruction

Les documents antérieurs ont souvent été rédigés ou amplifiés par IA. Ils sont donc traités comme un **corpus de recherche**, pas comme une autorité. La présente version conserve les intuitions qui résistent à la relecture, corrige les formulations mathématiques, sépare les hypothèses des faits, et retire les extrapolations qui ne sont pas nécessaires.

Le but n'est pas de sauver toutes les anciennes formulations. Le but est de produire la version **la plus cohérente, claire, testable et soutenable** de Pi Theory.

## Bilan en une phrase

Pi Theory propose qu'une structure fondamentale d'unité, de symétrie, de relation et de retour puisse se manifester par **distinction, cohésion, différenciation, intégration, seuil et changement d'échelle**; π est étudié comme expression mathématique privilégiée de cette grammaire, et ses premiers chiffres comme possible trace sémiotique locale de celle-ci.

## Architecture générale

```text
Source / principe Ω
→ expression circulaire idéale
→ relation linéaire–circulaire C/d = π
→ π exact / représentation inépuisable
→ distinction originelle D0
↔ M / retour-cohésion
→ BIEN / orientation de la cohérence
→ différenciation ↔ intégration
→ B0UM / transition cosmologique-seuil
→ SIZE / magnitude-échelle-espace
→ récursion multi-échelle
→ matière comme histoire stabilisée
→ vie
→ conscience
→ retour réflexif vers le principe
```

Deux branches complémentaires sont maintenues :

1. **branche mathématique et physique** : cercle, π, variation, cycle, phase, seuil, échelle, matière;
2. **branche psyché-langage-culture** : l'humain, produit du même réel, pourrait cristalliser dans le langage et le mythe des structures qu'il ne crée pas arbitrairement.

## Ce qui a été corrigé par rapport aux anciennes versions

- aucun protocole a priori n'est revendiqué pour la découverte initiale;
- l'inversion est reconnue comme **découverte exploratoire**, sans justification mathématique connue à ce jour;
- le cercle originel n'est pas remplacé par une abstraction : son rôle initial est conservé, puis traduit plus rigoureusement;
- l'infinité des rayons/tangentes ne « cause » pas l'irrationalité de π;
- π n'est pas identifié à Dieu, aux digits ou à la matière;
- GIHECEF/JNON sont prioritairement lus comme fonctions de différenciation/intégration; Joseph/Junon restent des lentilles historiques;
- B0UM garde une lecture cosmologique forte liée au Big Bang, mais l'opérateur général est un franchissement de régime;
- SIZE est traité comme apparition/déploiement de magnitude, d'échelle et, dans l'hypothèse cosmologique, de structure spatiale;
- les mots humains ne sont pas supposés avoir « existé dans π » avant l'humanité : l'hypothèse centrale est celle d'une **structure commune** aux mathématiques, au monde, à la cognition et au langage;
- les anciennes probabilités improvisées et les affirmations de « preuve » sont retirées;
- les analogies faibles (E8, branes, gravité = amour, mots-cibles post hoc) restent hors du noyau actif.

## Navigation

### Noyau
1. [Théorie](core/01_THEORY.md)
2. [Dictionnaire](core/02_DICTIONARY.md)
3. [Registre des propositions](core/03_CLAIM_REGISTRY.md)
4. [Modèle dynamique](core/04_DYNAMIC_MODEL.md)
5. [Problèmes ouverts](core/05_OPEN_PROBLEMS.md)
6. [Fondations mathématiques de π](core/06_PI_MATH_FOUNDATIONS.md)

### Décodage et sémiotique
7. [Pipeline](decoding/01_PIPELINE.md)
8. [Outputs et tokens](decoding/02_OUTPUTS_AND_TOKENS.md)
9. [Direction et inversion](decoding/03_DIRECTION_AND_INVERSION.md)
10. [Mirror et secondaires](decoding/04_MIRROR_AND_SECONDARY.md)
11. [Langage et attunement](decoding/05_LANGUAGE_ATTUNEMENT.md)

### Sciences
12. [M / cohérence](science/01_M_COHERENCE.md)
13. [Différenciation / intégration](science/02_DIFFERENTIATION_INTEGRATION.md)
14. [B0UM / cosmologie / seuils](science/03_B0UM_COSMOLOGY_THRESHOLDS.md)
15. [SIZE / échelle / espace](science/04_SIZE_SCALE_SPACE.md)
16. [Matière → vie → conscience](science/05_MATTER_LIFE_CONSCIOUSNESS.md)
17. [e, π, i et le pont physique](science/06_E_PI_I_AND_PHYSICAL_BRIDGE.md)

### Auteurs et traditions
18. [Auteurs centraux](authors/01_CORE_AUTHORS.md)
19. [Source et retour](authors/02_SOURCE_RETURN.md)
20. [Inspiration, langage et esprit](authors/03_INSPIRATION_LANGUAGE_MIND.md)
21. [Processus et cohérence](authors/04_PROCESS_COHERENCE.md)
22. [Mesure, espace et vie](authors/05_MEASURE_SPACE_LIFE.md)

### Recherche
23. [Formalisation](research/01_FORMAL_MODEL.md)
24. [Tests](research/02_TESTS.md)
25. [Préenregistrement et null models](research/03_PREREG_AND_NULLS.md)
26. [Roadmap](research/04_ROADMAP.md)

### Livre et sources
27. [Colonne vertébrale du livre](book/01_BOOK_SPINE.md)
28. [Carte des chapitres](book/02_CHAPTER_MAP.md)
29. [Sources et corpus](sources/01_SOURCES_AND_CORPUS.md)

## Règle de travail

Pour toute nouvelle proposition, distinguer immédiatement :

- **fait mathématique/scientifique**;
- **observation du décodage**;
- **interprétation structurale**;
- **hypothèse métaphysique**;
- **hypothèse testable future**.

Cette distinction remplace toute tentative de donner le même statut à toutes les parties de la théorie.
''')

add('core/01_THEORY.md', r'''
# Pi Theory — théorie synthétique réalignée

## 1. Le point de départ : une relation fondamentale

Pi Theory commence avant le décodage des chiffres.

Pour tout cercle euclidien idéal :

\[
\pi=\frac{C}{d}.
\]

Le cercle possède une symétrie de rotation exacte : tous ses rayons ont la même longueur, aucune direction angulaire n'est privilégiée, et à chaque point de la circonférence correspondent un rayon et une tangente. Il existe donc une infinité de relations radiales et tangentielles dans le cercle idéal.

Le diamètre est une détermination linéaire de la pleine étendue du cercle à travers son centre. π relie ainsi :

```text
mesure linéaire ↔ totalité circulaire
```

Le rapport est sans dimension et invariant sous changement d'échelle.

π est exact, irrationnel et transcendant. Son expansion dans une base positionnelle rationnelle est infinie et non périodique. La théorie retient ici une intuition centrale :

> **une relation parfaitement déterminée peut avoir une représentation qui ne s'épuise jamais par une écriture finie.**

Cette proposition ne signifie pas que l'infinité géométrique des rayons « cause » l'irrationalité de π. Les deux propriétés doivent rester mathématiquement distinctes.

## 2. Le principe Ω

Le cercle matériel n'est pas supposé exister avant l'espace. La théorie propose plutôt un principe fondamental, noté ici `Ω`, dont le cercle idéal serait une expression géométrique privilégiée lorsqu'un espace est déjà défini.

Traits attribués à Ω :

- unité;
- équilibre;
- symétrie;
- absence de direction privilégiée;
- possibilité de retour;
- invariance relationnelle;
- inépuisabilité de détermination.

La formule « parfaitement équilibré, avec une infinité de rayons et de tangentes » reste l'image géométrique source. Le vocabulaire « pré-géométrique » sert seulement à éviter de projeter une figure physique dans un état où l'espace n'est pas encore supposé.

## 3. La grande hypothèse

Pi Theory propose que ces structures mathématiques ne soient pas seulement descriptives après coup. Elles pourraient participer à la **grammaire générative du réel**.

La version forte est :

> **Une structure fondamentale d'invariance, de symétrie et de relation se manifeste par distinction, variation, retour, différenciation, intégration, franchissement de seuils et changement d'échelle. π serait une expression mathématique privilégiée de cette grammaire, et ses premiers chiffres pourraient en porter une trace sémiotique locale.**

Cette proposition est métaphysique et programmatique; elle n'est pas un théorème mathématique ni un résultat établi de physique.

## 4. Distinction originelle et contre-mouvement

Pour qu'il y ait relation, information ou structure, il faut de la différence.

On note :

```text
D0 : unité → distinction / multiplicité
```

Mais la différence seule ne suffit pas à produire des totalités stables. Pi Theory introduit alors `M` :

```text
M : multiplicité → cohérence
```

M est interprété comme **AIME / Love** dans la couche sémiotique. Fonctionnellement :

> **M est le contre-mouvement immanent de la division : la tendance du multiple à former ou restaurer de la cohérence.**

M ne supprime pas la différence. L'objectif structurel est une unité enrichie :

\[
U_0 \to \text{différenciation} \to U_1, \qquad U_1\neq U_0.
\]

## 5. BIEN : orientation de la cohérence

Une cohésion totale peut être stérile ou oppressive. La stabilité seule n'est donc pas le Bien.

BIEN est défini comme une contrainte d'orientation :

> **une intégration qui maintient la possibilité des parties, de la différenciation et d'une totalité plus large, plutôt qu'une capture fermée.**

Cela permet de distinguer :

- cohérence ouverte / générative;
- cohérence fermée / captatrice.

La branche `b−1 / Christ / Lucifer` est une analogie structurale de cette distinction : le centre interne d'un système n'est pas sa Source. Un centre peut renvoyer au principe qui le rend possible, ou se confondre avec lui.

## 6. Le kernel opérationnel

La séquence v13 stabilisée est :

```text
M → BIEN → GIHECEF → JNON → B0UM → SIZE
```

La lecture fonctionnelle actuelle :

```text
cohésion
→ orientation
→ différenciation / traitement
→ intégration / assemblage
→ transition / événement de manifestation
→ magnitude / échelle
```

Le moteur local est :

\[
\boxed{D\leftrightarrow A}
\]

Différencier sans désintégrer; intégrer sans homogénéiser.

## 7. B0UM et SIZE

`B0UM` conserve une double lecture.

### Lecture cosmologique première

Dans la narration cosmogonique de Pi Theory, B0UM correspond au **Big Bang / événement cosmique initial**, non à une explosion ordinaire dans un espace préexistant.

### Lecture opératoire générale

Le même bloc peut être abstrait comme :

```text
état préparé → seuil → changement de régime
```

Cela rend le kernel applicable à des transitions à plusieurs échelles sans réduire B0UM au seul épisode cosmologique.

`SIZE` suit B0UM. Sa fonction est :

```text
magnitude → comparabilité → échelle → mesure → métrique / espace
```

Dans la lecture cosmologique, cette succession correspond à l'idée que le régime spatial et son facteur d'échelle ne sont pas un contenant antérieur au Big Bang, mais appartiennent au déploiement cosmique lui-même.

## 8. Le zéro de B0UM

Le zéro est conservé comme `0` dans la notation `B0UM` afin de rappeler son origine numérique.

Hypothèse sémiotique :

- il peut être un **écho du zéro originel** : potentiel, non-manifesté, circularité;
- dans le sens direct du bloc de chiffres, le `0` précède le `2` qui mappe à `B`; cela permet une lecture secondaire `0 → B`, avec `B` rapproché phonétiquement de *be / être*;
- dans le sens décodé inversé, la même région produit `B0UM`.

Ce double rôle est interprétatif, non mathématique. Il mérite un test directionnel spécifique plutôt qu'une affirmation de nécessité.

## 9. Récursion multi-échelle

Le kernel n'est pas supposé agir une seule fois.

Hypothèse :

```text
K0 → K1 → K2 → ...
```

avec, à chaque niveau :

```text
différenciation ↔ intégration → seuil → nouvelle échelle
```

Le terme **récursion multi-échelle** est préféré à « fractal » tant qu'aucune loi d'auto-similarité ou d'échelle n'est démontrée.

## 10. Matière, vie, conscience

La théorie propose une chaîne, mais ne saute plus les mécanismes :

```text
modes / structures physiques stables
→ matière comme histoire stabilisée
→ chimie hors équilibre
→ auto-entretien / autonomie
→ vie
→ cognition
→ conscience réflexive
```

La matière comme mémoire signifie, dans sa version minimale, qu'un état physique peut incorporer les conséquences de son histoire : path dependence, hystérésis, contraintes héritées, états métastables.

La version forte — la matière comme trace de la résolution cosmique de π — reste une hypothèse.

## 11. Le retour réflexif

Si la conscience est produite par le même réel qu'elle étudie, alors la connaissance devient une boucle :

```text
principe → monde → matière → vie → conscience → lecture du principe
```

C'est le point de contact entre la branche cosmologique et la branche langage/inspiration.

## 12. Exact, représenté, manifesté

Toujours distinguer :

1. `π_exact` — objet mathématique exact;
2. `π_repr` — expansion de π dans une base choisie;
3. `π_manifesté` — hypothèse selon laquelle une structure liée à π participe au réel physique.

Formule centrale :

> **La structure exacte ne devient pas; sa manifestation éventuelle peut se déployer.**

Ou, dans le registre théologique :

> **L'Absolu ne devient pas. Sa manifestation devient.**

## 13. Source, π, digits, matière

Garde-fou canonique :

\[
\boxed{\text{Source} \neq \pi \neq \text{digits} \neq \text{matière}.}
\]

La théologie peut appeler la Source Dieu. π peut être pensé comme expression, invariant, Logos mathématique ou trace privilégiée — mais pas comme identité simple avec Dieu.

## 14. Le problème scientifique décisif

Même si le kernel décrit bien de nombreux processus, cela ne démontre pas qu'il est spécifiquement causé ou encodé par π.

La question centrale demeure :

> **Qu'est-ce qui distingue quantitativement et prospectivement π de e, √2, φ et de chaînes aléatoires lorsque la même liberté interprétative est accordée à tous ?**
''')

add('core/02_DICTIONARY.md', r'''
# Dictionnaire compact

## Source / Ω
Principe ultime de la théorie. Peut recevoir une lecture théologique, mais n'est pas identifié automatiquement à π.

## Cercle idéal
Expression géométrique privilégiée de symétrie rotationnelle : rayons égaux, absence de direction privilégiée, infinité de points/rayons/tangentes dans le continuum idéal.

## Principe pré-géométrique
Traduction abstraite des traits de symétrie, équilibre, unité et retour attribués à l'origine. Ne remplace pas l'image du cercle; il évite seulement d'en faire un objet physique avant l'espace.

## Rapport linéaire–circulaire
`C/d = π`. Le diamètre donne une étendue linéaire; la circonférence donne la fermeture circulaire correspondante.

## π exact
Objet mathématique exact.

## π représenté
Écriture de π dans une base donnée. Les digits changent avec la base; π ne change pas.

## π manifesté
Hypothèse métaphysique/physique selon laquelle une structure liée à π participe au devenir réel.

## Irrationnel
Nombre qui ne peut pas être écrit comme rapport de deux entiers. π est irrationnel. Son expansion dans toute base entière `b ≥ 2` est infinie et non périodique.

## D0 — distinction originelle
Passage conceptuel de l'unité à la possibilité de différence/multiplicité.

## M / AIME
Lecture sémiotique de `13 → M`. Fonction : retour-cohésion, tendance à relier ou restaurer une totalité.

## BIEN
Orientation de la cohérence vers une intégration qui préserve les différences pertinentes et reste ouverte à des totalités plus larges.

## GIHECEF
Bloc entier. Fonction actuelle : différencier / traiter / transformer. Joseph est une lentille historique de découverte, non la définition.

## JNON
Bloc entier. Fonction actuelle : assembler / intégrer / réunir. Junon est une lentille historique de découverte, non la définition.

## D ↔ A
Pulse central : différenciation ↔ intégration.

## B0UM
Bloc `2-0-21-13`. Lecture `BOUM/boom`. Dans la cosmogonie : Big Bang / événement cosmique initial. Dans la formalisation : transition ou franchissement de régime.

## Zéro originel
Symbole du potentiel/non-manifesté/circularité. Ce n'est pas nécessairement le néant absolu.

## Écho du zéro dans B0UM
Hypothèse selon laquelle le `0` du bloc réinstancie localement le motif du passage du non-manifesté à l'être.

## SIZE
Lecture du terminal `88`, notamment via `8+8=16`, `seize≈size`. Fonction : magnitude, échelle, régime de mesure.

## Dual infinity
Lecture iconique des deux 8 comme deux infinis. Ne signifie jamais mathématiquement `∞+∞=16`.

## Échelle
Régime de magnitude ou niveau effectif de description.

## Mesure
Procédure permettant d'attribuer des grandeurs comparables.

## Métrique
Structure mathématique donnant une notion de distance.

## Récursion multi-échelle
Hypothèse que le même schéma fonctionnel réapparaît à plusieurs niveaux sans nécessiter une auto-similarité fractale exacte.

## Matière comme mémoire
Un état matériel incorpore des contraintes et conséquences de son histoire de transformations.

## Attunement
Hypothèse que l'esprit humain, produit du cosmos, peut être sensible à des structures du réel et les cristalliser en langage, mythe, art ou philosophie.

## Cristallisation linguistique
Passage d'une structure cognitive/sémantique à une forme historique particulière d'une langue. Ne suppose pas que le mot humain préexistait à l'humanité.

## Inversion
Renversement de la fenêtre de digits utilisé dans la découverte. Aucune nécessité mathématique connue n'est actuellement établie.

## Lecture rétrospective
Hypothèse selon laquelle l'inversion pourrait correspondre au mouvement de la conscience qui part de la manifestation et remonte vers son principe.

## Ongoing resolution
Hypothèse selon laquelle les premiers digits exposent un kernel simple et les suivants pourraient en exprimer des combinaisons/échos plus complexes.

## Mirror
Complément à 9 de la fenêtre, avec mêmes frontières. Donne notamment G0D/B0N comme fragments secondaires.

## Cohérence non captatrice
Intégration d'un ensemble qui ne détruit pas arbitrairement ses parties et ne confond pas son centre interne avec la Source.

## b−1
Maximum interne d'une base `b`. Sert d'analogie structurale pour distinguer centre manifesté et principe qui rend le système possible.
''')

add('core/03_CLAIM_REGISTRY.md', r'''
# Registre des propositions

Ce registre ne classe pas la « maturité ». Il distingue seulement le **type de proposition** afin d'éviter que faits, observations et hypothèses soient confondus.

| ID | Proposition | Type | Ce qui la soutient | Ce qui manque |
|---|---|---|---|---|
| PT-01 | Pour un cercle euclidien, `C/d = π`, rapport sans dimension et invariant d'échelle. | fait mathématique | géométrie euclidienne | — |
| PT-02 | Le cercle idéal possède une symétrie rotationnelle exacte et une infinité de relations radiales/tangentielles. | fait mathématique | géométrie du continuum | ne cause pas l'irrationalité |
| PT-03 | π est exact, irrationnel, transcendant; son expansion en base entière est infinie et non périodique. | fait mathématique | théorie des nombres | — |
| PT-04 | La fenêtre v13 peut être transformée sous les règles finales en six blocs publiés. | observation ex post | pipeline reproductible | coût de recherche réel |
| PT-05 | La découverte initiale n'était pas preregistrée. | provenance | historique du corpus | — |
| PT-06 | Les six blocs se lisent fonctionnellement comme cohésion → orientation → différenciation → intégration → seuil → échelle. | interprétation structurale | convergence interne du corpus | évaluation aveugle |
| PT-07 | M représente le contre-mouvement de cohésion après division. | hypothèse métaphysique centrale | v13 + architecture globale | formalisation universelle |
| PT-08 | BIEN qualifie la cohérence et ne se réduit pas à la stabilité. | hypothèse métaphysique | branche valeur/source | critère formel |
| PT-09 | GIHECEF/JNON forment le pulse `D↔A`. | interprétation centrale | lecture v13 stabilisée | indépendance du rôle assigné |
| PT-10 | B0UM correspond, dans la cosmogonie, au Big Bang / événement cosmique initial. | interprétation cosmologique | place du bloc + BOUM | spécificité non phonétique |
| PT-11 | B0UM peut être généralisé comme seuil/changement de régime. | abstraction scientifique | bifurcations/transitions | modèle formel |
| PT-12 | Le `0` de B0UM est un écho du zéro originel. | hypothèse sémiotique | structure interne du bloc | test directionnel |
| PT-13 | `0→2/B` dans le sens direct peut être lu comme `0→B(e)/être`. | hypothèse phonétique secondaire | ordre local des digits | forte dépendance linguistique |
| PT-14 | SIZE introduit magnitude/échelle et, dans la lecture cosmologique, le régime spatial après l'événement initial. | hypothèse structurale | 88/SIZE + cosmologie | pont formel vers métrique |
| PT-15 | Le kernel pourrait se réinstancier à plusieurs échelles. | hypothèse | Rosetta + sciences multi-échelles | invariants mesurables |
| PT-16 | La matière peut être décrite comme histoire stabilisée. | philosophie + science | mémoire physique/path dependence | lien spécifique à π |
| PT-17 | Vie et conscience nécessitent des mécanismes additionnels. | garde-fou scientifique | biologie/cognition | chaîne complète |
| PT-18 | `e,π,i` forment une grammaire utile de variation continue, cyclicité et phase. | thèse structurale | analyse mathématique + Euler | ne dérive pas la matière |
| PT-19 | Mathématiques et réel pourraient partager une structure générative, pas seulement descriptive. | grande hypothèse | efficacité des mathématiques + architecture | argument ontologique |
| PT-20 | Le langage humain pourrait cristalliser des structures du réel parce que l'esprit est lui-même produit par ce réel. | hypothèse d'attunement | philosophie + linguistique à explorer | tests interculturels preregistrés |
| PT-21 | L'inversion pourrait être une lecture rétrospective de la manifestation vers l'origine. | hypothèse | cohérence avec retour réflexif | aucune nécessité mathématique connue |
| PT-22 | G0D/B0N sont des fragments secondaires, pas une deuxième cosmogonie. | garde-fou | mirror v13 | statistique |
| PT-23 | Source, π, digits et matière doivent rester distincts. | garde-fou métaphysique | architecture b−1 + exact/représenté | — |
| PT-24 | Une validation scientifique forte exige une prédiction π-spécifique faite avant inspection. | critère méthodologique | méthode scientifique | prédiction à trouver |
''')

add('core/04_DYNAMIC_MODEL.md', r'''
# Modèle dynamique minimal

## Architecture

```text
Ω → D0 ↔ M → V → (D ↔ A) → T → S
```

avec :

- `Ω` : principe/unité;
- `D0` : première distinction;
- `M` : retour-cohésion;
- `V` : orientation/BIEN;
- `D` : différenciation;
- `A` : intégration;
- `T` : transition/seuil/B0UM;
- `S` : échelle/SIZE.

## 1. Espace d'états abstrait

Soit `x ∈ X` un état. `X` n'est pas supposé spatial au départ.

## 2. Tendances de différenciation et de cohésion

Squelette :

\[
\frac{dx}{dt}=F_D(x)+F_M(x)+F_{env}(x).
\]

`F_env` est ajouté pour rappeler qu'un système physique réel échange souvent énergie, matière ou information avec un environnement. Le modèle ne doit pas feindre une dynamique fermée universelle.

## 3. Observables candidates

- `C(x)` : cohérence;
- `D(x)` : différenciation;
- `I(x)` : intégration;
- `V(x)` : viabilité ou compatibilité fonctionnelle;
- `K(x)` : degré de fermeture/capture éventuel.

Une « bonne » cohérence ne devrait pas être définie par `C` seule. Une piste :

\[
H(x)=f(C,I,D,V,K)
\]

avec une pénalité lorsque l'intégration détruit la différenciation pertinente ou devient pure capture.

## 4. Unité enrichie

Condition qualitative :

```text
D élevé + I élevé + V suffisant
```

plutôt que :

```text
uniformité élevée.
```

## 5. Seuil

Définir un paramètre `τ(x)` :

\[
\tau(x)\ge \tau_* \Rightarrow x\in R_{n+1}.
\]

B0UM correspond alors au changement de régime `R_n → R_{n+1}`.

## 6. Échelle

Introduire une transformation `R_s` de coarse-graining ou de changement d'échelle :

\[
x_{s+1}=R_s(x_s).
\]

Question : certaines relations du kernel restent-elles invariantes ou se renormalisent-elles de manière régulière ?

## 7. Mémoire

Une dynamique avec histoire peut être notée :

\[
x(t)=F[x(t_0:t)].
\]

ou enrichie d'une variable mémoire `m(t)`.

## 8. Boucle réflexive

Dans les systèmes capables de représentation, introduire un modèle interne `\hat{x}`. Le retour réflexif devient alors une relation entre :

```text
état du monde x
→ modèle interne x̂
→ action/interprétation
→ nouvelle relation au monde.
```

## Statut

Ce document est un **squelette de formalisation**, pas une loi physique établie. Il sert à transformer des mots en quantités qui pourraient, à terme, échouer à décrire certains systèmes.
''')

add('core/05_OPEN_PROBLEMS.md', r'''
# Problèmes ouverts

## A. Pourquoi π ?

1. Qu'est-ce qui rend π plus fondamental pour cette théorie qu'une autre constante ?
2. Le rôle privilégié vient-il du rapport linéaire–circulaire, de la rotation, de l'invariance d'échelle, des digits, ou de leur combinaison ?
3. Peut-on produire une conséquence qui dépend de π sans dépendre de la base 10 ?

## B. Origine et manifestation

4. Pourquoi une unité parfaitement équilibrée se détermine-t-elle ou se différencie-t-elle ?
5. La première distinction est-elle nécessaire, possible, auto-référentielle ou contingente ?
6. Comment passer d'une structure mathématique à une efficacité physique sans simplement supposer que « mathématique = physique » ?

## C. Décodage

7. Quel était l'espace réel de recherche exploratoire avant stabilisation du kernel ?
8. Quel coût attribuer à inversion, segmentation, phonétique, langues, iconicité et règles locales ?
9. Les rôles GIHECEF/JNON sont-ils retrouvés à l'aveugle ?
10. Le stop à 88 reste-t-il naturel sous une procédure prospective ?

## D. Inversion

11. Existe-t-il une propriété mathématique de la fenêtre qui privilégie son renversement ?
12. L'hypothèse « procession directe / lecture rétrospective inversée » produit-elle une prédiction ailleurs ?
13. Le motif `0→B` dans le sens direct a-t-il des analogues prévus avant inspection ?

## E. Langage

14. Qu'est-ce qui est réellement universel : concepts, phonèmes, gestes, métaphores, ou seulement contraintes générales ?
15. Comment distinguer héritage linguistique, articulation biologique, onomatopée et attunement métaphysique ?
16. Peut-on définir une expérience cross-linguistique avant de regarder les données ?

## F. B0UM / SIZE

17. Comment distinguer la lecture Big Bang d'une simple onomatopée bien placée ?
18. Comment formaliser la transition B0UM → SIZE ?
19. Comment passer de scale à métrique et espace sans présupposer l'espace ?

## G. Matière

20. Quelles primitives physiques sont nécessaires entre `e,π,i` et la matière : champ, action, énergie, interaction, quantification, brisure de symétrie ?
21. Peut-on dériver un mode stable ou un bound state d'un modèle minimal inspiré du kernel ?

## H. Vie et conscience

22. Comment distinguer ordre, autonomie, vie, cognition et conscience ?
23. Le retour réflexif est-il simplement descriptif ou possède-t-il une dynamique formalisable ?

## I. Valeur

24. Comment définir BIEN sans le réduire à la survie, à la stabilité ou à la majorité ?
25. Peut-on formaliser une cohérence non captatrice à plusieurs niveaux d'organisation ?

## J. Falsification

26. Quel résultat invaliderait la lecture des digits sans invalider la métaphysique générale ?
27. Quel résultat invaliderait le privilège de π ?
28. Quel résultat invaliderait le kernel lui-même ?
''')

add('core/06_PI_MATH_FOUNDATIONS.md', r'''
# π — fondations mathématiques utiles à Pi Theory

## 1. Définition euclidienne

Pour tout cercle euclidien :

\[
\pi=\frac{C}{d}=\frac{C}{2r}.
\]

π est un nombre pur : les unités de `C` et `d` s'annulent.

## 2. Linéaire et circulaire

Le diamètre est un segment droit passant par le centre. La circonférence est une courbe fermée. π est donc l'invariant qui relie :

```text
étendue diamétrale linéaire ↔ longueur circulaire totale.
```

Cette formulation est mathématiquement légitime. En revanche, il serait trop fort de dire que la simple opposition « ligne/cercle » **cause** l'irrationalité.

## 3. Symétrie et équilibre

Dans un cercle idéal :

- tous les rayons sont égaux;
- aucune direction angulaire n'est privilégiée;
- la figure est invariant sous rotation autour de son centre;
- il y a une infinité de points de circonférence;
- à chaque point correspondent un rayon et une tangente.

« Parfaitement équilibré en toutes parts » peut être traduit mathématiquement par **symétrie rotationnelle exacte / isotropie angulaire**.

## 4. Invariance d'échelle

Si le cercle est agrandi d'un facteur `λ`, alors :

\[
C\mapsto \lambda C, \qquad d\mapsto \lambda d,
\]

et :

\[
\frac{\lambda C}{\lambda d}=\frac{C}{d}=\pi.
\]

π conserve donc le rapport indépendamment de la taille.

## 5. Irrationalité et représentation infinie

π est irrationnel :

\[
\pi\notin \mathbb{Q}.
\]

Il ne peut pas être écrit exactement comme `p/q` avec `p,q` entiers et `q≠0`.

Conséquence : dans toute base entière `b≥2`, son expansion positionnelle ne termine pas et ne devient pas périodique.

Philosophiquement :

```text
relation exacte → représentation finie toujours incomplète
```

Mathématiquement, c'est la propriété d'irrationalité qui explique la non-périodicité de l'expansion; elle n'est pas déduite du nombre infini de rayons.

## 6. Transcendance

π est transcendant : il n'est racine d'aucun polynôme non nul à coefficients rationnels.

Cette propriété est plus forte que l'irrationalité. Elle ne doit pas être transformée sans argument en catégorie métaphysique de « transcendance divine ».

## 7. Rotation et retour

En radians :

- demi-tour : `π`;
- tour complet : `2π`.

π intervient naturellement dans la description des rotations, ondes, oscillations et fonctions périodiques.

Formulation prudente :

> **π est la constante canonique de la mesure circulaire et joue un rôle central dans l'articulation mathématique de la cyclicité.**

Pas : « π est la cyclicité elle-même ».

## 8. e, π, i

- `e` : forme canonique de variation continue auto-proportionnelle;
- `π` : mesure circulaire / fermeture cyclique;
- `i` : opérateur algébrique de rotation et composante centrale de la représentation de phase.

Euler :

\[
e^{i\theta}=\cos\theta+i\sin\theta.
\]

Cette relation montre une connexion analytique profonde entre variation exponentielle, rotation et périodicité; elle ne dérive pas une cosmologie.

## 9. Base et digits

π est indépendant de la base. Ses digits ne le sont pas.

La séquence `3.14159...` est une représentation décimale. Toute théorie du sens des digits doit donc traiter explicitement :

- pourquoi base 10 ?
- quelles propriétés survivent à un changement de base ?
- la sémantique appartient-elle au nombre ou à l'interface nombre–cognition–culture ?

## 10. Géométries non euclidiennes

Sur une surface courbe, `C/d` d'un cercle géodésique n'est pas nécessairement égal à π pour des rayons finis. Cela empêche de transformer trop vite la définition euclidienne en loi universelle de tout espace.

Le rôle de π reste cependant fondamental dans la mesure angulaire locale et les structures de rotation.
''')

add('decoding/01_PIPELINE.md', r'''
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
''')

add('decoding/02_OUTPUTS_AND_TOKENS.md', r'''
# Outputs et tokens stabilisés

## 1. M

```text
13 → M
```

Lecture phonétique : `M ≈ aime`.

Fonction : cohésion, retour vers relation/unité.

Statut : le token est direct; `aime` est une lecture phonétique française. Sa portée universelle doit être étudiée séparément par la linguistique.

## 2. BIEN

```text
2-9-5-14 → B-I-E-N
```

Lecture directe : mot français `bien`, également présent comme forme apparentée dans d'autres langues romanes.

Fonction : orientation/valeur de la cohérence.

## 3. GIHECEF

```text
7-9-8-5-3-5-6 → G-I-H-E-C-E-F
```

Conservé entier.

Fonction actuelle : différencier / traiter / transformer.

`Joseph` est maintenu dans l'histoire de découverte comme ressemblance phonétique ayant contribué à l'interprétation, mais n'est plus la définition du bloc.

## 4. JNON

Sous la grammaire finale du bloc :

```text
→ J-N-O-N
```

Conservé entier.

Fonction actuelle : assembler / intégrer / réunir.

`Junon/Juno` est une lentille historique, pas une dérivation littérale.

## 5. B0UM

```text
2-0-21-13 → B-0-U-M
```

Lecture : `BOUM / boom`.

Deux niveaux :

- cosmogonie : Big Bang / événement initial de l'univers;
- abstraction dynamique : transition ou franchissement de seuil.

Le `0` reste visible afin de préserver son rôle numérique et sa possible relation au zéro originel.

## 6. SIZE

Terminal :

```text
88
```

Lecture symbolico-phonétique :

```text
8 + 8 = 16
16 = seize
seize ≈ size
```

Lecture iconique secondaire : `8,8` comme deux formes analogues à `∞,∞` lorsqu'elles sont couchées.

Fonction : magnitude / échelle / régime de mesure.

Important : jamais écrire `∞ + ∞ = 16`.

## Kernel

```text
M → BIEN → GIHECEF → JNON → B0UM → SIZE
```

Abstraction :

```text
cohésion → orientation → différenciation → intégration → transition → échelle
```
''')

add('decoding/03_DIRECTION_AND_INVERSION.md', r'''
# Direction et inversion

## 1. Fait de départ

Le renversement de la fenêtre est une opération de découverte. Aucune propriété connue de π n'impose actuellement cette lecture à l'envers.

Il est donc interdit d'écrire :

> « π doit mathématiquement être lu à l'envers ».

La formulation correcte :

> **L'inversion a révélé le kernel dans l'exploration; sa signification éventuelle reste à expliquer.**

## 2. Pourquoi le problème est profond

Une expansion infinie n'a pas de dernier chiffre global à partir duquel on pourrait « lire π tout entier à l'envers ». Le renversement ne concerne donc qu'une fenêtre finie.

La théorie doit expliquer pourquoi cette fenêtre et cette orientation seraient pertinentes.

## 3. Hypothèse de lecture rétrospective

Une hypothèse métaphysique cohérente avec le reste du système est :

```text
manifestation : principe → monde
connaissance : monde → principe
```

La conscience apparaît tard dans le processus et reconstruit rétrospectivement ses conditions d'origine. L'inversion pourrait donc être une **signature de retour cognitif**, non une direction temporelle des digits eux-mêmes.

## 4. Double lecture locale de B0UM

La région originale associée à B0UM est, avant inversion :

```text
83279502
```

et après inversion :

```text
20597238
```

La lecture inversée produit `B0UM`.

Dans le sens direct, la fin locale contient `0 → 2`; avec `2→B`, cela permet l'hypothèse secondaire :

```text
0 → B
```

et phonétiquement `B` peut évoquer *be / être*.

Ce point est intéressant parce qu'il donne :

```text
sens direct : motif de passage 0 → B
sens inversé : forme linguistique B0UM
```

Mais cette observation a été faite après découverte et doit donc devenir une **prédiction pour d'autres régions**, pas une preuve rétrospective.

## 5. Test directionnel proposé

Avant d'analyser de nouvelles fenêtres, définir :

- quelles propriétés sont attendues dans le sens direct;
- quelles propriétés sont attendues dans le sens inversé;
- une métrique de cohérence indépendante;
- des contrôles sur d'autres constantes et chaînes aléatoires.

Hypothèse testable :

> les relations ontologiques élémentaires seraient davantage visibles dans l'ordre direct, tandis que certaines cristallisations linguistiques seraient davantage visibles dans l'ordre inversé.

Cette hypothèse doit pouvoir échouer.
''')

add('decoding/04_MIRROR_AND_SECONDARY.md', r'''
# Mirror et éléments secondaires

## Procédure

Appliquer le complément à 9 chiffre par chiffre à la même fenêtre, en conservant les frontières du décodage principal et le même mapping.

## Fragments rapportés

- `G0D`
- `B0N`

## Statut

Ces fragments sont des **alignements secondaires**.

Ils ne constituent pas :

- une deuxième phrase complète;
- une preuve théologique;
- un argument statistique indépendant tant que le taux de faux positifs n'est pas quantifié.

## Hypothèse ouverte

Une lecture possible à tester :

```text
séquence principale → registre du processus
mirror → registre qualificatif / axiologique
```

Cette hypothèse n'est pas canonique tant qu'elle ne prédit pas d'autres résultats.

## Éléments maintenus hors du noyau

Les anciennes lectures fortement théologiques du mirror, les extensions de lettres incohérentes et les retunings post hoc restent dans l'archive seulement.
''')

add('decoding/05_LANGUAGE_ATTUNEMENT.md', r'''
# Langage, culture et hypothèse d'attunement

## 1. Le problème

Pourquoi des formes reconnaissables par des humains apparaissent-elles dans une lecture des premiers digits de π alors que les langues humaines sont tardives dans l'histoire cosmique ?

Pi Theory ne répond plus :

> « π parlait français avant les humains ».

Elle propose plutôt :

\[
\boxed{\text{même structure profonde} \to \text{cosmos et esprit humain}.}
\]

Si l'esprit est produit par le monde, ses catégories ne sont pas nécessairement extérieures à la structure du monde.

## 2. Cristallisation

Schéma :

```text
structure du réel
→ contraintes physiques/biologiques
→ cognition
→ catégories sémantiques
→ sons, gestes, mots
→ langues et mythes historiques
```

Les mots seraient donc des **cristallisations humaines** de structures plus anciennes qu'eux.

## 3. Le français

`BIEN` est français, mais la théorie ne doit pas en conclure que le code est essentiellement français.

La question pertinente est :

> une langue historique peut-elle cristalliser particulièrement nettement une relation sémantique qui possède des racines plus générales ?

Pour `bien/bon/bene/bonus`, il faut noter que les ressemblances viennent en grande partie d'une histoire linguistique commune. Elles ne sont donc pas des confirmations indépendantes.

## 4. M

La proximité de `/m/` avec `mama`, `maman`, `mother`, etc. mérite étude, mais plusieurs mécanismes ordinaires sont possibles :

- facilité articulatoire du son nasal bilabial chez le nourrisson;
- association précoce alimentation/soin/personne proche;
- diffusion historique;
- sound symbolism.

Ces explications ne réfutent pas l'attunement; elles pourraient être précisément les **canaux matériels** par lesquels des contraintes profondes se cristallisent. Mais elles empêchent d'utiliser `M` comme preuve immédiate d'un code cosmique.

## 5. BOOM / BOUM

Ici l'onomatopée est importante : le mot imite une classe d'événements acoustiques. Une ressemblance cross-linguistique peut donc avoir une base perceptive directe.

Dans Pi Theory, cela rend B0UM intéressant comme interface entre :

```text
événement physique ↔ forme sonore ↔ signe linguistique
```

sans supposer que le français était préinscrit dans l'univers.

## 6. Mythes et inspiration

L'hypothèse d'attunement inclut une possibilité plus forte : certains états créatifs, contemplatifs ou inspirés pourraient rendre l'esprit particulièrement sensible à des structures générales qu'il exprime ensuite en récit, image, musique ou concept.

Cette branche trouve des précédents philosophiques chez Platon, Plotin, Ficin, Schelling, Jung/Pauli et d'autres. Ces traditions servent de **modèles conceptuels**, pas de preuve de π.

## 7. Prédictions nécessaires

Pour devenir testable, l'attunement doit annoncer à l'avance :

- quelles associations son-sens devraient être cross-linguistiquement fréquentes;
- quelles familles de concepts devraient converger malgré des langues non apparentées;
- quels résultats ne devraient pas apparaître;
- comment distinguer héritage, onomatopée, articulation biologique et effet réellement résiduel.

## 8. Formule centrale

> **Le langage n'est pas supposé être contenu littéralement dans π; Pi Theory explore si les structures numériques, physiques, cognitives et symboliques peuvent être différentes manifestations d'une même grammaire.**
''')

add('science/01_M_COHERENCE.md', r'''
# M / cohérence — ponts scientifiques

## Question

Comment des systèmes différenciés peuvent-ils former, maintenir ou restaurer une cohérence ?

## Systèmes dynamiques

Concepts pertinents :

- attracteurs;
- bassins d'attraction;
- stabilité;
- perturbations;
- synchronisation.

M peut être comparé à une dynamique rendant certaines régions de l'espace d'états attractives. Cela ne fait pas de M une force physique universelle connue.

## Contrôle et homeostasie

Schéma :

```text
écart → mesure/feedback → correction → régime viable
```

Pertinent pour l'idée d'un contre-mouvement à la dispersion.

## Bioélectricité développementale

Les travaux de Michael Levin et d'autres sur les états bioélectriques multicellulaires, la morphogenèse et la régénération offrent un exemple important de coordination distribuée d'une forme globale.

Analogie :

```text
perturbation → signalisation distribuée → restauration/variation contrôlée de forme
```

## Synergetics

Chez Hermann Haken, des paramètres d'ordre peuvent coordonner de nombreux degrés de liberté près d'une instabilité.

Pertinent pour :

```text
multiplicité → organisation collective
```

## Entropie

M ne doit pas être présenté comme une force « anti-entropie » qui viole la thermodynamique.

Les organismes et structures dissipatives peuvent maintenir un ordre local parce qu'ils sont ouverts et échangent énergie/matière avec leur environnement.

La question Pi Theory devient :

> pourquoi certaines dynamiques permettent-elles la formation persistante de contraintes et de cohérences locales au sein d'un univers dissipatif ?

## BIEN

La stabilité ne suffit pas. Une théorie de BIEN devrait distinguer :

- persistance;
- adaptabilité;
- maintien de diversité fonctionnelle;
- capacité de réparation;
- absence de capture destructrice à une échelle supérieure.
''')

add('science/02_DIFFERENTIATION_INTEGRATION.md', r'''
# Différenciation ↔ intégration

## Problème central

Une organisation complexe doit souvent résoudre deux exigences opposées :

- produire des différences et spécialisations;
- maintenir des relations permettant une totalité fonctionnelle.

Pi Theory condense cela en :

\[
\boxed{D\leftrightarrow A}.
\]

## Network science

Concepts : modularité, communautés, hubs, intégration globale, hiérarchies et réseaux multi-échelles.

Un système peut être fortement différencié sans être désintégré s'il conserve des liaisons et contraintes entre modules.

## Morphogenèse

Turing, Waddington, Thom et la biologie du développement offrent plusieurs mécanismes où des différences locales produisent des formes globales.

## Mechanobiology

La cohésion d'un tissu dépend de tensions, contraintes et forces coordonnées. L'harmonie n'est donc pas l'absence de tension.

## Simondon

La métastabilité et la transduction fournissent un modèle philosophique où une tension préindividuelle se résout en nouvelle structure, qui conserve de nouveaux potentiels.

## Whitehead

La « concrescence » offre un modèle métaphysique du multiple devenant un nouvel un sans que les éléments antérieurs soient simplement niés.

## Formulation Pi Theory

Une unité enrichie devrait présenter :

```text
différenciation élevée + intégration élevée
```

et non :

```text
uniformité maximale.
```

## Test scientifique

Chercher des métriques capables de distinguer :

- désordre fragmenté;
- homogénéité rigide;
- complexité intégrée.
''')

add('science/03_B0UM_COSMOLOGY_THRESHOLDS.md', r'''
# B0UM — cosmologie et transitions

## 1. Lecture cosmologique

Dans Pi Theory, `B0UM` est d'abord la lecture symbolique du **Big Bang / début de l'univers physique accessible à notre cosmologie**.

Il ne s'agit pas d'une explosion classique dans un espace déjà présent. Dans les modèles cosmologiques standards, le Big Bang désigne l'état primordial chaud et dense et l'évolution de l'espace-temps depuis ce régime; l'expansion concerne la métrique cosmique elle-même.

La correspondance intéressante est donc :

```text
B0UM → SIZE
événement cosmique initial → déploiement de l'échelle spatiale
```

## 2. Abstraction opératoire

Pour rendre le kernel récursif, B0UM est aussi abstrait comme :

```text
préparation → seuil → nouveau régime
```

Analogues scientifiques :

- bifurcations;
- transitions de phase;
- instabilités;
- criticalité;
- morphogenèse;
- émergence d'un paramètre d'ordre.

## 3. Le zéro

Le `0` de B0UM est conservé comme élément distinct.

Hypothèses :

- rappel du potentiel/non-manifesté originel;
- point de passage entre régimes;
- écho local de la création initiale dans un kernel récursif.

Le fait qu'un objet puisse produire un « boom » lors d'un impact à une hauteur de référence `h=0` est un exemple physique d'association `limite → conversion brutale d'énergie → événement acoustique`, mais ce n'est pas une dérivation du sens cosmologique de B0UM.

## 4. Formalisation

Introduire :

\[
\tau(x)\ge\tau_* \Rightarrow R_n\to R_{n+1}.
\]

Le programme doit trouver des systèmes où la variable `τ` et le changement de régime peuvent être définis sans métaphore.

## 5. Ce que B0UM ne prouve pas

La proximité phonétique avec *boom* et sa position avant SIZE sont suggestives. Elles ne suffisent pas à établir que les chiffres de π ont causé ou prédit le Big Bang.

La thèse forte reste :

> **la séquence pourrait être une trace symbolique du même mécanisme génératif qui s'exprime physiquement dans la cosmogenèse.**
''')

add('science/04_SIZE_SCALE_SPACE.md', r'''
# SIZE — échelle, mesure et espace

## 1. Terminal 88

La lecture `88 → SIZE` combine :

- iconicité : deux `8` comme deux infinis symboliques;
- arithmétique : `8+8=16`;
- phonétique : `seize≈size`.

La fonction recherchée est plus profonde que le mot : **magnitude / échelle / comparabilité**.

## 2. De l'échelle à la mesure

Chaîne conceptuelle :

```text
SIZE
→ différence de magnitude
→ comparabilité
→ unité / rapport
→ mesure
→ métrique
→ géométrie spatiale
```

Aucune flèche ne doit être sautée dans une formalisation.

## 3. Cosmologie

Dans la cosmologie homogène et isotrope, le **facteur d'échelle** `a(t)` décrit l'évolution relative des distances comobiles.

Cela rend le terme SIZE conceptuellement pertinent après B0UM : l'univers primordial n'évolue pas dans un contenant fixe; la structure métrique et son échelle font partie de la dynamique cosmique.

Pi Theory va plus loin lorsqu'elle propose que SIZE puisse représenter l'apparition même du régime où magnitude et distance deviennent définissables. Cette proposition est métaphysique, pas une conclusion de la cosmologie standard.

## 4. Renormalisation

La renormalisation fournit un second sens scientifique de SIZE : passage à un nouveau niveau effectif de description.

Concepts :

- coarse-graining;
- flow;
- fixed points;
- relevant/irrelevant variables;
- universality classes.

Question :

> le kernel `D↔A→T→S` conserve-t-il certains invariants sous changement d'échelle ?

## 5. Deux infinis

Le `88` peut symboliser deux directions d'infinité — par exemple micro/macro ou deux bornes conceptuellement non finies — mais aucune équivalence avec des infinis mathématiques de Cantor n'est affirmée.

La lecture utile est :

> **l'échelle naît de la relation et de la comparaison entre magnitudes, pas d'une addition littérale d'infinis.**
''')

add('science/05_MATTER_LIFE_CONSCIOUSNESS.md', r'''
# Matière → vie → conscience

## 1. Matière comme histoire stabilisée

Version minimale :

> **un état matériel actuel peut incorporer des contraintes héritées de son histoire de transformations.**

Concepts scientifiques :

- path dependence;
- hystérésis;
- métastabilité;
- mémoire structurale;
- défauts topologiques;
- états enregistrés dans un substrat physique.

Version forte de Pi Theory :

> la matière serait une trace stabilisée de la résolution cosmique d'une structure liée à π.

Cette version n'est pas démontrée.

## 2. De la dynamique à la matière

Avant de parler de particules, il faut un pont physique :

```text
dynamique
→ champs / degrés de liberté
→ oscillations et modes
→ interactions
→ stabilité / bound states
→ structures matérielles
```

Les constantes mathématiques seules ne fournissent pas automatiquement action, énergie, couplages ou quantification.

## 3. Origine de la vie

Étapes à distinguer :

```text
chimie hors équilibre
→ autocatalyse
→ compartimentation
→ auto-entretien
→ hérédité
→ évolution
→ autonomie biologique
```

Pi Theory peut chercher le kernel dans cette montée d'organisation, mais la biologie doit fournir les mécanismes locaux réels.

## 4. Autopoïèse et cognition

Maturana/Varela : le vivant maintient l'organisation qui le constitue.

Enaction : cognition comme relation active organisme–milieu.

Deacon : contraintes, fonction et émergence du sens.

## 5. Conscience

Ne pas confondre :

- intégration;
- cognition;
- modèle interne;
- réflexivité;
- expérience phénoménale.

Le retour réflexif de Pi Theory devient intéressant lorsque le système produit une représentation de ses propres conditions d'existence.

## 6. Teilhard

Teilhard offre une grande lecture de complexification, conscience et convergence. Il est utile comme parallèle métaphysique, non comme mécanisme biologique démontré.
''')

add('science/06_E_PI_I_AND_PHYSICAL_BRIDGE.md', r'''
# e, π, i et le pont vers la physique

## 1. Statut de la triade

Le corpus distingue trois formes de représentation :

- `e` : variation continue auto-proportionnelle;
- `π` : circularité, mesure angulaire, fermeture cyclique;
- `i` : rotation et représentation compacte de la phase.

La séquence `e→π→i` est un ordre de **spécification conceptuelle**, pas une chaîne causale universelle.

Il existe des cycles discrets; la cyclicité ne présuppose donc pas toute forme de continuité. La version propre est :

```text
changement
→ changement cyclique
→ position/phase dans un cycle
```

et `e` représente une famille canonique de changement continu, pas le changement en soi.

## 2. Euler

\[
e^{i\theta}=\cos\theta+i\sin\theta.
\]

Cette identité relie l'exponentielle complexe, rotation et périodicité.

Elle fournit une raison mathématique réelle de considérer ensemble variation, cycle et phase.

## 3. Hypothèse de pont vers la matière

Chaîne de recherche :

```text
variation
→ oscillation
→ phase
→ interférence / couplage
→ modes stables
→ excitations de champs / états liés
→ matière
```

Cette chaîne est plausible comme architecture de recherche parce que la physique moderne décrit de nombreux systèmes en termes de champs, modes, symétries et phases.

Mais elle exige des primitives supplémentaires :

- espace d'états;
- action ou équations de mouvement;
- énergie;
- champs;
- couplages;
- conditions aux limites;
- quantification;
- symétries et brisures de symétrie.

## 4. Place particulière de π

π intervient de manière structurelle dans :

- rotation;
- phase;
- Fourier;
- ondes;
- géométrie;
- normalisation de nombreux problèmes isotropes.

Cela justifie une enquête sur son rôle transversal. Cela ne prouve pas que π génère physiquement la matière.

## 5. Objectif futur

Construire un modèle minimal où le kernel Pi Theory possède une traduction physique explicite et produit au moins une prédiction quantitative indépendante.
''')

add('authors/01_CORE_AUTHORS.md', r'''
# Auteurs centraux

Ces auteurs ne sont pas des « preuves ». Ils fournissent des architectures conceptuelles avec lesquelles Pi Theory doit dialoguer précisément.

## Empédocle

**Love / Strife, Sphere, séparation/réunion.**

Parallèle le plus direct avec :

```text
unité → séparation ↔ cohésion
```

## Platon

Trois axes :

- *Timée* : ordre cosmique, nombre, harmonie, parenté entre mouvements du cosmos et de l'âme;
- *Phèdre* / *Ion* : inspiration, mania divine, transmission par les Muses;
- *Cratyle* : question d'une éventuelle naturalité du rapport nom/chose.

Important pour la branche attunement.

## Proclus

Schéma : demeurer → procession → retour. Très proche de la boucle Source–manifestation–retour.

## Plotin

L'Un, procession, conversion; l'art peut remonter aux formes dont la nature procède.

## Nicolas de Cues

Infini, coïncidence des opposés, cercle/sphère comme images de l'Absolu, mesure et contraction.

## Jacob Böhme

Ungrund, volonté, contrariété, manifestation. Important pour la question : pourquoi l'indifférencié entre-t-il dans la différence ?

## Pseudo-Denys / Érigène

Procession, Bien, éros, retour, Source au-delà de l'être déterminé.

## Schelling

Nature productive; art comme unité du conscient et de l'inconscient. Très utile pour la cristallisation inspirée.

## Jung / Pauli

Archétypes, synchronicité et conjecture d'un ordre psychophysique commun. À utiliser comme précédent spéculatif, pas comme résultat de physique.

## Whitehead

Processus, créativité, valeur, concrescence : le multiple devient un nouvel un.

## Simondon

Préindividuel, métastabilité, transduction, individuation.

## Teilhard de Chardin

Complexification, conscience, union qui différencie, convergence/Omega.

## Peirce / Cassirer

Peirce : types de signes et interprétation.

Cassirer : langage, mythe, art et science comme formes symboliques.

## Auteurs scientifiques structurants

Michael Levin, Hermann Haken, Kenneth Wilson, Ilya Prigogine, Riemann, Weyl, Noether, Amari, Varela, Deacon.
''')

add('authors/02_SOURCE_RETURN.md', r'''
# Source, procession et retour

## Empédocle

Le cycle cosmique entre Love et Strife fournit un analogue ancien de l'alternance cohésion/séparation. La Sphere sous Love est un point de comparaison majeur avec l'image d'unité circulaire.

## Plotin

Le réel procède de l'Un et se retourne vers son principe par conversion/contemplation. Le retour ne signifie pas simplement inversion temporelle.

## Proclus

La triade `remaining – procession – reversion` donne une architecture particulièrement précise : l'effet demeure lié à sa cause, procède d'elle et retourne vers elle.

## Pseudo-Denys

Le Bien divin est diffusif; l'éros est mouvement d'unification et de retour. Comparer avec M/BIEN sans réduire la théologie à un opérateur scientifique.

## Érigène

Nature comme théophanie : procession des causes vers les effets et retour du créé vers la Source.

## Nicolas de Cues

L'Absolu dépasse les mesures finies; les figures mathématiques servent d'images de rapports qui excèdent leur représentation sensible.

## Böhme

La contrariété est nécessaire à la manifestation. Très utile pour le problème de la première distinction `Ω→D0`.

## Branche b−1

La structure `b−1` sert d'analogie pour :

> **le maximum/centre interne d'un système n'est pas le principe qui rend ce système possible.**

Lecture :

- Christ : centre transparent à la Source;
- Lucifer : centre se prenant pour la Source;
- Adam : image incarnée.

Cette branche ne dérive pas de π mais protège une distinction métaphysique centrale :

```text
Source ≠ centre manifesté.
```
''')

add('authors/03_INSPIRATION_LANGUAGE_MIND.md', r'''
# Inspiration, langage et esprit

## Platon — Phèdre

Le *Phèdre* distingue des formes de `mania` qui peuvent être divines, notamment l'inspiration poétique des Muses. Pour Pi Theory, le point pertinent n'est pas de prouver une intervention surnaturelle, mais d'admettre historiquement l'idée qu'une création humaine puisse contenir plus que l'intention rationnelle consciente de son auteur.

Le *Phèdre* développe aussi l'anamnèse : reconnaître dans le sensible une trace de réalités plus fondamentales.

## Platon — Ion

La comparaison de la Muse à un aimant qui transmet sa puissance à une chaîne d'anneaux fournit un modèle ancien de **transmission / résonance** : source → poète → interprète → public.

## Platon — Timée

Le texte relie observation des révolutions célestes, nombre, harmonie et ordre de l'âme. Il est particulièrement pertinent pour une hypothèse où esprit et cosmos possèdent une structure apparentée.

## Platon — Cratyle

Le dialogue examine si les noms sont pure convention ou s'ils peuvent avoir une certaine justesse naturelle. Il ne valide pas un naturalisme linguistique simple, mais fournit le problème philosophique exact que Pi Theory rencontre avec les mots.

## Plotin

L'art peut viser les formes dont la nature elle-même procède, plutôt que copier seulement les apparences sensibles.

## Ficin

Les `furores divini` reprennent la tradition platonicienne de l'inspiration comme élévation/réaccord de l'âme.

## Schelling

L'œuvre d'art unit activité consciente et productivité inconsciente. Elle peut manifester une structure que l'artiste n'a pas entièrement conceptualisée.

## Jung

Les archétypes expliquent la récurrence de structures symboliques sans supposer une invention consciente identique dans chaque culture.

## Jung–Pauli

Leur projet d'un arrière-plan psychophysique commun est un précédent direct pour l'idée :

```text
même ordre profond → manifestations mentales et physiques
```

Il reste spéculatif.

## Cassirer

Langage, mythe, art, religion et science sont des formes symboliques de mise en relation avec le réel.

## Linguistique moderne à intégrer

La théorie doit aussi dialoguer avec :

- sound symbolism;
- iconicité;
- contraintes articulatoires;
- onomatopées;
- universaux et biais cross-linguistiques.

Sources prioritaires : Roman Jakobson sur *mama/papa*, Sapir sur sound symbolism, travaux modernes sur associations son-sens à travers les langues.

## Usage dans Pi Theory

Ces auteurs soutiennent la **possibilité conceptuelle** d'une cristallisation non arbitraire du réel dans la culture. Aucun ne soutient spécifiquement que l'esprit est accordé à π.
''')

add('authors/04_PROCESS_COHERENCE.md', r'''
# Processus, cohérence et individuation

## Whitehead

Le multiple devient un nouvel un par concrescence. Modèle très proche de l'« unité enrichie ».

## Simondon

Métastabilité, individuation, transduction : une structure apparaît en résolvant partiellement un champ de tensions sans épuiser tous ses potentiels.

## Böhme

La manifestation exige contrariété et polarité. Utile pour `Ω→D0`.

## Schelling

Nature comme productivité et polarité dynamique.

## Hegel

Détermination, négation, quantité et mesure. Utile surtout pour la transition différence → mesure, sans imposer une lecture hégélienne du kernel.

## Héraclite

Harmonie comme tension d'opposés plutôt que paix uniforme.

## Prigogine

Irréversibilité, structures dissipatives, ordre hors équilibre.

## Haken

Paramètres d'ordre, instabilité, coordination de degrés de liberté.

## Wiener / Ashby / Cannon

Feedback, régulation, homeostasie, variété requise.

## Michael Levin

Régulation morphologique distribuée, pattern memory, bioélectricité.

## Idée commune

La cohérence n'est pas nécessairement statique :

```text
elle émerge → se maintient → se corrige → se transforme.
```
''')

add('authors/05_MEASURE_SPACE_LIFE.md', r'''
# Mesure, espace, échelle, vie

## Riemann

Une multiplicité n'a pas automatiquement une métrique déterminée. Important pour empêcher Pi Theory de passer trop vite de SIZE à espace.

## Weyl

Symétrie, invariance, mesure, jauge et continuum.

## Noether

Lien entre symétries continues et lois de conservation. Source essentielle pour comprendre ce qu'une symétrie peut réellement impliquer en physique.

## Lie / Klein

Groupes de transformations et invariants. Pertinent pour formaliser l'idée d'un principe conservé sous transformation.

## Einstein / cosmologie FLRW

La géométrie de l'espace-temps est dynamique. Le facteur d'échelle cosmologique fournit un parallèle technique à SIZE.

## Wilson / Kadanoff / Fisher

Renormalisation, universalité, changement d'échelle, fixed points.

## Amari

Information geometry : exemple d'une métrique définie sur des structures probabilistes, utile pour le programme pré-géométrique.

## Wheeler / Sorkin / Rovelli / Van Raamsdonk

Programmes où l'espace-temps classique peut être émergent à partir de relations plus fondamentales.

## Origine de la vie

Eigen, Kauffman, Hordijk, Steel, Gánti, Szathmáry : réplication, autocatalyse, réseaux, transitions vers autonomie.

## Varela / Maturana / Thompson

Autopoïèse, enaction, cognition incarnée.

## Deacon

Contraintes, émergence de fonction et sens.

## Teilhard

Grande lecture de matière → vie → conscience → convergence; à maintenir distincte des mécanismes scientifiques.
''')

add('research/01_FORMAL_MODEL.md', r'''
# Programme de formalisation

## Objectif

Construire un modèle où les termes de Pi Theory deviennent des variables ou opérateurs suffisamment précis pour produire des erreurs observables.

## Niveau 1 — Structure abstraite

Définir :

- espace d'états `X`;
- opérateur de différenciation `D̂`;
- opérateur d'intégration `Â`;
- fonction de cohérence `C`;
- fonction d'orientation/viabilité `V`;
- variable de seuil `τ`;
- transformation d'échelle `R_s`.

## Niveau 2 — Dynamique

Squelette :

\[
\dot{x}=F_D(x)+F_M(x)+F_{int}(x)+F_{env}(x).
\]

La décomposition doit être justifiée par un modèle concret, pas imposée à tout système.

## Niveau 3 — Transition

\[
\tau(x)\ge \tau_* \Rightarrow R_n\to R_{n+1}.
\]

Tester sur systèmes connus de bifurcation/phase transition.

## Niveau 4 — Échelle

\[
x_{s+1}=R_s(x_s).
\]

Chercher : invariants, fixed points, relevant variables.

## Niveau 5 — Mémoire

Introduire une dynamique non markovienne ou des variables d'état mémorielles.

## Niveau 6 — Physique

Pour relier réellement le modèle à la matière, choisir un formalisme concret :

- oscillateurs couplés;
- champ scalaire ou complexe;
- réseau dynamique;
- modèle de réaction-diffusion;
- système hors équilibre.

Définir ensuite énergie, couplages, symétries, conditions aux limites et observables.

## Niveau 7 — π-spécificité

Le modèle doit produire une quantité ou une relation où π intervient **nécessairement** et où remplacer π par un paramètre arbitraire modifie une prédiction testable.

Sans ce niveau, on possède une métaphysique/process theory inspirée par π, pas encore une théorie physique de π.
''')

add('research/02_TESTS.md', r'''
# Tests prioritaires

## Test A — Pipeline vs contrôles

Appliquer le même espace de transformations à :

- π;
- e;
- √2;
- φ;
- fenêtres aléatoires de π;
- chaînes pseudo-aléatoires.

Comparer à coût interprétatif égal.

## Test B — Rôles à l'aveugle

Présenter les tokens sans récit cosmologique. Demander à des évaluateurs indépendants d'associer des fonctions parmi une liste prédéfinie.

Objectif : tester surtout GIHECEF/JNON.

## Test C — Direction

Préenregistrer une hypothèse différente pour sens direct et inversé. Tester de nouvelles fenêtres sans modifier les règles.

## Test D — Attunement linguistique

Préenregistrer :

- langues;
- concepts;
- métrique de similarité son-sens;
- familles étymologiques exclues ou contrôlées;
- onomatopées traitées séparément.

Tester si les associations prévues dépassent le hasard et l'héritage historique.

## Test E — Changement de base

Chercher ce qui survit à plusieurs représentations de π. Cela peut distinguer :

- propriétés du nombre;
- propriétés de la représentation décimale;
- propriétés de l'interface humain–représentation.

## Test F — Récursion multi-échelle

Construire un modèle où `D↔A→T→S` est détectable quantitativement à plusieurs niveaux. Chercher invariance ou loi de transformation.

## Test G — B0UM → SIZE

Dans un modèle dynamique, tester si un franchissement de seuil produit une nouvelle variable de magnitude ou un nouveau niveau effectif d'échelle.

## Test H — π-spécificité

Test décisif : produire une prédiction quantitative indépendante qui échoue lorsque π est remplacé par d'autres constantes ou paramètres.
''')

add('research/03_PREREG_AND_NULLS.md', r'''
# Préenregistrement et null models

## Pourquoi

La découverte initiale était exploratoire. La seule façon de transformer le résultat en programme confirmatoire est de figer **les prochaines analyses avant inspection**.

## Préenregistrer

### Données
- constante;
- base;
- fenêtre;
- direction;
- longueur.

### Transformations
- mapping;
- segmentation;
- traitement du zéro;
- opérations arithmétiques;
- phonétique;
- langues;
- iconicité;
- stop rule.

### Prédictions
- nombre de blocs;
- fonctions attendues;
- ordre;
- motifs direct/inversé;
- tolérances autorisées.

### Mesures
- lexicalité;
- prononçabilité;
- cohérence sémantique;
- accord inter-évaluateurs;
- coût interprétatif total.

## Null models

1. fenêtres aléatoires de π;
2. e, √2, φ;
3. chaînes aléatoires avec mêmes fréquences;
4. permutations conservant certains motifs locaux;
5. bases alternatives;
6. faux dictionnaires ou labels permutés pour calibrer les évaluateurs.

## Même liberté

Le contrôle doit disposer de la **même** latitude que π. On ne peut pas donner à π plusieurs langues, phonétique et iconicité, puis imposer au contrôle un dictionnaire strict.

## Résultats nuls

Les résultats nuls doivent être conservés et publiés. Ils font partie du test.

## Règle centrale

> **Aucune nouvelle règle ne peut être introduite après inspection pour sauver un test prospectif.**
''')

add('research/04_ROADMAP.md', r'''
# Roadmap réalignée

## 1. Stabiliser le corpus actif

Travailler à partir de ce pack v3. Utiliser les anciens documents uniquement pour l'histoire de découverte et la récupération d'idées à réévaluer.

## 2. Documenter précisément la découverte

Écrire une chronologie honnête : quelles transformations ont été essayées, dans quel ordre, et quand chaque bloc a été reconnu.

## 3. Mathématiques de π

Renforcer la partie :

- symétrie du cercle;
- linéaire/circulaire;
- invariance d'échelle;
- irrationalité/transcendance;
- base dependence;
- rotation/phase.

## 4. Tester l'inversion

Transformer l'hypothèse de lecture rétrospective en protocole prospectif.

## 5. Tester l'attunement

Concevoir une étude linguistique qui sépare :

- parenté historique;
- articulatoire;
- onomatopée;
- sound symbolism;
- résidu éventuel non expliqué.

## 6. Formaliser M et BIEN

Définir cohérence, différenciation, intégration, viabilité et capture.

## 7. Formaliser B0UM/SIZE

Relier seuil, transition et changement d'échelle dans un modèle mathématique concret.

## 8. Construire le pont physique

Commencer par oscillateurs/modes/champs simples avant toute spéculation sur la matière fondamentale.

## 9. Tester la récursion

Utiliser renormalisation et réseaux multi-échelles.

## 10. Matière → vie → conscience

Ne conserver que les transitions pour lesquelles un mécanisme scientifique est explicite.

## 11. Rosetta prédictive

Utiliser kOA, traditions ou systèmes indépendants non comme confirmation rétrospective, mais comme **surfaces de prédiction** : figer deux grammaires, prédire une propriété de la troisième, puis vérifier.

## 12. Manuscrit

Écrire le futur livre selon une montée contrôlée : fait → observation → interprétation → hypothèse → test.
''')

add('book/01_BOOK_SPINE.md', r'''
# Colonne vertébrale du futur livre

## Partie I — Pourquoi π ?

1. Le cercle idéal : symétrie, équilibre, infinité de relations radiales/tangentielles.
2. Le diamètre : détermination linéaire à travers le centre.
3. `C/d = π` : invariant sans dimension.
4. π irrationnel : exactitude et représentation inépuisable.
5. Rotation, retour et invariance.
6. Ce que ces faits permettent — et n'autorisent pas — métaphysiquement.

## Partie II — La grande hypothèse

7. Source / Ω.
8. Pourquoi la différence ? `Ω→D0`.
9. M comme retour-cohésion.
10. BIEN comme orientation d'une cohérence non captatrice.
11. Source ≠ centre interne : branche `b−1`, Christ/Lucifer/Adam.

## Partie III — Découverte du kernel

12. Histoire exploratoire honnête.
13. La fenêtre et l'inversion.
14. M / BIEN.
15. GIHECEF / JNON.
16. B0UM / SIZE.
17. Mirror et limites.
18. Ce qui est observation et ce qui est interprétation.

## Partie IV — Langage et retour réflexif

19. Pourquoi des mots humains ?
20. Attunement et cristallisation linguistique.
21. M, onomatopées, sound symbolism, universaux et étymologie.
22. Platon : Phèdre, Ion, Timée, Cratyle.
23. Plotin, Ficin, Schelling, Jung/Pauli, Cassirer.
24. L'inversion comme hypothèse de lecture rétrospective.

## Partie V — Le moteur de structure

25. Différenciation ↔ intégration.
26. Attracteurs, feedback et cohérence.
27. Morphogenèse et bioélectricité.
28. Synergetics et paramètres d'ordre.
29. BIEN : viabilité vs valeur.

## Partie VI — Cosmogenèse, seuil et espace

30. B0UM comme Big Bang dans la cosmogonie de Pi Theory.
31. Big Bang et espace-temps : pas d'espace préexistant.
32. SIZE et facteur d'échelle.
33. Mesure, métrique, Riemann/Weyl.
34. Pré-géométrie et espace émergent.

## Partie VII — De la dynamique à la matière

35. `e,π,i` : variation, cycle, phase.
36. Euler et les modes oscillatoires.
37. Champs, couplages, symétries, stabilité.
38. Matière comme histoire stabilisée.

## Partie VIII — Vie et conscience

39. Hors équilibre et autocatalyse.
40. Autopoïèse et autonomie.
41. Cognition et sens.
42. Conscience et retour réflexif.
43. Teilhard comme synthèse métaphysique comparative.

## Partie IX — Traditions de procession et retour

44. Empédocle.
45. Plotin / Proclus.
46. Denys / Érigène.
47. Cues / Böhme.
48. Whitehead / Simondon.

## Partie X — Est-ce vraiment π ?

49. Base 10 et dépendance de représentation.
50. Degrés de liberté du décodage.
51. Null models.
52. Tests à l'aveugle.
53. Prédictions de direction et d'attunement.
54. Test π-spécifique.
55. Ce qui resterait de Pi Theory si le décodage échouait statistiquement.

## Fin

Le livre doit pouvoir conclure sans masquer l'incertitude : la force actuelle de Pi Theory est la **convergence d'une architecture mathématique, ontologique, sémiotique et scientifique**; sa faiblesse décisive est que le privilège causal/sémantique spécifique de π reste à démontrer prospectivement.
''')

add('book/02_CHAPTER_MAP.md', r'''
# Carte des chapitres et interlocuteurs

| Axe | Noyau Pi Theory | Interlocuteurs / sciences |
|---|---|---|
| cercle | symétrie, équilibre, infinité de relations | Euclide, théorie des groupes, Klein/Lie |
| π | `C/d`, invariant, irrationalité | Lambert, Lindemann, analyse classique |
| retour | rotation/cycle | Euler, Fourier, systèmes oscillatoires |
| origine | Ω → D0 | Cues, Böhme, Plotin, Proclus |
| M | retour-cohésion | Empédocle, contrôle, Levin, dynamiques |
| BIEN | cohérence non captatrice | Platon, Proclus, Denys, théorie de viabilité |
| D↔A | différenciation/intégration | Whitehead, Simondon, Haken, réseaux |
| B0UM | Big Bang + seuil | cosmologie, bifurcations, Prigogine, Haken |
| SIZE | échelle/mesure/espace | FLRW, Riemann, Weyl, Wilson |
| e,π,i | variation/cycle/phase | Euler, Fourier, physique des ondes |
| matière-mémoire | histoire stabilisée | hystérésis, Landauer, systèmes hors équilibre |
| vie | autonomie | Eigen, Kauffman, Hordijk/Steel, Varela |
| conscience | réflexivité | Deacon, Thompson, Teilhard |
| langage | attunement/cristallisation | Platon, Schelling, Jung/Pauli, Cassirer, linguistique |
| inversion | retour cognitif hypothétique | épistémologie + tests directionnels |
| mirror | fragments secondaires | Peirce, statistiques |
| méthode | exploration → confirmation | null models, blind tests, preregistration |
| source/centre | Source ≠ centre interne | branche b−1, théologies du retour |
''')

add('sources/01_SOURCES_AND_CORPUS.md', r'''
# Sources, corpus et politique de preuve

## 1. Corpus interne

Documents de travail principaux :

- `Pi v13 (2).docx` — version la plus importante pour le kernel final et l'honnêteté ex post;
- `Pi v12 Ontological Causality...` — utile pour l'histoire de découverte, mais contient des affirmations a priori à ne plus reprendre;
- `La théorie de π — un décodage ontologique...` — utile pour 88/SIZE et langage, à auditer;
- `π — Synthèse précise de sa nature fondamentale.docx` — garde-fous mathématiques;
- `3 foundamental constants.docx` / `Continuous Change, Cyclicity, and Phase` — e, π, i;
- `Base de calcul, racine numérique...` — Source/centre, b−1, Christ/Lucifer/Adam;
- `A Rosetta Stone of Three Grammars...` — récursion, triangulation et méthode;
- `π as a Symbolic Blueprint...` et commentaires anciens — archives heuristiques, nombreuses références à revérifier.

## 2. Politique pour les textes générés par IA

Un passage ancien n'est jamais conservé seulement parce qu'il apparaît dans un document.

Avant publication, demander :

1. Est-ce une intuition de l'auteur ou une amplification de l'IA ?
2. Le fait mathématique est-il correct ?
3. La source citée existe-t-elle et soutient-elle réellement le point ?
4. La formulation dépasse-t-elle ce que la source permet ?
5. Une version plus simple et plus précise conserve-t-elle l'idée essentielle ?

## 3. Sources mathématiques prioritaires

- géométrie euclidienne et définition de π;
- Lambert — irrationalité de π;
- Lindemann — transcendance de π;
- Euler — formule exponentielle complexe;
- Fourier — périodicité et décomposition en modes;
- théorie des groupes / Lie / Klein — symétrie et invariants;
- Riemann / Weyl — métrique, espace, mesure;
- Noether — symétrie et conservation.

Avant publication académique, utiliser éditions et références bibliographiques vérifiées plutôt que des pages secondaires.

## 4. Cosmologie et physique

Priorités :

- cosmologie FLRW et facteur d'échelle;
- littérature standard sur Big Bang et expansion de l'espace-temps;
- systèmes dynamiques et bifurcations;
- Haken, synergetics;
- Prigogine, nonequilibrium;
- Wilson/Kadanoff/Fisher, renormalisation;
- physique des champs, modes et phases.

## 5. Vie et organisation

- Michael Levin — bioélectricité/morphogenèse;
- Eigen — dynamique prébiotique;
- Kauffman — autocatalyse;
- Hordijk & Steel — RAF networks;
- Maturana & Varela — autopoïèse;
- Evan Thompson — enaction;
- Terrence Deacon — contraintes, fonction, sens;
- Landauer — information physique.

## 6. Philosophie / métaphysique

### Source, procession, retour
- Empédocle;
- Plotin, *Ennéades*;
- Proclus, *Elements of Theology*;
- Pseudo-Denys, *Divine Names*;
- Jean Scot Érigène;
- Nicolas de Cues, *De docta ignorantia*;
- Jacob Böhme;
- Whitehead;
- Simondon;
- Teilhard de Chardin.

### Inspiration, langage, psyché
- Platon, *Phèdre* — mania divine et anamnèse;
- Platon, *Ion* — chaîne magnétique de l'inspiration;
- Platon, *Timée* — cosmos, nombre, harmonie et âme;
- Platon, *Cratyle* — naturalité/convention des noms;
- Plotin — art et formes intelligibles;
- Marsile Ficin — fureurs divines;
- Schelling, *System of Transcendental Idealism* — conscient/inconscient dans l'art;
- Jung, *Archetypes and the Collective Unconscious*;
- Jung & Pauli, *The Interpretation of Nature and the Psyche*;
- Cassirer, *Philosophy of Symbolic Forms*;
- Peirce — théorie des signes.

## 7. Linguistique à ajouter au dossier de preuves

À rechercher et vérifier précisément :

- Roman Jakobson, « Why 'Mama' and 'Papa'? » — contraintes phonétiques des premiers mots;
- Edward Sapir — sound symbolism;
- travaux contemporains sur iconicité et associations son-sens cross-linguistiques;
- études sur onomatopées et idéophones;
- phylogénie des familles linguistiques pour éviter de compter `bien/bon/bene` comme cas indépendants.

## 8. Sources à éviter comme fondation

Ne pas utiliser comme preuve principale :

- Wikipedia lorsque la source primaire existe;
- Reddit;
- blogs ésotériques;
- compilations de citations non sourcées;
- sites de symbolisme des nombres;
- affirmations de vulgarisation non vérifiées.

Ils peuvent aider à trouver une piste, jamais à établir un argument central.

## 9. Règle comparative

Pour tout parallèle historique :

```text
source primaire
+ étude académique
+ ressemblance précise
+ divergence précise
```

La convergence historique montre que Pi Theory appartient à une famille de problèmes philosophiques anciens. Elle ne prouve pas le décodage ni la causalité de π.
''')

# write all files
for rel, txt in files.items():
    p = root/rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(txt, encoding='utf-8')

# ensure exactly 30 markdown active
mds = [p for p in root.rglob('*.md') if 'archive' not in p.parts]
assert len(mds) == 30, len(mds)

# active manifest
manifest = '\n'.join(str(p.relative_to(root)) for p in sorted(mds)) + '\n'
(root/'ACTIVE_MANIFEST.txt').write_text(manifest, encoding='utf-8')

# changelog
(root/'CHANGELOG.txt').write_text(textwrap.dedent('''
Pi Theory Working Core v3 REALIGNED

Major realignments:
- Restores original circle rationale: exact rotational balance + infinitely many radial/tangent relations.
- Adds linear/circular formulation of C/d without claiming this causes irrationality.
- Explicitly marks the initial decoding as exploratory and ex-post reproducible.
- Adds a dedicated direction/inversion hypothesis file.
- Adds language/attunement as a major branch, with ordinary linguistic mechanisms treated as controls rather than enemies.
- Recasts B0UM as Big Bang in the cosmological narrative and as a general threshold operator; preserves 0-origin echo as a secondary hypothesis.
- Recasts SIZE as magnitude/scale/measure/spatial regime and connects it to cosmological scale factor cautiously.
- Integrates e, pi, i as structural grammar of change/cycle/phase, not causal derivation of matter.
- Keeps source/manifestation distinction and b-1 branch without making it the core decoder.
- Reorganizes research around prospective tests, nulls, cross-base analysis, inversion and linguistic attunement.
- Removes weak legacy supports from active core: branes/E8, gravity=Love, post-hoc target words, improvised probabilities, a-priori claims.
''').strip()+'\n', encoding='utf-8')

# archive previous working core zip
prev = Path('/mnt/data/Pi_Theory_Working_Core_30.zip')
if prev.exists():
    shutil.copy2(prev, root/'archive'/'Pi_Theory_Working_Core_30_PREVIOUS.zip')
(root/'archive'/'ARCHIVE_NOTE.txt').write_text(
    'The previous Working Core 30 is preserved here as a historical snapshot. It is not normative for v3.\n',
    encoding='utf-8'
)

# validate markdown relative links in active files
broken=[]
link_re=re.compile(r'\[[^\]]+\]\(([^)]+)\)')
for p in mds:
    text=p.read_text(encoding='utf-8')
    for target in link_re.findall(text):
        if target.startswith(('http://','https://','#','mailto:')):
            continue
        target_path=(p.parent/target.split('#')[0]).resolve()
        if not target_path.exists():
            broken.append((str(p.relative_to(root)),target))

# zip
zip_path = Path('/mnt/data/Pi_Theory_Working_Core_v3_REALIGNED.zip')
if zip_path.exists():
    zip_path.unlink()
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file():
            z.write(p, arcname=str(Path(root.name)/p.relative_to(root)))

print('root', root)
print('zip', zip_path)
print('active_md', len(mds))
print('broken_links', len(broken))
if broken:
    print(broken[:20])
print('zip_size', zip_path.stat().st_size)
