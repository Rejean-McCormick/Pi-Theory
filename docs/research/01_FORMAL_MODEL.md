# Formalization Program

## Goal

Translate the vocabulary of Pi Theory into variables, operators, and measurable relations that can produce observable error when the theory is wrong.

## Core state model

```text
dx/dt = F_D(x) + F_M(x)
```

where differentiation and integration/coherence are modeled separately.

## Candidate dimensions

```text
D = differentiation
I = integration
C = coherence
V = viability
S = scale
T = transition indicator
```

## Threshold model

```text
if tau(x) >= tau_star:
    regime_n -> regime_n+1
```

## Multi-scale map

```text
x_(s+1) = R_s(x_s)
```

Research should ask whether the same functional relations recur under coarse-graining.

## Pi-specific requirement

A generic complex-systems model is not enough. The formal program must eventually define `H_pi`: a consequence that changes when pi is replaced by e, sqrt(2), phi, or matched random controls.
