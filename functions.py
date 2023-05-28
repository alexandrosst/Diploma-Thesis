import networkx as nx
import numpy as np

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
            sum += data["interaction_index"]
        total += count*sum
    return total


def createSnapshot(numNodes, maxInteractions, degrees, possiblePeers, activitiesCount) :
    # numberOfInteractions = np.random.choice([2,3])
    numberOfInteractions = 1
    G = nx.Graph()
    G.add_nodes_from(range(numNodes))

    # find for a node how many additional interactions we could add
    possibleInteractions = [0]*numNodes
    for node in range(numNodes) :
        possibleInteractions[node] = maxInteractions - degrees[node]
        if possibleInteractions[node] <= 0 :
            possibleInteractions[node] = 0
        else :
            possibleInteractions[node] = min(numberOfInteractions, possibleInteractions[node])
    
    for node in range(numNodes) :
        if possibleInteractions[node] <= 0 :
            continue
        
        #choose randomly from possible peers
        temp = [u for u in possiblePeers[node].keys() if possibleInteractions[u] >= 1 and not(G.has_edge(u, node))]
        peers = list(np.random.choice(temp, size=possibleInteractions[node], replace=False))

        peers.sort(key=possiblePeers[node].get, reverse=True)
        
        #split possible ways of interaction in sublists and choose randomly an activity from each sublist
        weights = [np.random.choice(sublist) for sublist in np.array_split(range(activitiesCount), possibleInteractions[node])]
        
        weights.sort(reverse=True)

        #add new interaction to the graph
        for peer, weight in zip(peers, weights) :
            G.add_edge(node, peer, interaction_index=weight)
            possibleInteractions[node] = max(possibleInteractions[node] - 1, 0)
            possibleInteractions[peer] = max(possibleInteractions[peer] - 1, 0)
            # if G.has_edge(node, peer) :
            #     G[node][peer]["interaction_index"] = round(0.5*(weight + G[node][peer]["interaction_index"]))
            # else :
            #     G.add_edge(node, peer, interaction_index=weight)
        # print(possibleInteractions)        
    return G


def getActivity(index) :
    activities = ["to share content, chat in a social network platform",
            "to participate in debate/group discussion & presentation",
            "to play games",
            "to study in group or work on collaborative projects",
            "to be volunteers",
            "to be teammates in a sports team"]
    
    return activities[index]

