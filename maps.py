import pandas as pd

# 1. SETUP: The Spatial Base Model Data
data = {
    'Ward': ['Adyar', 'Anna Nagar', 'T-Nagar', 'Mylapore', 'Velachery'],
    'Population': [250000, 300000, 200000, 150000, 280000],
    'Current_GW_Level': [12.5, 15.2, 18.0, 10.5, 14.0],  # Meters below ground
    'Recharge_Rate': [0.12, 0.08, 0.05, 0.15, 0.10],    # Soil permeability
    'Daily_Demand_LPCD': 150 # Liters Per Capita Day
}

df = pd.DataFrame(data)

def run_simulation(rainfall_mm, policy_rwh=False):
    """
    Step 3, 4, and 6: The Simulation Engine
    rainfall_mm: Yearly rainfall input
    policy_rwh: Boolean (If True, increases recharge by 20%)
    """
    # Calculate Total Demand (MLD - Million Liters per Day)
    df['Total_Demand_MLD'] = (df['Population'] * df['Daily_Demand_LPCD']) / 1_000_000
    
    # Step 4: Groundwater Impact
    # Simplification: Change in GW = (Rainfall * Recharge) - Extraction
    rwh_boost = 1.2 if policy_rwh else 1.0
    
    df['GW_Recharge_Volume'] = (rainfall_mm * df['Recharge_Rate'] * rwh_boost)
    df['Extraction_Impact'] = df['Total_Demand_MLD'] * 0.5 # Assume 50% comes from GW
    
    # Calculate Net Change
    df['Net_GW_Change'] = df['GW_Recharge_Volume'] - df['Extraction_Impact']
    
    # Step 5: Risk Level
    df['Risk_Level'] = df['Net_GW_Change'].apply(lambda x: 'CRITICAL' if x < 50 else 'STABLE')
    
    return df

# --- STEP 6: RUNNING SCENARIOS ---

print("🌊 --- CWIS SIMULATION REPORT --- 🌊\n")

# Scenario A: Drought Year
print("⚠️ SCENARIO: DROUGHT (500mm Rain)")
drought_results = run_simulation(500)
print(drought_results[['Ward', 'Total_Demand_MLD', 'Net_GW_Change', 'Risk_Level']])

print("\n" + "-"*50 + "\n")

# Scenario B: Normal Rain + Rainwater Harvesting Policy
print("✅ SCENARIO: NORMAL RAIN (1200mm) + MANDATORY RWH")
policy_results = run_simulation(1200, policy_rwh=True)
print(policy_results[['Ward', 'Total_Demand_MLD', 'Net_GW_Change', 'Risk_Level']])