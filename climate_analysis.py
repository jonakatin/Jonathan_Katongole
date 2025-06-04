import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("climate_action_data.csv")

# Initial inspection
print("Initial shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nSample Records:\n", df.head())

# Step 1: Replace 'error' entries with NaN
df.replace("error", np.nan, inplace=True)

# Step 2: Attempt to convert columns to numeric where applicable
for col in df.columns:
    if df[col].dtype == 'object':
        try:
            df[col] = pd.to_numeric(df[col])
            print(f"Converted {col} to numeric.")
        except:
            pass  # Leave non-convertible columns as-is

# Step 3: Remove duplicate rows
df.drop_duplicates(inplace=True)

# Step 4: Visualize missing data before imputation
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Data Heatmap")
plt.tight_layout()
plt.savefig("missing_data_heatmap.png")
plt.show()

# Step 5: Handle missing values
# Fill numeric columns with median
for col in df.select_dtypes(include=[np.number]).columns:
    if df[col].isnull().sum() > 0:
        median = df[col].median()
        df[col].fillna(median, inplace=True)
        print(f"Filled missing values in numeric column '{col}' with median: {median}")

# Fill categorical columns with mode
for col in df.select_dtypes(include=['object']).columns:
    if df[col].isnull().sum() > 0:
        mode = df[col].mode()[0]
        df[col].fillna(mode, inplace=True)
        print(f"Filled missing values in categorical column '{col}' with mode: {mode}")

# Step 6: Re-inspect cleaned data
print("\nCleaned DataFrame Info:")
print(df.info())

# Step 7: Descriptive statistics
print("\nDescriptive Statistics:\n", df.describe(include='all'))

# Step 8: Histograms of numeric variables
df.select_dtypes(include=[np.number]).hist(bins=20, figsize=(14, 10), edgecolor='black')
plt.tight_layout()
plt.suptitle("Histograms of Numeric Variables", fontsize=16)
plt.subplots_adjust(top=0.92)
plt.savefig("climate_analysis_histograms.png")
plt.show()

# Step 9: Correlation heatmap
numeric_df = df.select_dtypes(include=[np.number])
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap="YlGnBu")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# Step 10: Insights

# Correlation with Fertilizer_Recommendation
if 'Fertilizer_Recommendation' in df.columns:
    try:
        corr_target = numeric_df.corr()['Fertilizer_Recommendation'].drop('Fertilizer_Recommendation')
        print("\nCorrelation with Fertilizer Recommendation:\n", corr_target.sort_values(ascending=False))
    except Exception as e:
        print("Could not calculate correlation with 'Fertilizer_Recommendation':", e)

# Crop with highest average soil moisture
if 'Crop_Type' in df.columns and 'Soil_Moisture' in df.columns:
    try:
        highest_soil_moisture = df.groupby("Crop_Type")["Soil_Moisture"].mean().sort_values(ascending=False)
        print("\nCrop Types by Average Soil Moisture:\n", highest_soil_moisture)
        print(f"\nCrop with highest average soil moisture: {highest_soil_moisture.idxmax()}")
    except Exception as e:
        print("Could not determine crop with highest soil moisture:", e)

# Suggest irrigation for crops where Temperature > 30°C
if 'Temperature' in df.columns and 'Soil_Moisture' in df.columns and 'Crop_Type' in df.columns:
    try:
        hot_crops = df[df['Temperature'] > 30]
        avg_soil_moisture = hot_crops.groupby("Crop_Type")["Soil_Moisture"].mean()
        print("\nIrrigation Suggestions for Crops with Temp > 30°C:")
        for crop, moisture in avg_soil_moisture.items():
            if moisture < 30:
                print(f"Increase irrigation for {crop} (Avg Soil Moisture: {moisture:.2f})")
            else:
                print(f"{crop} has sufficient moisture ({moisture:.2f})")
    except Exception as e:
        print("Could not generate irrigation suggestions:", e)

# Step 11: Save cleaned dataset
df.to_csv("cleaned_precision_agriculture_data.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_precision_agriculture_data.csv'")