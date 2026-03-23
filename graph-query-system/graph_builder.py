import networkx as nx

def build_graph(tables):
    G = nx.DiGraph()
    if "sales_order_headers" in tables:
        for _, row in tables["sales_order_headers"].iterrows():
            order_id = str(row["salesOrder"])

            G.add_node(
                f"order_{order_id}",
                type="sales_order",
                label=f"Order {order_id}",
                details=dict(row)
            )

    if "sales_order_items" in tables:
        for _, row in tables["sales_order_items"].iterrows():
            item_id = str(row["salesOrderItem"])
            order_id = str(row["salesOrder"])
            product_id = str(row["material"])

            item_node = f"item_{item_id}"
            order_node = f"order_{order_id}"
            product_node = f"product_{product_id}"

            G.add_node(
                item_node,
                type="order_item",
                label=f"Item {item_id}",
                details=dict(row)
            )

            G.add_node(
                product_node,
                type="product",
                label=f"Product {product_id}",
                details={"product_id": product_id}
            )

            G.add_edge(order_node, item_node, relation="has_item")
            G.add_edge(item_node, product_node, relation="belongs_to")

    print(f"✅ Graph built with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

    return G