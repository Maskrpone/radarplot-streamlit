import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

data = [
    {"name": "Cataracte", "branch": "vision", "is_enabled": True, "value": 10},
    {"name": "Presbitie", "branch": "vision", "is_enabled": True, "value": 12},
    {"name": "Audition", "branch": "audition", "is_enabled": True, "value": 15},
    {"name": "Surpoids", "branch": "mobilité", "is_enabled": True, "value": 6},
    {"name": "1", "branch": "masse musculaire", "is_enabled": True, "value": 20}
]

branchs = [
    "mobilité",
    "masse musculaire",
    "densité osseuse",
    "nutrition",
    "risque vasculaire",
    "vision",
    "audition",
    "cognition",
    "psychologie",
    "sommeil"
]

st.title("Dynamic Radarplot")

st.header("Edition")
st.markdown("Enable or disable prefragility factors to update the radarplot")

edited_data = st.data_editor(data, key="field_editor", disabled=["name", "branch", "value"], column_order=["name", "is_enabled"])

df = pd.DataFrame(edited_data)
df_enabled = df[df["is_enabled"]]
branch_scores = df_enabled.groupby('branch')['value'].sum().reset_index()
branch_scores.columns = ["branch", 'score']

df_all_branches = pd.DataFrame({'branch': branchs})
final_scores = pd.merge(
    df_all_branches,
    branch_scores,
    on='branch',
    how='left'
).fillna({'score': 0})
final_scores['score'] = final_scores['score'].astype(int)

plot_data = pd.DataFrame(dict(
    r = final_scores["score"],
    theta = branchs
))


# Plotting
st.header("Radar Plot")
fig = px.line_polar(plot_data, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')
st.plotly_chart(fig)

# Data editor
edited_df = st.data_editor(final_scores)
