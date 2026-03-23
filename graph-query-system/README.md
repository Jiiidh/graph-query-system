# Graph-Based Context Query System

## Overview
This project builds a context graph system that transforms fragmented SAP Order-to-Cash (O2C) data into an interconnected graph and enables natural language querying through an intelligent chat interface.

The goal is to make it easy to trace relationships across orders, deliveries, billing, and products — something that is difficult in traditional relational tables.
---
## Key Insight

Traditional relational systems make it difficult to trace multi-step business flows.

This system solves that by:
- Converting tabular data into a graph
- Enabling direct traversal across entities
- Supporting natural language queries over relationships
---
## Architecture

### 1. Data Layer
- 19 SAP O2C dataset tables loaded using Pandas (JSONL format)
- Includes:
  - Sales Orders
  - Deliveries
  - Billing Documents
  - Payments
  - Products
  - Customers
---
### 2. Graph Layer
- Built using NetworkX
- Nodes represent business entities:
  - SalesOrder
  - OrderItem
  - Product
- Edges represent relationships:
  - SalesOrder → OrderItem (has_item)
  - OrderItem → Product (belongs_to)
This structure enables efficient traversal across business processes.
---
### 3. Query Engine
- Converts user queries into graph operations
- Implements:
  - Aggregation (top products, total orders)
  - Graph traversal (order → item → product)
- Supports flow tracing across entities
---
### 4. Natural Language Interface
- Lightweight intent detection system
- Maps user queries to graph operations
- Designed to be extendable to real LLM APIs (Gemini/OpenRouter)
---
### 5. UI Layer
- Built using Streamlit
- Left panel: Interactive graph visualization (Pyvis)
- Right panel: Chat interface for querying
---
## Database Choice

**NetworkX + Pandas**
Chosen because:
- No external database setup required
- Fast in-memory graph traversal
- Flexible for prototyping graph-based systems
---
## Guardrails

The system restricts queries to dataset-related topics:
- Keyword-based validation
- Rejects unrelated queries
- Returns safe fallback responses

Example:
> "This system only answers dataset-related queries."
---
## Example Queries

- "Which products are most ordered?"
- "Total orders"
- "Trace order flow"
---
## Demo
👉 Add your deployed link here: