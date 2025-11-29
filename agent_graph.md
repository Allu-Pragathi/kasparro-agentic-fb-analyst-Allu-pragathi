# Agent Graph — Kasparro Agentic Facebook Analyst

```mermaid
flowchart TD
    A[User Query] --> B[Planner Agent]
    B --> C[Data Agent]
    C --> D[Insight Agent]
    D --> E[Evaluator Agent]
    E --> F{Validated?}
    F -->|yes| G[Creative Generator]
    F -->|no| D
    G --> H[Report Compiler]
```

### Planner Agent
Breaks user query into subtasks: load data, summarize, identify low-CTR segments, hypothesize, validate, create creatives.

### Data Agent
Loads dataset and produces summaries: ROAS trend, CTR by campaign, creative samples.

### Insight Agent
Generates hypotheses from summaries.

### Evaluator Agent
Quantitatively validates hypotheses using thresholds from config.

### Creative Generator
Produces headline/text/CTA suggestions for low-CTR campaigns based on dataset samples.
