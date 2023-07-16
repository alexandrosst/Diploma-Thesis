# Διπλωματική εργασία
## Σύντομη περιγραφή
<p align="justify"> Το repository αυτό δημιουργήθηκε στο πλαίσιο της εκπόνησης της διπλωματικής εργασίας με τίτλο <b>"Μελέτη μηχανισμού αλληλεπίδρασης & ομαδοποίησης χρηστών στην εκπαίδευση με χρήση τεχνικών deep learning"</b> με απώτερο στόχο να συμπεριλάβει τον υλοποιημένο κώδικα Python που σχετίζεται μ' αυτήν. </p>

![cover.pdf](https://github.com/alexandrosst/Diploma-Thesis/blob/main/img.svg)

<p align="justify">Σκοπός της εργασίας είναι η κατασκευή ενός μηχανισμού αλληλεπίδρασης των μαθητών μιας σχολικής κοινότητας ως αποτέλεσμα της κοινής τους συμμετοχής σε μια σειρά από ομαδικές δραστηριότητες.</p>

<p align="justify">Η εργασία χωρίζεται σε δύο μέρη.</p>
<p align="justify">Στο <b>μέρος Ι</b> εξετάζεται η δημιουργία ενός τέτοιου μηχανισμό κατά τρόπο ισότιμο χωρίς τον κοινωνικό αποκλεισμό κανενός μαθητή. Για τη δημιουργία των αλληλεπιδράσεων λαμβάνονται υπόψη οι προσωπικές προτιμήσεις των μαθητών, η οποία ως πληροφορία θεωρείται προσπελάσιμη από ερωτηματολόγια με γνώμες και σκέψεις μαθητών. Κατασκευάζεται ένας γράφος προτιμήσεων για την προσομοίωση των αποτελεσμάτων ενός τέτοιου ερωτηματολογίου, ο οποίος λαμβάνεται υπόψη για τη δημιουργία των αλληλεπιδράσεων, οι οποίες εξίσου αποτυπώνονται σε γράφο εξελισσόμενο όμως στο χρόνο.</p>

<p align="justify">Στο <b>μέρος ΙΙ</b> εξετάζεται μια έμμεση πηγή πληροφορίας για τις προτιμήσεις των μαθητών που είναι η ανάλυση συναισθήματος συνομιλιών που συμμετέχουν. Προς αυτή την κατεύθυνση σχεδιάζεται ένα νευρωνικό δίκτυο για την ταξινόμηση κειμένου σε θετικό συναίσθημα, αρνητικό συναίσθημα ή ουδέτερο κάνοντας χρήση ενός προεκπαιδευμένου μοντέλου παραγωγής embeddings. Τελικά, κατασκευάζεται ένα συναισθηματικό προφίλ για κάθε χρήστη της συνομιλίας και υπολογίζεται μια εκτίμηση της έντασης της αλληλεπίδρασης των χρηστών.</p>

## Περιγραφή των αρχείων
<p>Περιλαμβάνει δύο υποκαταλόγους που αντιστοιχούν στα δύο επιμέρους μέρη της διπλωματικής. Ο κατάλογος <a href=https://github.com/alexandrosst/Diploma-Thesis/tree/main/sentiment%20analysis>sentiment analysis</a> αντιστοιχεί στο μέρος ΙΙ της εργασίας. Περιλαμβάνει τα εξής αρχεία:</p>
<ul>
    <li><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/chat_words.txt>chat_words.txt</a>: <p align="justify">πρόκειται γι' αρχείο με συγκεντρωμένες συντομογραφίες του διαδικτυακού λόγου (π.χ. το omg αντιστοιχίζεται στο oh my god).</p></li>
    <li><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/phrases.xlsx>phrases.xlsx</a>: <p align="justify">πρόκειται γι' αρχείο με συγκεντρωμένες φράσεις που σχετίζονται με τη σχολική πραγματικότητα. Η πλεονότητα αυτών δημιουργήθηκε με χρήση του Bing Chat, αλλά αρκετές είναι προϊόν έμπνευσης του @alexandrosst.</p></li>
    <li><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/train.csv>train.csv</a>, <a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/validation.csv>validation.csv</a>, <a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/test.csv>test.csv</a>: <p align="justify">πρόκειται γι' αρχεία που προέρχονται από το επίσημο <a href=https://github.com/google-research/google-research/tree/master/goemotions>GoEmotions Dataset Repository</a>. Η μόνη διαφορά είναι η απομάκρυνση των δειγμάτων με διφορούμενο συναίσθημα ή με διπλή κατηγοριοποίηση (θετικό & ουδέτερο, θετικό & αρνητικό, αρνητικό & ουδέτερο) που είναι λίγα στο πλήθος. Επίσης, στο train.csv έχουν ενσωματωθεί και τα δείγματα από το αρχείο phrases.xlsx.</p></li>
    <li><a href=https://github.com/alexandrosst/Diploma-Thesis/blob/main/sentiment%20analysis/neural_network.ipynb>neural_network.ipynb</a>:<p align="justify">πρόκειται για τ' αρχείο με τον κώδικα της υλοποίησης με το νευρωνικό δίκτυο και τη συνάρτηση υπολογισμού της εκτίμησης έντασης αλληλεπίδρασης μεταξύ δύο μαθητών βασισμένη σε μια συνομιλία τους.</p></li>
</ul>




## Αναφορές
> Demszky, Dorottya and Movshovitz-Attias, Dana and Koenecke, Allison and Cowen, Alan and Nemade, Gaurav and Goyal, Naman and Jurafsky, Dan. "GoEmotions: A Dataset of Fine-Grained Emotions." arXiv preprint arXiv:2005.00547 (2020).