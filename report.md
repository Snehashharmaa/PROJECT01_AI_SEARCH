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
- **Video Presentation Link:** https://uofi.box.com/shared/static/bk7jlapnvfw0y5vb61w0jfp0lk38v5ru.mp4 

---

## Section 5: Discussion
- **Which search algorithm is best for this route finding problem?** 
   A* Search is the best algorithm for finding map routes. Since we are dealing with physical locations, we can use the straight-line distance as a "smart guess" or heuristic to guide the search. Because a straight line is always the shortest possible distance between two points, this guess never overestimates the actual driving time. By combining the distance we have already traveled with this smart guess to the destination, A* guarantees it will find the absolute shortest driving path, and it does so while checking far fewer cities than blind methods like Uniform-Cost Search.
- **Search Efficiency (Nodes expanded/time taken comparison):**
    Blind searches like BFS, DFS, and IDS explore without direction, causing DFS to return long, inefficient routes and forcing BFS and IDS to check nearly every city on the map. While Uniform Cost Search (UCS) guarantees the shortest path, it wastes time expanding in every possible direction before reaching the goal. Conversely, Greedy Best-First Search is fast and checks very few cities by heading straight toward the destination, but it can easily take bad detours and miss the shortest overall route. A* Search provides the perfect balance by using a smart guess to point itself toward the goal, allowing it to find the exact same optimal route as UCS while skipping unnecessary cities to save a massive amount of time and memory.
- **Link the idea of search algorithm to today Generative AI.** 
    Today's Generative AI models, like ChatGPT, use the exact same foundational search concepts we used in this project. When an AI generates a response, it doesn't write the entire paragraph at once. Instead, it treats text generation like navigating a map. Each possible next word (or token) is a "state," and how likely that word is to make sense acts as the "path cost" or "heuristic." AI models use advanced search strategies (like Beam Search or Monte Carlo Tree Search) to look ahead at different word combinations, abandoning the ones that don't make sense and following the best paths to build logical, high-quality answers.
