import networkx as nx
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def calculateProbability(item) :
    # preference
    if item == 0 or item == 1 :
        return 1
    # perception of preference
    elif item == 2 or item == 3 :
        return 0.7
    # avoidance
    elif item == 4 or item == 5 :
        return 0
    # perception of avoidance
    else :
        return 0.3


def calculateIndexes(prefGraph, snapshotGraph, numNodes) :

    # Direct Sociometric Indexes
    Sp = [0] * numNodes # incoming edges to a node - elections
    Pp = [0] * numNodes # incoming edges to a node - perceptions of elections
    Sn = [0] * numNodes # incoming edges to a node - rejections
    Pn = [0] * numNodes # incoming edges to a node - perceptions of rejections
    Rp = [0] * numNodes # number of cases - reciprocal elections
    Rn = [0] * numNodes # number of cases - reciprocal rejections
    Os = [0] * numNodes # number of cases - feeling opposition (election & rejection)
    Ep = [0] * numNodes # outcoming edges from a node - elections
    En = [0] * numNodes # outcoming edges from a node - rejections
    Pap = [0] * numNodes # number of cases - have perception of election and get election
    Pan = [0] * numNodes # number of cases - have perception of rejection and get rejection

    def isReciprocal(node1, node2, weight) :
        for u, v, data in prefGraph.edges(node2, data=True) :
            if v == node1 and data["questionItem"] == weight :
                return True
        return False

    
    for u, v, data in prefGraph.edges(data=True) :
        if snapshotGraph.has_edge(u, v) :
            if data["questionItem"] in {0, 1}:
                Sp[v] += 1
                Ep[u] += 1
            elif data["questionItem"] in {2, 3} :
                Pp[v] += 1
            elif data["questionItem"] in {4, 5} :
                Sn[v] += 1
                En[u] += 1
            else :
                Pn[v] += 1 
    

    for u, v, data in prefGraph.edges(data=True) :        
        if snapshotGraph.has_edge(u, v) :
            if data["questionItem"] in {0, 1} :
                if isReciprocal(u, v, data["questionItem"]) :
                    Rp[u] += 1
                elif isReciprocal(u, v, data["questionItem"] + 4) :
                    Os[u] += 1
                else :
                    None
            elif data["questionItem"] in {4, 5} :
                if isReciprocal(u, v, data["questionItem"]) :
                    Rn[u] += 1
                elif isReciprocal(u, v, data["questionItem"] - 4) :
                    Os[u] += 1
                else :
                    None
            elif data["questionItem"] in {2, 3} :
                if isReciprocal(u, v, data["questionItem"] - 2) :
                    Pap[u] += 1
                else :
                    None
            else :
                if isReciprocal(u, v, data["questionItem"] - 2) :
                    Pan[u] += 1
                else :
                    None

                
    #Compound Sociometric Indexes
    #Individual
    popularity = [item / (2*(numNodes - 1)) for item in Sp] 
    antipathy = [item / (2*(numNodes - 1)) for item in Sn]
    affectiveConnection = [item1 / item2 if item2 != 0 else 0 for item1, item2 in zip(Rp, Sp)]
    sociometricStatus = [(item1 + item2 - item3 - item4) / (4*(numNodes - 1)) for item1, item2, item3, item4 in zip(Sp, Pp, Sn, Pn)]
    positiveExpansion = [item / (2*(numNodes - 1)) for item in Ep]
    negativeExpansion = [item / (2*(numNodes - 1)) for item in En]
    realisticPerception = [(item1 + item2) / (item3 + item4) if (item3 + item4) != 0 else 0 for item1, item2, item3, item4 in zip(Pap, Pan, Sp, Sn)]
    
    
    #Group
    association = sum(Rp) / (2*numNodes* (numNodes - 1))
    dissociation = sum(Rn) / (2*numNodes * (numNodes - 1))
    s = sum(Sp)
    cohesion =  sum(Rp) / s if s != 0 else 0
    socialIntensity = (sum(Sp) + sum(Sn)) / (2*numNodes*(numNodes - 1))

    
    return {
        "individual": 
            {
            "popularity": np.average(popularity),
            "antipathy": np.average(antipathy),
            "affective connection": np.average(affectiveConnection),
            "sociometric status": np.average(sociometricStatus),
            "positive expansion": np.average(positiveExpansion),
            "negative expansion": np.average(negativeExpansion),
            "realistic perception": np.average(realisticPerception)
            },
        "group":
            {
                "association": association,
                "dissociation": dissociation,
                "cohesion": cohesion,
                "social intensity": socialIntensity
            }
        }


def analyzeQuiz(prefGraph, threshold, numNodes) :
    def findProbBetween(node1, node2) :
        edges_node1_to_node2 = [calculateProbability(data["questionItem"]) for u, v, data in prefGraph.edges(node1, data=True) if v == node2]
        edges_node2_to_node1 = [calculateProbability(data["questionItem"]) for u, v, data in prefGraph.edges(node2, data=True) if v == node1]

        if len(edges_node1_to_node2) == 0 and len(edges_node2_to_node1) == 0 :
            return None
        elif len(edges_node1_to_node2) == 0 :
            return np.average(edges_node2_to_node1)
        elif len(edges_node2_to_node1) == 0 :
            return np.average(edges_node1_to_node2)
        else :
            return np.average([np.average(edges_node1_to_node2), np.average(edges_node2_to_node1)])        
    
    #dictionary {edge : probability of existing in the Preference Graph}
    edgesProbabilities = {}
    
    #examine edges between nodes in Preference Graph
    #calculate probability. How strong is the connection between people?
    for node in range(numNodes) :
        for other in range(node + 1, numNodes) :
            prob = findProbBetween(node, other)
            if prob is not None :
                edgesProbabilities[(node, other)] = prob

    #find possible peers for a student
    #step 1: find connecting links with prob < threshold
    possiblePeers = [[] for _ in range(numNodes)]       
    for edge, prob in edgesProbabilities.items() :
        if prob < threshold :
            possiblePeers[edge[0]].append(edge[1])
            possiblePeers[edge[1]].append(edge[0])

    #step 2: keep all the other nodes as possible peers to interact with
    possiblePeers = list(map(lambda item : list(set(range(numNodes)) - set(item[1] + [item[0]])), enumerate(possiblePeers)))
    
    for node, peers in enumerate(possiblePeers) :
        d = dict()
        for peer in peers :
            try :
                d[peer] = edgesProbabilities[(min(node, peer), max(node, peer))]
            except :
                d[peer] = 1 
        possiblePeers[node] = d
    
    return possiblePeers


def calculateIntensityForSnapshot(snapshotGraph, numNodes) :
    total = 0
    for node in range(numNodes) :
        count, sum = (0, 0)
        for u, v, data in snapshotGraph.edges(node, data=True) :
            count += 1
            sum += data["weight"]
        total += count*sum
    return total


def createSnapshot(numNodes, maxInteractions, possiblePeers) :

    G = nx.Graph()
    G.add_nodes_from(range(numNodes))
    
    for node in range(numNodes) :
        achievablePeers = [u for u in possiblePeers[node] if maxInteractions > G.degree(u)]
        possibleInteractions = maxInteractions - G.degree(node)
        interactions = min(len(achievablePeers), possibleInteractions, 3)
        
        if interactions == 0 :
            continue
        else :
            peers = list(np.random.choice(achievablePeers, size=interactions, replace=False))

            counter = dict.fromkeys(["A", "B", "C"], 0)
            counter.update(Counter([e[2]["weight"] for e in G.edges(data=True)]))
            weights = [key for key, value in sorted(counter.items(), key=lambda item: item[1])][:interactions]
            

            for peer, weight in zip(peers, weights) :
                G.add_edge(node, peer, weight=weight)

    for node in range(numNodes) :
        G.nodes[node]["A"] = None
        G.nodes[node]["B"] = None
        G.nodes[node]["C"] = None

    activitiesIndex = {"A": [1, 2], "B": [3, 4], "C": [5, 6]}
    edgesToRemove = []

    for u, v, d in G.edges(data="weight") :
        node1 = G.nodes[u][d]
        node2 = G.nodes[v][d]
        if node1 is None and node2 is None :
            activity = np.random.choice(activitiesIndex[d])
            G.nodes[u][d] = activity
            G.nodes[v][d] = activity
            G[u][v]["weight"] = activity
        elif node1 is not None and node2 is not None:
            edgesToRemove.append((u,v))
        else :
            activity = node1 or node2    
            G.nodes[u][d] = activity
            G.nodes[v][d] = activity
            G[u][v]["weight"] = activity 

    
    G.remove_edges_from(edgesToRemove)
   

    return G


def getActivity(index) :
    activities = ["to share content, chat in a social network platform",
            "to participate in debate/group discussion & presentation",
            "to play games",
            "to study in group or work on collaborative projects",
            "to be volunteers",
            "to be teammates in a sports team"]
    
    return activities[index-1]


def findActivitiesStatistics(G) :
    nodesPerActivity = dict.fromkeys(range(1, 7), 0)
    for node in G.nodes() :
        for activity in G.nodes[node].values() :
            if activity is not None :
                nodesPerActivity[activity] += 1

    fig = plt.figure(figsize = (12, 5))
    activities = ["intensity: 1\n\nto share content,\nchat in a social\nnetwork platform",
            "intensity: 2\n\nto participate\nin debate/group\ndiscussion\n& presentation",
            "intensity: 3\n\nto play games",
            "intensity: 4\n\nto study in group\nor work on\ncollaborative projects",
            "intensity: 5\n\nto be volunteers",
            "intensity: 6\n\nto be teammates\nin a sports team"]
    plt.bar(activities, nodesPerActivity.values(), color ="#3a3b95", width = 0.4)
    plt.grid(True)
    plt.xlabel("activity type")
    plt.ylabel("No. of nodes")
    plt.title("No. of nodes = f(activity type)")
    plt.show()

    nodesPerActivityEngagement = dict.fromkeys(range(4), 0)
    for node in G.nodes() :
        numberOfActivities = sum(item is not None for item in G.nodes[node].values())
        nodesPerActivityEngagement[numberOfActivities] += 1
    activityEngagement = ["activities: 0", 
                          "activities: 1", 
                          "activities: 2", 
                          "activities: 3"]
    plt.bar(activityEngagement, nodesPerActivityEngagement.values(), color ="#3a3b95", width = 0.4)
    plt.grid(True)
    plt.xlabel("No. of activities")
    plt.ylabel("No. of nodes")
    plt.title("No. of nodes = f(activity engagement)")
    plt.show()
