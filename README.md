**Ausgangslage**  
Die Web-App soll für den Operations Research Unterricht an der FHS St.Gallen als anschauliches und interaktives Beispiel dienen, das den Studierenden die Traveling-Salesman-Aufgabenstellung näherbringt. Des Weiteren soll die Web-App so weit ausgeklügelt sein, dass sie auf der Website des Instituts für Modellbildung und Simulation eingebettet werden kann.


**Funktion/Projektidee**   
Der User kann aus einer Dropdown-Liste eine Aufgabe auswählen. Beispielsweise: «Verbinden Sie alle Schweizer Hauptstädte so, wie Sie das Gefühl haben, dass die Strecke am kürzesten ist.» Mittels einer Distanzmatrix kann die Distanz zwischen den Städte-Paaren berechnet werden. Für das Beispiel mit den 26 Kantonshauptstädte, umfasst die Tabelle 26 x 26 Zahlen. Die Städte werden auf der Karte vorgegeben. Sobald der Benutzer eine gültige Tour “zusammengeklickt” hat, erscheint die Länge der ganzen Tour. Es sollte möglich sein, dass der Benutzer diese Tour abspeichern und ggf. ausdrucken kann. Ausserdem soll eine High-Score-Liste erstellt werden können, die Rückmeldung darüber gibt, wer bis jetzt die kürzeste Tour zusammengeklickt hat. Es werden keine Touren optimiert. Anspruchsvolle Algorithmen sind somit nicht nötig.


**Workflow**  
**Dateneingabe**  
Die Dateneingabe erfolgt durch den User, in dem er eine Route auf der Landkarte einzeichnet.   

**Datenverarbeitung/Speicherung**  
Mittels einer Distanzmatrix wird die Länge der eingegeben Route berechnet. Es sollen zwei verschiedene Routenberechnungen auswählbar sein. Eine die, die Strecke anhand von der Luftlinie berechnet und eine, die bspw. die LKW-Fahrzeit berechnet. Für das werden zwei verschiedene Distanzmatrizen verwendet.    

**Datenausgabe**  	  
Als Output erscheint die Länge der eingegeben Route und das Ranking.    

**Projektteam:** Flurin Böni, Vanessa Toscan

![Alt-Text](Szenario.jpg "optionaler Titel")      


**Mockup:**  
![Alt-Text](Mockup.png "optionaler Titel")   



**Beispiel Aufgabenstellung:**  
Verbinden Sie Chur, St.Gallen, Bern und Zürich in einer Reihenfolge, damit eine möglichst kurze Strecke rauskommt. Der Start und das Ende ist in Chur.    
![Alt-Text](Aufgabe1.png "optionaler Titel")  


User 1 gibt folgendes ein:  
1. Chur nach SG → 92 km  
2. SG nach Zürich → 85 km  
3. Zürich nach Bern → 122 km  
4. Bern nach Chur → 244 km  

Gesamthaft: **543 km**    
Distanzen von http://kantone-staedte.infos-schweiz.ch/distanztabelle-schweizer-staedte.html    

![Alt-Text](Aufgabe2.png "optionaler Titel")  

User 2 gibt folgendes ein:  
1. Chur nach Bern → 244 km  
2. Bern nach SG → 160 km  
3. SG nach Zürich → 85 km  
4. Zürich nach Chur → 122 km  

Gesamthaft: **611 km**    
Distanzen von http://kantone-staedte.infos-schweiz.ch/distanztabelle-schweizer-staedte.html  

**Ranking:**  
**Platz 1**:User 1 → 543 km  
**Platz 2**: User 2 → 611 km 









