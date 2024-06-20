import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define the nodes and their positions
nodes = {
    "User Searches": (0, 0),
    "User Views Details": (1, 0),
    "User Books a Room": (2, 0),
    "Payment Processed": (3, 0),
    "Booking Confirmation Sent": (4, 0)
}

# Add nodes to the graph
for node, pos in nodes.items():
    G.add_node(node, pos=pos)

# Define the edges
edges = [
    ("User Searches", "User Views Details"),
    ("User Views Details", "User Books a Room"),
    ("User Books a Room", "Payment Processed"),
    ("Payment Processed", "Booking Confirmation Sent")
]

# Add edges to the graph
G.add_edges_from(edges)

# Get positions for the nodes
pos = nx.get_node_attributes(G, 'pos')

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue')

# Draw the edges
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='->', arrowsize=20)

# Draw the labels
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

# Create a legend
search_patch = mpatches.Patch(color='skyblue', label='Search for Hotels')
view_patch = mpatches.Patch(color='skyblue', label='View Hotel Details')
book_patch = mpatches.Patch(color='skyblue', label='Book a Room')
payment_patch = mpatches.Patch(color='skyblue', label='Payment Processing')
confirmation_patch = mpatches.Patch(color='skyblue', label='Send Booking Confirmation')

plt.legend(handles=[search_patch, view_patch, book_patch, payment_patch, confirmation_patch], loc='lower center', bbox_to_anchor=(0.5, -0.1), ncol=2)

# Remove axis
plt.axis('off')

# Display the plot
plt.title("Complete User Case Story Process Diagram")
plt.show()
