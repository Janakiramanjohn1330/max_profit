## 📈 Max Profit Land Development Optimization ## 
**📌 Overview**

* This project solves the Max Profit Problem, where a landowner must decide the optimal combination of properties to build within a given time constraint in order to maximize total         earnings.

* Each property type has:

* A fixed construction time

* A defined land usage

* A specific earning per operational time unit

* The challenge is to determine the best mix of properties that maximizes profit when only one property can be built at a time.

**🎯 Objective**

* Maximize total earnings within a given time limit n

* Choose the optimal combination of:

* Theatre (T)

* Pub (P)

* Commercial Park (C)

* Respect construction time constraints

* Output the count of each property type built

🧠 Approach
**1️⃣ Input**

A single integer n representing total available time units

**2️⃣ Decision Logic**

* Evaluate all possible combinations of properties

* Ensure total construction time does not exceed n

* Calculate total earnings for each valid combination

* Select the combination that produces maximum profit

**3️⃣ Output Format**
T: <count> P: <count> C: <count>

**🛠️ Technologies Used**

* Python

* Jupyter Notebook

* Basic Algorithms

* Greedy / Optimization Logic
