import streamlit as st
from load_data import load_all_tables
from graph_builder import build_graph
from llm_interface import process_query
from pyvis.network import Network
import tempfile
st.set_page_config(page_title="Graph Query System", layout="wide")
st.title("📊 Graph-Based Query System")
st.markdown("Explore business relationships using graph visualization and natural language queries.")
@st.cache_resource
def load_graph():
    tables = load_all_tables()
    graph = build_graph(tables)
    return graph
graph = load_graph()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔗 Graph Visualization")

    net = Network(height="650px", width="100%", bgcolor="#0e1117", font_color="white")

    color_map = {
        "sales_order": "#1f77b4",
        "order_item": "#ff7f0e",
        "product": "#2ca02c"
    }
    for node, data in graph.nodes(data=True):
        node_type = data.get("type", "")
        label = data.get("label", node)
        color = color_map.get(node_type, "gray")
        net.add_node(
            node,
            label=label,
            color=color,
            title=str(data.get("details", {}))
        )
    for source, target, data in graph.edges(data=True):
        net.add_edge(source, target, title=data.get("relation", ""))
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
    net.save_graph(tmp_file.name)
    with open(tmp_file.name, "r", encoding="utf-8") as f:
        html = f.read()
    st.components.v1.html(html, height=650)

with col2:
    st.subheader("💬 Chat Interface")
    st.info("💡 Try: 'top products', 'total orders', or 'trace order flow'")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Ask your question:")
        submit = st.form_submit_button("Send")
    if submit and user_input:
        st.session_state.messages.append(("user", user_input))
        response = process_query(user_input, graph)
        st.session_state.messages.append(("ai", response))
    for role, msg in st.session_state.messages:
        if role == "user":
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(msg)