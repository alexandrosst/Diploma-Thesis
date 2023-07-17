# Διπλωματική εργασία
## Σύντομη περιγραφή
<p align="justify"> Το repository αυτό δημιουργήθηκε στο πλαίσιο της εκπόνησης της διπλωματικής εργασίας με τίτλο <b>"Μελέτη μηχανισμού αλληλεπίδρασης & ομαδοποίησης χρηστών στην εκπαίδευση με χρήση τεχνικών deep learning"</b> με απώτερο στόχο να συμπεριλάβει τον υλοποιημένο κώδικα Python που σχετίζεται μ' αυτήν. </p>

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
    <li><p align="justify"><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/phrases.xlsx>phrases.xlsx</a> ⇝ πρόκειται για αρχείο με συγκεντρωμένες φράσεις που σχετίζονται με τη σχολική πραγματικότητα. Η πλεονότητα αυτών δημιουργήθηκε με χρήση του Bing Chat, αλλά αρκετές είναι προϊόν έμπνευσης του συγγραφέα της εργασίας.</p></li>
    <li><p align="justify"><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/train.csv>train.csv</a>, <a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/validation.csv>validation.csv</a>, <a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/test.csv>test.csv</a> ⇝ πρόκειται για αρχεία που προέρχονται από το επίσημο <a href=https://github.com/google-research/google-research/tree/master/goemotions>GoEmotions Dataset Repository</a>. Η μόνη διαφορά είναι η απομάκρυνση των δειγμάτων με διφορούμενο συναίσθημα ή με διπλή κατηγοριοποίηση (θετικό & ουδέτερο, θετικό & αρνητικό, αρνητικό & ουδέτερο) που είναι λίγα στο πλήθος. Επίσης, στο train.csv έχουν ενσωματωθεί και τα δείγματα από το αρχείο phrases.xlsx. Τέλος, διαφέρουν στο ότι έχουν υποστεί προεπεξεργασία στα κείμενά τους.</p></li>
    <li><p align="justify"><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/neural_network.ipynb>neural_network.ipynb</a> ⇝ πρόκειται για το αρχείο με τον κώδικα της υλοποίησης, δηλαδή για το νευρωνικό δίκτυο και τη συνάρτηση υπολογισμού της εκτίμησης έντασης αλληλεπίδρασης μεταξύ δύο μαθητών βασισμένη σε μια συνομιλία τους. Για την παραγωγή embeddings έγινε χρήση του προεκπαιδευμένου μοντέλου <a href=https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest>twitter-roberta-base-sentiment-latest</a>.</p></li>
</ul>




## Αναφορές
> Demszky, Dorottya and Movshovitz-Attias, Dana and Koenecke, Allison and Cowen, Alan and Nemade, Gaurav and Goyal, Naman and Jurafsky, Dan. "GoEmotions: A Dataset of Fine-Grained Emotions." arXiv preprint arXiv:2005.00547 (2020).