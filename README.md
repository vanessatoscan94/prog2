**Ausgangslage**  
Die Web-App soll für den Operations Research Unterricht an der FHS St.Gallen als anschauliches und interaktives Beispiel der Travelling-Salesman-Aufgabe dienen. Des Weiteren soll die Web-App so weit ausgeklügelt sein, dass sie auf der Website des Instituts für Modellbildung und Simulation eingebettet werden kann.
Die Travelling-Salesman Aufgabe besteht darin, eine Reihenfolge für den Besuch mehrerer Orte so zu wählen, dass keine Station ausser der ersten mehr als einmal besucht wird, die gesamte Reisestrecke des Handlungsreisenden möglichst kurz und die erste Station gleich der letzten Station ist.

**Funktion/Projektidee**   
Der User kann aus einer Dropdown-Liste eine TSP-Aufgabe auswählen. Die Aufgabenstellung besteht beispielsweise darin, dass eine Landkarte mit 10 – 50 markierten Städten gezeigt wird, z.B. eine Schweizerkarte mit allen 26 Kantonshauptstädte. Mittels einer Distanzmatrix kann die Distanz zwischen den Städte-Paaren berechnet werden.Für das Beispiel mit den 26 Kantonshauptstädte, umfasst die Tabelle 26 x 26 Zahlen. 
Nun soll der Benutzer in der Lage sein, über Klicke selbst eine Tour zu erstellen. Sobald der Benutzer eine gültige Tour “zusammengeklickt” hat, erscheint die Länge der ganzen Tour. Es sollte möglich sein, dass der Benutzer diese Tour abspeichern und ggf. ausdrucken kann. Ausserdem soll eine High-Score-Liste erstellt werden können, die auch Rückmeldung darüber gibt, wie weit die eingegeben Tour von der optimalen Tour entfernt ist. Als weiteres Feature soll die eingegeben Tour angepasst bzw. verbessert werden können.

**Workflow**  
**Dateneingabe**  
Die Dateneingabe erfolgt durch den User, in dem er eine Route auf der Landkarte einzeichnet.
**Datenverarbeitung/Speicherung**  
Mittels einer Distanzmatrix wird die Länge der eingegeben Route und der optimalen Route berechnet. Die Abweichung zwischen der optimalen und eingegeben Route wird auch berechnet und abgespeichert. Sie dient als Grundlage für die Erstellung des Ranking.  
**Datenausgabe**  	  
Als Output erscheint die Länge der eingegeben Route, die optimale Route, die Abweichung sowie das Ranking.  
**Projektteam:** Flurin Böni, Vanessa Toscan
