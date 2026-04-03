
import streamlit as st
import pandas as pd
import numpy as np

st.title("🤖 Next Best Action Simulator")
st.write("This app simulates how AI-driven decisions improve long-term user value compared to rule-based strategies.")

num_users = st.slider("Number of Users", 100, 1000, 500)
num_days = st.slider("Number of Days", 5, 20, 10)

actions = ["show_offer", "show_video", "send_notification"]

users = pd.DataFrame({
    "user_id": range(num_users),
    "user_type": np.random.choice(["deal_hunter", "content_consumer", "casual"], size=num_users)
})

def get_response(user_type, action):
    probs = {
        "deal_hunter": {"show_offer": 0.7, "show_video": 0.2, "send_notification": 0.4},
        "content_consumer": {"show_offer": 0.2, "show_video": 0.7, "send_notification": 0.3},
        "casual": {"show_offer": 0.3, "show_video": 0.3, "send_notification": 0.2}
    }
    return np.random.rand() < probs[user_type][action]

def simple_model(user_type, action):
    if user_type == "deal_hunter":
        return {"show_offer": 0.7, "show_video": 0.2, "send_notification": 0.4}[action]
    elif user_type == "content_consumer":
        return {"show_offer": 0.2, "show_video": 0.7, "send_notification": 0.3}[action]
    else:
        return {"show_offer": 0.3, "show_video": 0.3, "send_notification": 0.2}[action]

def get_next_best_action(user_type):
    scores = [(a, simple_model(user_type, a)) for a in actions]
    return max(scores, key=lambda x: x[1])[0]

def simulate_ai():
    results = []
    for _, user in users.iterrows():
        user_type = user["user_type"]
        cumulative = 0
        for day in range(num_days):
            action = get_next_best_action(user_type)
            response = int(get_response(user_type, action))
            cumulative += response
            results.append({
                "user_id": user["user_id"],
                "day": day,
                "strategy": "AI",
                "cumulative": cumulative
            })
    return pd.DataFrame(results)

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

if st.button("Run Simulation 🚀"):
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
