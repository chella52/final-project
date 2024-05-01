import yaml
import pandas as pd
from neo4j import GraphDatabase

class Neo4jDataLoader:
    """
    A class to load data from Neo4j and convert it into a pandas DataFrame.

    Attributes:
    - neo4j_uri: The URI of the Neo4j database.
    - neo4j_user: The username to authenticate with Neo4j.
    - neo4j_password: The password to authenticate with Neo4j.
    - cypher_query: The Cypher query to retrieve data from Neo4j.
    """

    def __init__(self, config_file_path='config.yaml'):
        """
        Initializes the Neo4jDataLoader class.

        Parameters:
        - config_file_path (str): The path to the YAML configuration file.
        """
        with open(config_file_path, 'r') as config_file:
            config = yaml.safe_load(config_file)

        self.neo4j_uri = config['neo4j']['uri']
        self.neo4j_user = config['neo4j']['user']
        self.neo4j_password = config['neo4j']['password']

        self.cypher_query = """
            MATCH (s:Sale)
            RETURN s.region AS Region, s.country AS Country, s.itemType AS ItemType, s.salesChannel AS SalesChannel,
                   s.orderPriority AS OrderPriority, s.orderDate AS OrderDate, s.orderID AS OrderID,
                   s.shipDate AS ShipDate, s.unitsSold AS UnitsSold, s.unitPrice AS UnitPrice,
                   s.unitCost AS UnitCost, s.totalRevenue AS TotalRevenue, s.totalCost AS TotalCost,
                   s.totalProfit AS TotalProfit
        """

    def load_data(self):
        """
        Loads data from Neo4j and converts it into a pandas DataFrame.

        Returns:
        - df (pandas.DataFrame): The DataFrame containing the loaded data.
        """
        driver = GraphDatabase.driver(self.neo4j_uri, auth=(self.neo4j_user, self.neo4j_password))

        with driver.session() as session:
            result = session.run(self.cypher_query)
            data = result.data()

        df = pd.DataFrame(data)
        return df

# Create an instance of Neo4jDataLoader and load the data
loader = Neo4jDataLoader()
df = loader.load_data()

# Print success message
print("DataFrame 'df' created successfully.")

