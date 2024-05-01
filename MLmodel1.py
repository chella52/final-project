from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 
from retrieve import df 

class RegressionModel:
    """
    A class to perform linear regression modeling.

    Attributes:
    - df (pandas.DataFrame): The DataFrame containing the data.
    """

    def __init__(self, df):
        """
        Initializes the RegressionModel class.

        Parameters:
        - df (pandas.DataFrame): The DataFrame containing the data.
        """
        self.df = df

    def train_linear_regression(self, feature_cols, target_col, test_size=0.2, random_state=42):
        """
        Trains a linear regression model using the provided data.

        Parameters:
        - feature_cols (list): The list of column names representing the features.
        - target_col (str): The name of the target variable column.
        - test_size (float, optional): The proportion of the dataset to include in the test split.
        - random_state (int, optional): Controls the shuffling applied to the data before splitting.

        Returns:
        - r2 (float): The R-squared score of the model.
        """
        # Selecting features and target variable
        X = self.df[feature_cols]
        y = self.df[target_col]

        # Splitting the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        # Creating and training the linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Making predictions
        y_pred = model.predict(X_test)

        # Evaluating the model
        r2 = r2_score(y_test, y_pred)

        # Printing coefficients associated with each feature
        for feature, coef in zip(feature_cols, model.coef_):
            if coef > 0:
                print(f"For each additional unit increase in {feature}, the predicted {target_col} increases by {coef:.1f} units.")
            elif coef < 0:
                print(f"For each additional unit increase in {feature}, the predicted {target_col} decreases by {abs(coef):.1f} units.")
            else:
                print(f"The coefficient associated with {feature} is zero, indicating no impact on {target_col}.")

        return r2

# Assuming df is your DataFrame containing the loaded data
# Replace 'feature_cols' and 'target_col' with your specific column names
feature_cols = ['UnitsSold', 'UnitPrice', 'UnitCost']
target_col = 'TotalRevenue'

# Create an instance of RegressionModel
regression_model = RegressionModel(df)

# Train the linear regression model
r2 = regression_model.train_linear_regression(feature_cols, target_col)

# Print the evaluation metrics
print("R-squared Score:", r2)

