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
