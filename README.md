# Διπλωματική εργασία
## Σύντομη περιγραφή
<p align="justify"> Το repository αυτό δημιουργήθηκε στο πλαίσιο της εκπόνησης της διπλωματικής εργασίας με τίτλο <b>"Μελέτη μηχανισμού αλληλεπίδρασης & ομαδοποίησης χρηστών στην εκπαίδευση με χρήση τεχνικών deep learning"</b> στο Εθνικό Μετσόβιο Πολυτεχνείο με απώτερο στόχο να συμπεριλάβει τον υλοποιημένο κώδικα Python που σχετίζεται μ' αυτήν.</p>

![cover.pdf](https://github.com/alexandrosst/Diploma-Thesis/blob/main/img.svg)

<p align="justify">Σκοπός της εργασίας είναι η κατασκευή ενός μηχανισμού αλληλεπίδρασης των μαθητών μιας σχολικής κοινότητας ως αποτέλεσμα της κοινής τους συμμετοχής σε μια σειρά από ομαδικές δραστηριότητες.</p>

<p align="justify">Η εργασία χωρίζεται σε δύο μέρη.</p>
<p align="justify">Στο <b>μέρος Ι</b> εξετάζεται η δημιουργία ενός τέτοιου μηχανισμό κατά τρόπο ισότιμο χωρίς τον κοινωνικό αποκλεισμό κανενός μαθητή. Για τη δημιουργία των αλληλεπιδράσεων λαμβάνονται υπόψη οι προσωπικές προτιμήσεις των μαθητών, η οποία ως πληροφορία θεωρείται προσπελάσιμη από ερωτηματολόγια με γνώμες και σκέψεις μαθητών. Κατασκευάζεται ένας γράφος προτιμήσεων για την προσομοίωση των αποτελεσμάτων ενός τέτοιου ερωτηματολογίου, ο οποίος λαμβάνεται υπόψη για τη δημιουργία των αλληλεπιδράσεων, οι οποίες εξίσου αποτυπώνονται σε γράφο εξελισσόμενο όμως στο χρόνο.</p>

<p align="justify">Στο <b>μέρος ΙΙ</b> εξετάζεται μια έμμεση πηγή πληροφορίας για τις προτιμήσεις των μαθητών που είναι η ανάλυση συναισθήματος συνομιλιών που συμμετέχουν. Προς αυτή την κατεύθυνση σχεδιάζεται ένα νευρωνικό δίκτυο για την ταξινόμηση κειμένου σε θετικό συναίσθημα, αρνητικό συναίσθημα ή ουδέτερο κάνοντας χρήση ενός προεκπαιδευμένου μοντέλου παραγωγής embeddings. Τελικά, κατασκευάζεται ένα συναισθηματικό προφίλ για κάθε χρήστη της συνομιλίας και υπολογίζεται μια εκτίμηση της έντασης της αλληλεπίδρασης των χρηστών.</p>

## Περιγραφή των αρχείων
<p align="justify">Περιλαμβάνει δύο υποκαταλόγους που αντιστοιχούν στα δύο επιμέρους μέρη της διπλωματικής.</p>

### Κατάλογος <a href=https://github.com/alexandrosst/Diploma-Thesis/tree/main/preference_interaction_graph>preference_interaction_graph</a>
<p align="justify">Ο κατάλογος αυτός σχετίζεται με το μέρος Ι της εργασίας. Περιλαμβάνει τα εξής αρχεία:</p>
<ul>
    <li><p align="justify"><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/preference_interaction_graph/preferenceGraph.ipynb>preferenceGraph.ipynb</a> ⇝ περιλαμβάνει τον κώδικα της υλοποίησης για την κατασκευή του γράφου προτίμησης των μαθητών που προσομοιώνει τα πορίσματα ενός ερωτηματολογίου.</p></li>
    <li><p align="justify"><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/preference_interaction_graph/interactionGraph.ipynb>interactionGraph.ipynb</a> ⇝ περιλαμβάνει τον κώδικα της υλοποίησης για την κατασκευή του γράφου αλληλεπίδρασης των μαθητών που χρησιμοποιεί τη γνώση του γράφου προτίμησης.</p></li>
</ul>

### Κατάλογος <a href=https://github.com/alexandrosst/Diploma-Thesis/tree/main/sentiment%20analysis>sentiment_analysis</a>
<p align="justify">Ο κατάλογος αυτός σχετίζεται με το μέρος ΙΙ της εργασίας. Περιλαμβάνει τα εξής αρχεία:</p>
<ul>
    <li><p align="justify"><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/chat_words.txt>chat_words.txt</a> ⇝ πρόκειται γι' αρχείο με συγκεντρωμένες συντομογραφίες του διαδικτυακού λόγου (π.χ. το "omg" αντιστοιχίζεται στο "oh my god", το "imo" αντιστοιχίζεται στο "in my opinion" κ.ά.).</p></li>
    <li><p align="justify"><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/phrases.xlsx>phrases.xlsx</a> ⇝ πρόκειται για αρχείο με συγκεντρωμένες φράσεις που σχετίζονται με τη σχολική πραγματικότητα. Η πλεονότητα αυτών δημιουργήθηκε με χρήση του Bing Chat.</p></li>
    <li><p align="justify"><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/train.csv>train.csv</a>, <a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/validation.csv>validation.csv</a>, <a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/test.csv>test.csv</a> ⇝ πρόκειται για αρχεία που προέρχονται από το επίσημο <a href=https://github.com/google-research/google-research/tree/master/goemotions>GoEmotions Dataset Repository</a>. Η μόνη διαφορά είναι η απομάκρυνση των δειγμάτων με διφορούμενο συναίσθημα ή με διπλή κατηγοριοποίηση (θετικό & ουδέτερο, θετικό & αρνητικό, αρνητικό & ουδέτερο) που είναι λίγα στο πλήθος. Επίσης, στο train.csv έχουν ενσωματωθεί και τα δείγματα από το αρχείο phrases.xlsx. Τέλος, διαφέρουν στο ότι έχουν υποστεί προεπεξεργασία στα κείμενά τους.</p></li>
    <li><p align="justify"><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/neural_network.ipynb>neural_network.ipynb</a> ⇝ πρόκειται για το αρχείο με τον κώδικα της υλοποίησης, δηλαδή για το νευρωνικό δίκτυο και τη συνάρτηση υπολογισμού της εκτίμησης έντασης αλληλεπίδρασης μεταξύ δύο μαθητών βασισμένη σε μια συνομιλία τους. Για την παραγωγή embeddings έγινε χρήση του προεκπαιδευμένου μοντέλου <a href=https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest>twitter-roberta-base-sentiment-latest</a>.</p></li>
</ul>

## Aπαιτήσεις
<ul>
    <li>Python 3.11.4</li>
    <li>Torch 2.0.1</li>
</ul>

## Παραδείγματα εκτέλεσης
### Περίπτωση 1η: Γράφος προτίμησης
Εργαζόμαστε στο αρχείο <a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/preference_interaction_graph/preferenceGraph.ipynb>preferenceGraph.ipynb</a>.

Για τη δημιουργία του γράφου προτίμησης και την αποθήκευσή του ως αρχείο `preferenceGraph.json` έχουμε:

```python
options = {
    "n" : 100, # number of students
    "maxPreferencesPerCategory" : 10 # maximum possible number of edges (student's thoughts) per opinion item
}

# create preference graph
G = createPreferenceGraph(**options) # G is a networkx DiGraph

# save preference graph in currect directory
saveGraphJson(G, "./preferenceGraph.json")
```

Κάθε ακμή του γράφου προτίμησης έχει δύο ειδών βάρη, το "opinion" με την αναλυτική περιγραφή της γνώμης και το "opinionItem" με το index αυτού της περιγραφής. Δηλαδή για μια ακμή έχουμε:

```python
u = ...
v = ...
print(G[u][v])
```

### Περίπτωση 2η: Γράφος αλληλεπίδρασης
Εργαζόμαστε στο αρχείο <a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/preference_interaction_graph/interactionGraph.ipynb>interactionGraph.ipynb</a>.

Για τη φόρτωση του γράφου προτίμησης από το αρχείο `./preferenceGraph.json` και τη δημιουργία του γράφου αλληλεπίδρασης έχουμε:

```python
path = "./preferenceGraph.json"

options = {
    "threshold" : 0.4, # threshold for probability
    "maxInteractions" : 4, # maximum possible number of interactions for a node
    "maxTimestamp" : 15 # number of snapshots
}

# create interaction graph
G = createInteractionGraph(preferenceGraph=readPreferenceGraph(path), **options)["graph"]
```

<p align="justify">Κάθε κόμβος έχει τρία βάρη, "Α", "Β", "C" που έχει το index της δραστηριότητας. Κάθε ακμή έχει ένα βάρος "weight" που έχει το index της δραστηριότητας. Έχουμε:</p>

```python
t = ... # timestamp
u = ... # node1
v = ... # node2

print(G[t][u][v]) # weights of edge (u,v)
print(G[t].nodes[u]) # weights of node u at timestamp t
print(G[t].nodes[v]) # weights of node v at timestamp t

```

### Περίπτωση 3η: Εκτίμηση έντασης αλληλεπίδρασης σε μια διαδικτυακή συνομιλία
Εργαζόμαστε στο αρχείο <a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/neural_network.ipynb>neural_network.ipynb</a>.

Για την εύρεση της έντασης αλληλεπίδρασης σε μια τυχαία συνομιλία έχουμε:

```python
# random chat between two students
dialogue = [
    "Hey, what's up? 😊",
    "Not much. I'm just really frustrated about the programming project we turned in yesterday. 😔",
    "Why is that? What happened? 😟",
    "I feel like you didn't do your part and it really hurt our grade. You were supposed to work on the front-end and you barely did anything. 😞",
    "What are you talking about? I worked really hard on the front-end! You were the one who was supposed to do the back-end and you didn't even finish it!",
    "That's not true! I finished everything on time and it was all working perfectly. You were the one who was slacking off and not contributing anything. 😠🤬",
    "I can't believe you're saying that! I worked just as hard as you did and I did everything I was supposed to do. You're just trying to blame me for your own mistakes. 😠👎🏽",
    "No, I'm not! You're the one who messed everything up and now we're both going to suffer because of it. I can't believe you're being so selfish and stubborn about this. 😠",
    "I'm not being selfish or stubborn! You're just trying to make me look bad so you can feel better about yourself. It's not going to work. We both know what really happened. 🤮",
    "I can't even talk to you right now. You're being so unreasonable and unfair. I thought we were friends, but I guess I was wrong. 😔",
    "I thought so too, but I guess I was wrong too. Maybe we should just work on our own projects from now on. It's obviously not working out between us."
]

# get the intensity of chat
create_sentimental_profile(trained_model, dialogue[::2], dialogue[1::2])
```

## Αναφορές
> Google Research. (2021). GoEmotions. GitHub. https://github.com/google-research/google-research/tree/master/goemotions

> CardiffNLP. (2022). Twitter RoBERTa-base Sentiment Analysis. Hugging Face. https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest