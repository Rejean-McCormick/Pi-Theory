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

## Niveau 7 — Retour, résidu et cycles

Pour un cycle `n`, définir un état de départ manifesté `U_n` et un opérateur de retour `Q_n`. Si une distance `d` existe :

\[
arepsilon_n=d(Q_n(U_n),U_n).
\]

Tester ensuite si `ε_n` prédit objectivement :

- un changement de régime;
- une nouvelle échelle;
- une propriété du cycle suivant.

Un modèle valide doit permettre `ε_n=0` aussi bien que `ε_n>0`; Pi Theory ne doit pas imposer le résidu par définition.

## Niveau 8 — π-spécificité

Le modèle doit produire une quantité ou une relation où π intervient **nécessairement** et où remplacer π par un paramètre arbitraire modifie une prédiction testable.

Sans ce niveau, on possède une métaphysique/process theory inspirée par π, pas encore une théorie physique de π.
