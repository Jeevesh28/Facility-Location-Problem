# Facility Location Problem 🏭

## Problem Statement 🎓	
The **Uncapacitated Facility Location Problem (UFLP)** is the problem of finding the optimal placement of facilities of unrestricted capacities among potential facility **(m)** locations such that the cost of satisfying demands of all the customers **(n)** is minimized. Here, cost is of two types: 
* **(c):** the service or connection cost  to provide service to a customer by a facility
* **(f):** the opening cost to open a facility

UFLP is also known as the Simple Plant Location Problem (SPLP) or the Warehouse Location Problem (WLP). UFLP is known to be an **NP-hard problem**.

## Initialising Customers and Facility with Random Coordinates 🏁	
![Figure](https://i.imgur.com/bFHI1JT.png)

## Undisrupted Uncapacitated Facility Location Problem ⏩
**Cost Function:** 

* *Customer:* `I = [i for i in range(0, n)]` 
* *Facility:* `J = [i for i in range(0, m)]` 
* *Demand of Customer:* `h = {i: rnd.randint(1, 10) for i in I}`
* *2-D cartesian product:* `A = [(i, j) for i in I for j in J]` 
* *Fixed setup cost of Facility:* `f = {j: 100 for j in J}`
* *Cost to reach customer from Facility:* `c = {(i, j): 1*np.hypot(xc[i]-xf[j], yc[i]-yf[j]) for (i, j) in A}`

**Result:**

![Undisrupted Uncapacitated Facility Location](https://i.imgur.com/C33C0cO.png)

## Disrupted Uncapacitated Facility Location Problem ▶️
**Cost Function:** 
* *High penalty for disrupted facility:* `max_disruption = 10000`
* *Customer:* `I = [i for i in range(0, n)]` 
* *Facility:* `J = [i for i in range(0, m)]` 
* *Demand of Customer:* `h = {i: rnd.randint(1, 10) for i in I}`
* *2-D cartesian product:* `A = [(i, j) for i in I for j in J]` 
* *Fixed setup cost of Facility:* `f = {j: 100 for j in J}`
* *Cost to reach customer from Facility:* `c = {(i, j): 1*np.hypot(xc[i]-xf[j], yc[i]-yf[j]) for (i, j) in A}`
* *Penalty due to disruptions:* `p = {j: rnd.choice(np.array((0, max_disruption // 4, max_disruption // 2, max_disruption)), p=[0.5, 0.25, 0.15, 0.1])`

**Result:**

![Disrupted Uncapacitated Facility Location Problem](https://i.imgur.com/fF6HqRW.png)
