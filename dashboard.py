import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------
st.set_page_config(
    page_title="Chennai Water Live Monitoring",
    layout="wide"
)

# ----------------------------------------
# LOAD DATA
# ----------------------------------------
data = pd.read_csv("final_output.csv")
data.columns = data.columns.str.lower()
data["date"] = pd.to_datetime(data["date"])
data = data.sort_values("date")

# ----------------------------------------
# SESSION STATE
# ----------------------------------------
if "index" not in st.session_state:
    st.session_state.index = 0

# Auto-refresh every 10 seconds
st_autorefresh(interval=10000, key="playback")

# Move timeline
if st.session_state.index < len(data) - 1:
    st.session_state.index += 1
else:
    st.session_state.index = 0

current = data.iloc[st.session_state.index]

# ----------------------------------------
# TITLE
# ----------------------------------------
st.title("💧 Chennai Smart Water — Live Monitoring (Simulated)")
st.caption("Time-based digital twin replay of reservoir operations")

st.markdown(f"### 📅 Current Date: **{current['date'].date()}**")

st.divider()

# ----------------------------------------
# CITY STATUS
# ----------------------------------------
st.subheader("🏙️ City Water Status")

c1, c2, c3 = st.columns(3)

c1.metric("Supply Index", round(current["supply_index"], 3))
c2.metric("Water Stress", current["water_stress_level"])
c3.metric("Alert Level", current["alert_level"])

st.divider()

st.subheader("🧠 System Intelligence & Advisory")

# explanation text
if current["alert_level"] == "CRITICAL 🔴":
    st.error(
        "⚠️ **Critical Water Stress Detected.**\n\n"
        "Multiple reservoirs are showing highly negative net flow, "
        "indicating excessive outflow and depletion. Immediate action is "
        "recommended to stabilize water supply. Authorities should consider:\n"
    )
    st.markdown(
        "- 🔹 Reducing metro and industrial drawal temporarily.\n"
        "- 🔹 Activating secondary sources like Veeranam supply.\n"
        "- 🔹 Issuing public water conservation advisories.\n"
        "- 🔹 Preparing emergency distribution plans."
    )

elif current["alert_level"] == "MEDIUM PRIORITY 🟡":
    st.warning(
        "⚠️ **Moderate Water Stress Noted.**\n\n"
        "Some reservoirs are compensating for deficits in others.\n"
        "Careful monitoring and gradual demand management is advised.\n"
    )
    st.markdown(
        "- ⚪ Monitor reservoir levels and adjust pumping schedules.\n"
        "- ⚪ Encourage voluntary conservation campaigns.\n"
        "- ⚪ Assess upcoming rainfall forecasts for replenishment."
    )

else:
    st.success(
        "✅ **Water System Stable.**\n\n"
        "Reservoir inflow and outflow are balanced for the current period.\n"
        "Continue routine monitoring to maintain stability."
    )

# ----------------------------------------
# RESERVOIR STATUS
# ----------------------------------------
st.subheader("🏞️ Reservoir Operations")

reservoirs = {
    "Poondi": ["poondi_inflow_total", "poondi_outflow_total"],
    "Cholavaram": ["cholavaram_inflow_total", "cholavaram_outflow_total"],
    "Red Hills": ["redhills_inflow_total", "redhills_outflow_total"],
    "Chembarambakkam": ["chembarambakkam_inflow_total", "chembarambakkam_outflow_total"],
    "Veeranam": ["veeranam_inflow_total", "veeranam_outflow_total"],
    "Thervoy Kandigai": ["thervoykandigai_inflow_total", "thervoykandigai_outflow_total"]
}

cols = st.columns(len(reservoirs))

for col, (dam, (inf, outf)) in zip(cols, reservoirs.items()):
    inflow = current[inf]
    outflow = current[outf]
    net = inflow - outflow

    if inflow == 0 and outflow == 0 and current["alert_level"] == "CRITICAL 🔴":
        status = "HIGH 🔴 (Backup inactive)"
    elif net < -300:
        status = "HIGH 🔴"
    elif net < -100:
        status = "MODERATE 🟡"
    else:
        status = "NORMAL 🟢"

    col.markdown(
        f"""
        ### {dam}
        **Inflow:** {int(inflow)} MLD  
        **Outflow:** {int(outflow)} MLD  
        **Net:** {int(net)} MLD  
        **Status:** {status}
        """
    )

st.divider()
def generate_explanation(row):
    if row["alert_level"] == "CRITICAL 🔴":
        return (
            "⚠️ Multiple reservoirs are under severe stress. "
            "Outflow exceeds inflow for prolonged periods, indicating over-extraction. "
            "The city is relying heavily on limited backup sources. "
            "Immediate demand regulation and alternate sourcing are strongly recommended."
        )

    elif row["alert_level"] == "MODERATE 🟡":
        return (
            "⚠️ Water supply imbalance detected. "
            "Some reservoirs are compensating for others, increasing operational load. "
            "Preventive measures such as controlled release and demand awareness are advised."
        )

    else:
        return (
            "✅ Reservoir operations are currently stable. "
            "Inflow and outflow levels are balanced, indicating healthy system performance."
        )
def generate_suggestions(row):
    suggestions = []

    if row["alert_level"] == "CRITICAL 🔴":
        suggestions = [
            "🚨 Activate emergency water management protocol",
            "🚰 Reduce metro water drawal temporarily",
            "💧 Increase Veeranam and backup sourcing",
            "🏗️ Regulate industrial and tanker usage",
            "📢 Issue public water conservation advisory"
        ]

    elif row["alert_level"] == "MODERATE 🟡":
        suggestions = [
            "⚖️ Monitor reservoir extraction closely",
            "🚰 Balance supply across reservoirs",
            "📊 Prepare contingency distribution plan",
            "📢 Encourage voluntary conservation"
        ]

    else:
        suggestions = [
            "✅ Continue normal operations",
            "📈 Maintain routine monitoring",
            "🛠️ Perform preventive maintenance"
        ]

    return suggestions
st.divider()
st.subheader("🧠 System Intelligence Summary")

explanation = generate_explanation(current)
suggestions = generate_suggestions(current)

st.info(explanation)

st.markdown("### ✅ Recommended Actions")
for s in suggestions:
    st.markdown(f"- {s}")

# ----------------------------------------
# TREND GRAPH
# ----------------------------------------
st.subheader("📊 Reservoir Flow Trend (Last 30 Days)")

selected = st.selectbox("Select Reservoir", list(reservoirs.keys()))
inf_col, out_col = reservoirs[selected]

trend_df = data.iloc[
    max(0, st.session_state.index - 30) : st.session_state.index + 1
]

fig = px.line(
    trend_df,
    x="date",
    y=[inf_col, out_col],
    labels={"value": "MLD", "variable": "Flow"},
    title=f"{selected} — Flow Trend"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# FOOTER
# ----------------------------------------
st.caption(
    "Digital Twin Simulation | Smart City Chennai Water Intelligence"
)
