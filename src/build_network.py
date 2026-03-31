import pandas as pd
import networkx as nx
from itertools import combinations

def build_user_network(file_path, max_thread_size=None):
    df = pd.read_csv(file_path)

    # Create unique thread ID
    df["thread_id"] = (
        df["page_name"].astype(str) + "||" + 
        df["thread_subject"].astype(str)
    )

    G = nx.Graph()

    # Add nodes
    users = df["username"].unique()
    G.add_nodes_from(users)

    grouped = df.groupby("thread_id")

    for thread, group in grouped:
        thread_users = group["username"].unique()

        # Optional safety cap
        if max_thread_size and len(thread_users) > max_thread_size:
            continue

        for u1, u2 in combinations(thread_users, 2):
            if G.has_edge(u1, u2):
                G[u1][u2]["weight"] += 1
            else:
                G.add_edge(u1, u2, weight=1)

    return G