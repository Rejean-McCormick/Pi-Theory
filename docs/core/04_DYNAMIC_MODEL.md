# Minimal Dynamic Model

## 1. State dynamics

Let `x(t)` denote the state of a system.

A minimal decomposition is:

```text
dx/dt = F_D(x) + F_M(x)
```

`F_D` represents processes that increase differentiation. `F_M` represents processes that increase some form of integration or coherence.

## 2. Candidate observables

Possible system-level variables include:

```text
D(x) = differentiation
I(x) = integration
V(x) = viability or functional persistence
C(x) = coherence
```

A future harmony measure might have the form:

```text
H(x) = f(D(x), I(x), V(x))
```

No canonical function has yet been established.

## 3. Threshold

`B0UM` can be represented abstractly as:

```text
if tau(x) >= tau_star:
    x -> new_regime(x)
```

The meaning of `tau` depends on the scientific domain: instability, control parameter, criticality, energetic barrier, network transition, or another measurable variable.

## 4. Scale transition

`SIZE` suggests coarse-graining or scale change:

```text
x_(s+1) = R_s(x_s)
```

The research question is whether any functional relation survives the transformation `R_s` as an invariant, fixed point, or universality pattern.

## 5. Memory

Matter-as-memory can be modeled weakly through path dependence:

```text
x(t) depends on prior states, constraints, or internal memory variables
```

This is compatible with hysteresis, metastability, structural inheritance, and physical memory. It does not by itself establish a pi-specific mechanism.

## 6. Recursive return

A generic cycle is:

```text
U_n -> D_n -> A_n -> U_(n+1)
```

A residual formulation is:

```text
U_(n+1) = integrate(D_n) + epsilon_n
```

The symbol `epsilon_n` is provisional. It denotes irreducible difference, not measurement error unless a future model defines it that way.
