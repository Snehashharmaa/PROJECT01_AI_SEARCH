# Project 1 Report: Intelligent Search Visualizer

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Selected Region:**`, `**Live Deployment URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information 
- **Name:** sneha sharma 
- **UID (netID):** sshar68
- **UIN:** 661090803

---

## Section 1: Selected City Region
- **Selected Region:** Illinois, USA

---

## Section 2: Map Graph Configuration
- **Total Cities Configured:** 22
- **Total Connection Edges:** 35
- **Graph Fully Connected:** Yes

---

## Section 3: Local Verification & Search Algorithms
*Check the algorithms you successfully ran and verified on your local development server by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Breadth-First Search (BFS)
- [x] Depth-First Search (DFS)
- [x] Uniform Cost Search (UCS)
- [x] Iterative Deepening Search (IDS)
- [x] Greedy Best-First Search (Greedy)
- [x] A* Search (A*)

---

## Section 4: Deployed and Presentation Information
- **Deployment Platform:** Render
- **Live Deployment URL:** https://project01-ai-search-b4ck.onrender.com/
- **Video Presentation Link:** [Provide an accessible link to your 5–7 minute video presentation]

---

## Section 5: Discussion
- **Which search algorithm is best for this route finding problem?** 
    Here are clear, detailed answers for Section 5: Discussion that you can paste directly into your report.md:Section 5: DiscussionWhich search algorithm is best for this route finding problem?A* Search is the best algorithm for this spatial route-finding problem. Because road connections represent real physical distances, the straight-line Haversine distance serves as an admissible heuristic ($h(n) \le h^*(n)$) that never overestimate actual travel distance. By combining cumulative edge costs with heuristic estimates ($f(n) = g(n) + h(n)$), A* guarantees finding the shortest path (optimality) while expanding significantly fewer nodes than uninformed methods like Uniform-Cost Search.
- **Search Efficiency (Nodes expanded/time taken comparison):**
    Uninformed algorithms like BFS, DFS, and IDS explore nodes blindly without direction, often expanding a large portion of the graph (e.g., expanding 15–20 nodes for distant routes) and suffering from higher runtimes or suboptimal paths (DFS). Uniform Cost Search (UCS) guarantees optimal path length but expands nodes uniformly in all directions. In contrast, informed algorithms like Greedy Best-First Search expand fewer nodes by strictly following the heuristic toward the goal, though it can yield suboptimal paths. A* achieves the best balance: it expands far fewer nodes than UCS while strictly guaranteeing the optimal shortest road distance.
- **Link the idea of search algorithm to today Generative AI.** 
    Modern Generative AI models (such as LLMs using Beam Search or Monte Carlo Tree Search in reasoning models like OpenAI o1/o3) rely on search principles to decode and select optimal output sequences. During text generation, auto-regressive models do not evaluate all possible completions at once; instead, they navigate a high-dimensional state space where words/tokens represent states and token probabilities serve as path costs/heuristics. Search algorithms guide the model to expand and prune candidate responses, ensuring coherent, highly probable, and reasoning-sound outputs.

