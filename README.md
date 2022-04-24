# Facility Location Problem

Mixed-integer programming models for deciding where to open facilities and which customers each one serves, solved with Gurobi. Covers the uncapacitated problem, a disruption-aware variant where facilities can fail, and a capacitated solver for benchmark instances.

**Stack:** Python · GurobiPy · NumPy · Matplotlib

---

## Problem

Given *m* candidate facility sites and *n* customers, choose which facilities to open and assign every customer to an open facility, minimizing:

- **opening cost** *f<sub>j</sub>* for each facility opened, plus
- **service cost** *c<sub>ij</sub>* for serving customer *i* from facility *j*, weighted by demand.

The **Uncapacitated Facility Location Problem (UFLP)**, also called the Simple Plant Location Problem or Warehouse Location Problem, is NP-hard, which is why it's solved as a MIP rather than by enumeration.

## Formulation

With binary *y<sub>j</sub>* (open facility *j*) and *x<sub>ij</sub>* (customer *i* served by *j*):

```
minimize    Σ_j f_j · y_j  +  Σ_i Σ_j h_i · c_ij · x_ij
subject to  Σ_j x_ij = 1           for every customer i   (each customer served once)
            x_ij ≤ y_j             for every i, j         (only open facilities serve)
            x_ij, y_j ∈ {0, 1}
```

The capacitated variant adds `Σ_i h_i · x_ij ≤ capacity_j · y_j` for each facility.

## Experiments

### 1. Uncapacitated, no disruptions

Customers and candidate facilities are placed at random coordinates. Demand *h<sub>i</sub>* is a random integer from 1 to 10, every facility costs 100 to open, and service cost is Euclidean distance.

![Customers and candidate facilities](https://i.imgur.com/bFHI1JT.png)

![Optimal solution without disruptions](https://i.imgur.com/C33C0cO.png)

### 2. Uncapacitated, with disruptions

Each facility gets a random disruption penalty *p<sub>j</sub>* added to its cost, drawn from {0, 2,500, 5,000, 10,000} with probabilities {0.5, 0.25, 0.15, 0.1}. The model now trades distance against reliability: it avoids facilities likely to fail even when they are closer.

![Optimal solution with disruptions](https://i.imgur.com/fF6HqRW.png)

### 3. Capacitated benchmark instances

`solve.py` reads instance files (facility count, customer count, then setup cost, capacity and coordinates per facility, and demand and coordinates per customer) and solves the capacitated problem with Gurobi. Instances of different sizes are in `data/`.

## Running it

A Gurobi license is required (free academic licenses are available).

```bash
pip install gurobipy numpy matplotlib
jupyter notebook "UFLP (with and without Disruptions).ipynb"   # experiments 1 and 2
python solve.py data/fl_16_1                                    # experiment 3
```

## Repository layout

```
UFLP (with and without Disruptions).ipynb   uncapacitated models and plots
solve.py                                    capacitated solver for instance files
data/                                       benchmark instances (fl_<facilities>_<id>)
```
