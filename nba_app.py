import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -------------------------------
# Load model with caching
# -------------------------------
@st.cache_resource
def load_artifacts():
    with open("nba_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("columns.pkl", "rb") as f:
        columns = pickle.load(f)

    return model, columns

model, columns = load_artifacts()

# -------------------------------
# UI
# -------------------------------
st.title("🤖 Next Best Action Simulator")
st.write("This app simulates how AI-driven decisions improve long-term user value compared to rule-based strategies.")

# Reduced defaults for speed
num_users = st.slider("Number of Users", 50, 300, 100)
num_days = st.slider("Number of Days", 5, 20, 10)

actions = ["show_offer", "show_video", "send_notification"]

users = pd.DataFrame({
    "user_id": range(num_users),
    "user_type": np.random.choice(["deal_hunter", "content_consumer", "casual"], size=num_users)
})

# -------------------------------
# Behavior Logic (Ground Truth)
# -------------------------------
def get_response(user_type, action):
    probs = {
        "deal_hunter": {"show_offer": 0.7, "show_video": 0.2, "send_notification": 0.4},
        "content_consumer": {"show_offer": 0.2, "show_video": 0.7, "send_notification": 0.3},
        "casual": {"show_offer": 0.3, "show_video": 0.3, "send_notification": 0.2}
    }
    return np.random.rand() < probs[user_type][action]

# -------------------------------
# FAST Prediction (Optimized)
# -------------------------------
def predict_response(user_type, prev_action, prev_response, action):

    # Create empty feature vector (FAST)
    row_encoded = pd.DataFrame(0, index=[0], columns=columns)

    # Set relevant features manually
    if f"user_type_{user_type}" in row_encoded:
        row_encoded[f"user_type_{user_type}"] = 1

    if f"action_{action}" in row_encoded:
        row_encoded[f"action_{action}"] = 1

    if f"prev_action_{prev_action}" in row_encoded:
        row_encoded[f"prev_action_{prev_action}"] = 1

    if "prev_response" in row_encoded:
        row_encoded["prev_response"] = prev_response

    # Predict probability
    prob = model.predict_proba(row_encoded)[0][1]

    return prob

# -------------------------------
# Next Best Action
# -------------------------------
def get_next_best_action(user_type, prev_action, prev_response):
    scores = []

    for action in actions:
        prob = predict_response(user_type, prev_action, prev_response, action)
        scores.append((action, prob))

    return max(scores, key=lambda x: x[1])[0]

# -------------------------------
# AI Simulation
# -------------------------------
def simulate_ai():
    results = []

    for _, user in users.iterrows():
        user_type = user["user_type"]
        cumulative = 0

        prev_action = "none"
        prev_response = 0

        for day in range(num_days):
            action = get_next_best_action(user_type, prev_action, prev_response)

            response = int(get_response(user_type, action))
            cumulative += response

            results.append({
                "user_id": user["user_id"],
                "day": day,
                "strategy": "AI",
                "cumulative": cumulative
            })

            prev_action = action
            prev_response = response

    return pd.DataFrame(results)

# -------------------------------
# Rule-Based Simulation
# -------------------------------
def simulate_rule():
    results = []

    for _, user in users.iterrows():
        user_type = user["user_type"]
        prev_action = np.random.choice(actions)
        prev_response = 0
        cumulative = 0

        for day in range(num_days):
            if prev_response == 1:
                action = prev_action
            else:
                action = np.random.choice(actions)

            response = int(get_response(user_type, action))
            cumulative += response

            results.append({
                "user_id": user["user_id"],
                "day": day,
                "strategy": "Rule",
                "cumulative": cumulative
            })

            prev_action = action
            prev_response = response

    return pd.DataFrame(results)

# -------------------------------
# Run Simulation
# -------------------------------
if st.button("Run Simulation 🚀"):

    with st.spinner("Running simulation..."):
        ai_df = simulate_ai()
        rule_df = simulate_rule()

    ai_ltv = ai_df.groupby("user_id")["cumulative"].max().mean()
    rule_ltv = rule_df.groupby("user_id")["cumulative"].max().mean()

    st.subheader("📊 Results")
    st.write(f"AI LTV: {round(ai_ltv,2)}")
    st.write(f"Rule LTV: {round(rule_ltv,2)}")

    improvement = ((ai_ltv - rule_ltv) / rule_ltv) * 100
    st.write(f"📈 Improvement: {round(improvement,1)}%")

    combined = pd.concat([ai_df, rule_df])
    chart = combined.groupby(["day", "strategy"])["cumulative"].mean().reset_index()

    st.line_chart(chart.pivot(index="day", columns="strategy", values="cumulative"))
