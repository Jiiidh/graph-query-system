def process_query(query, graph):
    query = query.lower()
    allowed_keywords = ["order", "product", "sales", "billing", "delivery", "flow"]
    if not any(word in query for word in allowed_keywords):
        return "⚠️ This system is designed to answer dataset-related queries only."
    if "top" in query and "product" in query:
        from query_engine import top_products
        top = top_products(graph)
        result = "### 🔥 Top Products\n\n"
        for product, count in top:
            clean = product.replace("product_", "")
            result += f"- **Product {clean}** → {count} orders\n"
        return result

    elif "total" in query and "order" in query:
        from query_engine import total_orders
        return f"### 📊 Total Orders\n\n**{total_orders(graph)} orders found**"

    elif "trace" in query or "flow" in query:
        from query_engine import trace_order_flow
        flows = trace_order_flow(graph)
        result = "### 🔗 Sample Order Flow\n\n"
        for f in flows:
            result += f"- {f}\n"
        return result
    
    else:
        return "🤔 I understood your query partially. Try asking about orders, products, or flows."