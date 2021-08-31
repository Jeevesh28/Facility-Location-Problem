# Facility Location Problem 
import sys
from collections import namedtuple
import math
from gurobipy import *

# Tuples storing variables
Point = namedtuple("Point", ['x', 'y'])
Facility = namedtuple("Facility", ['index', 'setup_cost', 'capacity', 'location'])
Customer = namedtuple("Customer", ['index', 'demand', 'location'])

# Distance between points
def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def solve_it(input_data):
    # Parse the input file data
    lines = input_data.split('\n')

    # Read facility and customer count on 1st line of input file
    parts = lines[0].split()
    facility_count = int(parts[0])
    customer_count = int(parts[1])
    
    # Storing Facility parameters
    facilities = []
    for i in range(1, facility_count + 1):
        parts = lines[i].split()
        facilities.append(Facility(i - 1, float(parts[0]), int(parts[1]), Point(float(parts[2]), float(parts[3]))))

    # Storing Customer parameters
    customers = []
    for i in range(facility_count + 1, facility_count + customer_count + 1):
        parts = lines[i].split()
        customers.append(Customer(i - 1 - facility_count, int(parts[0]), Point(float(parts[1]), float(parts[2]))))

    # Build minimisation model
    m = Model()
    
    x = {}
    y = {}
    d = {}

    # Building cost function
    for j in range(facility_count): 
    	x[j] = m.addVar(vtype = GRB.BINARY, name="x%d" % j)
    
    for i in range(customer_count): 
    	for j in range(facility_count): 
    		y[(i,j)] = m.addVar(vtype = GRB.BINARY, name="y%d,%d" % (i,j)) 
    		d[(i,j)] = length(customers[i][2], facilities[j][3]) 
    m.update() 
    
    # Add constraints
    for i in range(customer_count): 
    	m.addConstr(quicksum(y[(i,j)] for j in range(facility_count)) == 1)

    for i in range(customer_count): 
    	for j in range(facility_count): 
    		m.addConstr(y[(i,j)] <= x[j]) 
    
    for j in facilities: 
    	m.addConstr(quicksum(y[(i.index,j.index)] * i.demand for i in customers) <= j.capacity) 
    
    # GRB minimize cost function
    m.setObjective(quicksum(facilities[j].setup_cost * x[j] + quicksum(d[(i,j)] * y[(i,j)] for i in range(customer_count)) for j in range(facility_count)), GRB.MINIMIZE) 
    m.optimize()

    # Calculate the cost of the solution
    obj = sum([f.setup_cost*x[f.index] for f in facilities])
    solution = []
    
    for pair in y:
        obj += length(customers[pair[0]].location, facilities[pair[1]].location) * y[(pair[0], pair[1])]
    
    for c in customers:
        for f in facilities:
            if y[(c.index,f.index)].X == 1:
                solution.append(f.index)
    print('Customer to Facility mapping:')
    return solution

if __name__ == '__main__':
    
    # Accessing input file from data folder
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    
    else:
        print('Input file missing. Select one from the data directory. (i.e. python solve.py ./data/fl_3_1)')