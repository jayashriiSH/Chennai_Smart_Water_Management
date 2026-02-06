def apply_scenario(
    base_supply,
    base_demand,
    climate,
    population_factor,
    supply_options,
    policy_options
):
    supply = float(base_supply)
    demand = float(base_demand)



    # 🌧️ Climate Scenarios
    if climate == "Low Rainfall":
        supply *= 0.8
    elif climate == "Extreme Drought":
        supply *= 0.6
    elif climate == "Excess Rainfall":
        supply *= 1.2

    # 🧍 Population Growth
    demand *= population_factor

    # 💧 Supply Scenarios
    if "Reservoir Failure" in supply_options:
        supply *= 0.7
    if "Desalination Expansion" in supply_options:
        supply += 120
    if "Rainwater Harvesting" in supply_options:
        supply += 80

    # 🏛️ Policy Scenarios
    if "Reduced Groundwater Pumping" in policy_options:
        demand *= 0.85
    if "Leak Reduction Program" in policy_options:
        supply *= 1.1

    net = supply - demand

    # 🚦 Risk Classification (WIDE & REALISTIC)
    if net >= 80:
        risk = "LOW"
    elif net >= -40:
        risk = "MODERATE"
    else:
        risk = "HIGH"

    return {
        "supply": round(supply, 1),
        "demand": round(demand, 1),
        "net": round(net, 1),
        "risk": risk
    }
