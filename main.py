import os
import pandas as pd
import sqlite3


# Connect to the SQLite database
conn = sqlite3.connect("Employee.db")

# Path to the folder containing CSV files
folder_path = "Relations"

# Iterate through all files in the folder
for COMP4522ASSIGNMENT2 in os.listdir(folder_path):
    # Check if the file is a CSV file
    if COMP4522ASSIGNMENT2.endswith(".csv"):
        # Construct the full path to the CSV file
        csv_file_path = os.path.join(folder_path, COMP4522ASSIGNMENT2)
        
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Extract table name from file name (remove file extension)
        table_name = os.path.splitext(COMP4522ASSIGNMENT2)[0]
        
        # Write the DataFrame to the SQLite database
        df.to_sql(table_name, conn, if_exists="replace", index=False)

# Commit changes to the database
conn.commit()

###############################################################

# QUERIES

# Q1: Are there any employees that are "female" and that work in project
# "computerization" with an effort of "10" hours per week, and that have
# "jennifer" as a supervisor? If so, list them.
ans1 = pd.read_sql_query("SELECT e.employee_name FROM employee e JOIN female f ON e.employee_name = f.name JOIN workson a ON e.employee_name = a.name JOIN supervise z ON e.employee_name = z.subordinate AND z.supervisor= 'jennifer' AND a.project = 'computerization' AND a.effort = '10' ", conn)

# Q2: Who is the employee who makes over "40000" dollars a year and
# works for the "research" department?
ans2 = pd.read_sql_query("SELECT e.employee_name FROM employee e JOIN department d ON e.employee_name = d.employee_name JOIN salary o ON e.employee_name = o.employee_name WHERE o.salary > 40000 AND d.department = 'research' ", conn)

# Q3: Who is the supreme chief of this fictional company (aka the President)?
ans3a = pd.read_sql_query("SELECT e.employee_name FROM employee e JOIN salary f ON e.employee_name = f.employee_name WHERE f.salary = (SELECT MAX(salary) FROM salary) ", conn)
ans3b = pd.read_sql_query("SELECT e.employee_name FROM employee e LEFT JOIN supervise s ON e.employee_name = s.subordinate WHERE s.supervisor IS NULL ", conn)

# Q4: Who are the individuals that work on project "productx" with an *effort*
# of 20 or more hours a week?
ans4 = pd.read_sql_query("SELECT e.employee_name FROM employee e JOIN workson w ON e.employee_name = w.name WHERE w.project = 'productx' AND w.effort >= 20", conn)


# b = pd.read_sql_query("SELECT e.* FROM employee e JOIN female f ON e.employee_name = f.name JOIN supervise s JOIN workson p ON e.project_id = p.project_id WHERE e.gender = 'female' AND p.project_name = 'computerization' AND e.hours_per_week = 10 AND e.supervisor_name = 'jennifer' ", conn)

print("Question 1")
print(ans1)

print("Question 2")
print(ans2)

print("Question 3") 
print("Method ONE (Max Salary):")
print(ans3a)
print("Method TWO (Displays those that dont have supervisor):")
print(ans3b)

print("Question 4")
print(ans4)

# Close the connection
conn.close()