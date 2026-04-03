# 🤖 Next Best Action Simulator  
### Building an AI System to Optimize Long-Term User Value

## 🔗 Live Demo  
👉 https://nba-simulator-92zlj8uzeneoppjvjh8q9c.streamlit.app/


## 🧠 TL;DR

Most systems optimize for short-term engagement (clicks), but real-world products need to optimize for **long-term user value (LTV)**.

In this project, I built a **Next Best Action (NBA) system** that:

- Learns user behavior from data  
- Predicts short-term response probabilities  
- Uses those predictions to make sequential decisions  
- Demonstrates how AI improves long-term outcomes (~35% higher LTV vs rules)

---

# 🎯 Problem

Modern products (recommendations, ads, notifications) face a core challenge:

> Should we optimize for immediate clicks or long-term value?

---

## ❌ Limitation of Short-Term Metrics

Optimizing for clicks can lead to:

- spammy notifications  
- poor user experience  
- declining long-term engagement  

---

## 💡 Key Question

> How can we design systems that optimize **long-term user value** instead of short-term interactions?

---

# 🧪 Approach

We simulate a controlled environment to study decision-making over time.

---

## 🧩 Step 1: Simulate User Behavior

We create synthetic users with different behavioral patterns:

| User Type | Preference |
|----------|-----------|
| deal_hunter | responds to offers |
| content_consumer | prefers videos |
| casual | mixed behavior |

---

### Why simulate?

- Real-world data is noisy and biased  
- Simulation gives us **ground truth behavior**  
- Enables controlled experimentation  

---

## 🧠 Key Insight

> AI is only needed when user behavior is heterogeneous. If all users behaved the same, simple rules would suffice.

---

# 📊 Step 2: Define Long-Term Metrics

---

## ❌ Short-Term Metric

- Response (click/no click)

---

## ✅ Long-Term Metric

### Lifetime Value (LTV)


---

## 🔁 Supporting Metric: Cumulative Reward

- Tracks value accumulation over time  
- Used during simulation  

---

### ⚠️ Important Distinction

| Metric | Role |
|------|------|
| Cumulative Reward | dynamic (used during simulation) |
| LTV | final outcome (used for evaluation) |

---

## 🧠 Key Insight

> Optimizing for short-term response does not guarantee long-term value.

---

# 🤖 Step 3: Train Prediction Model

We train a supervised model to estimate: P(response | user_state, action)


---

## 📥 Inputs

- user type  
- previous action  
- previous response  
- candidate action  

---

## 📤 Output

- probability of response (0–1)

---

## 🧠 Important Insight

> The model does NOT optimize LTV — it only predicts short-term outcomes.

---

# ⚠️ Why Not Predict LTV Directly?

Because:

- LTV is a future outcome  
- difficult to attribute to individual actions  
- delayed and noisy  

---

## 🔥 Core Idea

> Long-term optimization emerges from repeated short-term decisions

---

# ⚙️ Step 4: Build Decision System (NBA)

This is the most important step.

---

## 🎯 Next Best Action Logic

For each user state:

1. Evaluate all possible actions  
2. Predict response probability for each  
3. Select action with highest probability  

---

## 🔁 Decision Loop P(response | user_state, action)


---

## 🧠 Key Insight

> Machine learning models do not make decisions — decision logic built on top of predictions does.

---

# 🔄 Step 5: Multi-Step Simulation

---

## Why simulation is needed

Single-step evaluation is misleading because:

- actions affect future states  
- bad early decisions compound  

---

## What we simulate

For each user:

- multiple days  
- sequential actions  
- evolving state  

---

## 🔥 Advanced Concept

This approximates:

> **Counterfactual reasoning**  
(What would have happened if we chose differently?)

---

# ⚔️ Step 6: Compare Strategies

---

## 🟥 Rule-Based Strategy

- repeat last successful action  
- random exploration otherwise  

---

## 🟩 AI Strategy

- use model predictions  
- always choose best action  

---

# 📊 Results

| Strategy | Avg LTV |
|----------|--------|
| Rule-Based | ~4.1 |
| AI (NBA) | ~5.6 |

---

👉 **~35–40% improvement**

---

# 🔍 Why AI Works Better

---

## Rule-Based

- trial-and-error  
- slow adaptation  
- no generalization  

---

## AI System

- learns user patterns  
- adapts quickly  
- makes better early decisions  

---

## 🧠 Key Insight

> Early decisions compound over time → better early actions → higher long-term value

---

# ⚠️ Risks of AI Systems

---

## 1. Over-exploitation
- same action repeated  
- user fatigue  

---

## 2. Feedback loops
- system reinforces its own behavior  

---

## 3. Cold start
- no data for new users  

---

## 4. Wrong generalization
- incorrect assumptions applied  

---

## 🧠 Key Insight

> AI systems don’t just optimize behavior — they shape it.

---

# ⚡ System Challenges

---

## 🚨 Inference Latency

Simulation requires:

---

## 🧠 Key Insight

> Machine learning models do not make decisions — decision logic built on top of predictions does.

---

# 🔄 Step 5: Multi-Step Simulation

---

## Why simulation is needed

Single-step evaluation is misleading because:

- actions affect future states  
- bad early decisions compound  

---

## What we simulate

For each user:

- multiple days  
- sequential actions  
- evolving state  

---

## 🔥 Advanced Concept

This approximates:

> **Counterfactual reasoning**  
(What would have happened if we chose differently?)

---

# ⚔️ Step 6: Compare Strategies

---

## 🟥 Rule-Based Strategy

- repeat last successful action  
- random exploration otherwise  

---

## 🟩 AI Strategy

- use model predictions  
- always choose best action  

---

# 📊 Results

| Strategy | Avg LTV |
|----------|--------|
| Rule-Based | ~4.1 |
| AI (NBA) | ~5.6 |

---

👉 **~35–40% improvement**

---

# 🔍 Why AI Works Better

---

## Rule-Based

- trial-and-error  
- slow adaptation  
- no generalization  

---

## AI System

- learns user patterns  
- adapts quickly  
- makes better early decisions  

---

## 🧠 Key Insight

> Early decisions compound over time → better early actions → higher long-term value

---

# ⚠️ Risks of AI Systems

---

## 1. Over-exploitation
- same action repeated  
- user fatigue  

---

## 2. Feedback loops
- system reinforces its own behavior  

---

## 3. Cold start
- no data for new users  

---

## 4. Wrong generalization
- incorrect assumptions applied  

---

## 🧠 Key Insight

> AI systems don’t just optimize behavior — they shape it.

---

# ⚡ System Challenges

---

## 🚨 Inference Latency

Simulation requires: users × days × actions × predictions

---

## 💡 Observation

> The bottleneck in AI systems is often **inference latency**, not training

---

## ⚙️ Optimizations Applied

- caching model predictions  
- reducing simulation scale  
- optimized feature encoding  

---

# ⚖️ Trade-offs

| Factor | Trade-off |
|------|-----------|
| Accuracy | ↑ |
| Speed | ↓ |

---

## 🧠 Insight

> The best model is not always the best system — system design matters.

---

# 🧱 System Architecture Summary

---

### 1. Model
Predicts response probability  

---

### 2. Decision Layer
Selects best action  

---

### 3. Environment
Simulates user behavior  

---

### 🔁 Loop

---

## 💡 Observation

> The bottleneck in AI systems is often **inference latency**, not training

---

## ⚙️ Optimizations Applied

- caching model predictions  
- reducing simulation scale  
- optimized feature encoding  

---

# ⚖️ Trade-offs

| Factor | Trade-off |
|------|-----------|
| Accuracy | ↑ |
| Speed | ↓ |

---

## 🧠 Insight

> The best model is not always the best system — system design matters.

---

# 🧱 System Architecture Summary

---

### 1. Model
Predicts response probability  

---

### 2. Decision Layer
Selects best action  

---

### 3. Environment
Simulates user behavior  

---

### 🔁 Loop
state → decision → outcome → new state


---

## 🔥 Final Insight

> AI systems create value through better sequences of decisions, not just better predictions.

---

# 🧪 Tech Stack

- Python  
- pandas, numpy  
- scikit-learn  
- Streamlit  

---

# 🌐 Deployment

Deployed on Streamlit Cloud:

- interactive UI  
- public link  
- real-time simulation  

---

# 🚀 Future Work

- exploration (epsilon-greedy / bandits)  
- delayed rewards (reinforcement learning)  
- real-world datasets  
- advanced models (XGBoost, deep learning)  

---

# 👩‍💻 Author

Built as part of preparation for **AI Product Management roles**

---

# ⭐ Final Takeaway

> Building AI systems is not just about predicting better —  
> it’s about designing systems that make better decisions over time.



