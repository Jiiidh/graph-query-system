def top_products(graph):
    product_count = {}
    for u, v, data in graph.edges(data=True):
        if data.get("relation") == "belongs_to":
            product_count[v] = product_count.get(v, 0) + 1
    sorted_products = sorted(product_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_products[:5]

def total_orders(graph):
    return sum(1 for _, d in graph.nodes(data=True) if d.get("type") == "sales_order")

def trace_order_flow(graph):
    flows = []
    for node, data in graph.nodes(data=True):
        if data.get("type") == "sales_order":
            order = node
            items = list(graph.successors(order))
            for item in items:
                products = list(graph.successors(item))
                for product in products:
                    flows.append(f"{order} → {item} → {product}")

    return flows[:5]  