import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from retrieve import df

class AnomalyDetection:
    """
    Class for detecting anomalies in sales transactions using Isolation Forest.
    
    Attributes:
        df (pandas.DataFrame): DataFrame containing sales transaction data.
    """
    def __init__(self, df):
        """
        Initializes the AnomalyDetection object with the provided DataFrame.
        
        Args:
            df (pandas.DataFrame): DataFrame containing sales transaction data.
        """
        self.df = df.copy()

    def detect_anomalies(self):
        """
        Detects anomalies in sales transactions using Isolation Forest and plots the anomalies.
        """
        # Selecting numerical features for anomaly detection
        numerical_features = ['UnitsSold', 'UnitPrice', 'UnitCost', 'TotalRevenue', 'TotalCost', 'TotalProfit']
        X = self.df[numerical_features]

        # Training the Isolation Forest model
        isolation_forest = IsolationForest(contamination=0.01)  # Contamination parameter defines the proportion of outliers to be detected
        isolation_forest.fit(X)

        # Predicting outliers
        outliers = isolation_forest.predict(X)

        # Adding outlier predictions to the original dataframe
        self.df['Outlier'] = outliers

        # Plotting the anomalies
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df.index, self.df['TotalProfit'], c=self.df['Outlier'], cmap='coolwarm', s=20)
        plt.xlabel('Index')
        plt.ylabel('Total Profit')
        plt.title('Anomaly Detection with Isolation Forest')
        plt.colorbar(label='Outlier Score')
        plt.show()

    def get_anomalies(self):
        """
        Returns the anomalies detected in the sales transactions.
        
        Returns:
            pandas.DataFrame: DataFrame containing the detected anomalies.
        """
        return self.df[self.df['Outlier'] == -1]


# Example usage:
if __name__ == "__main__":
    # Load the dataset
    from retrieve import df
    anomaly_detector = AnomalyDetection(df)
    anomaly_detector.detect_anomalies()
    anomalies = anomaly_detector.get_anomalies()
    print("Anomalies Detected:")
    print(anomalies)

