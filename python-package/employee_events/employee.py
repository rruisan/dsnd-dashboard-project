# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
from .sql_execution import query

# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"


    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    def names(self):
        
        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        q = f"""
            SELECT first_name, last_name, employee_id
            FROM {self.name};
        """
        result = self.query(q)
        return [(f"{row[0]} {row[1]}", row[2]) for row in result]    

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    def username(self, id):
        
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        q = f"""
            SELECT first_name, last_name
            FROM {self.name}
            WHERE employee_id = {id};
        """
        result = self.query(q)
        return [(f"{row[0]} {row[1]}",) for row in result]

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    def model_data(self, id):
        q = f"""
            SELECT SUM(positive_events) AS positive_events
                 , SUM(negative_events) AS negative_events
            FROM {self.name}
            JOIN employee_events
                ON employee.employee_id = employee_events.employee_id  -- Corrección del JOIN
            WHERE {self.name}.employee_id = {id};  -- Condición WHERE correcta
        """
        return self.pandas_query(q)