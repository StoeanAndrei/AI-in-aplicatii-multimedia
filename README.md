# AI-in-aplicatii-multimedia

Folosind modelul generativ “Stable Diffusion” din KerasCV, am generat o serie de imagini ce contin un tren de culoare violet, pe baza unei propozitii, text, anume “high quality realistic image of a violet train on the road”. Acest model generativ este unul destul de precis, eficient si puternic, prezentand avantaje precum viteze mari de redarea a imaginilor. Acest model generativ text-to-image este destul de interesant datorita calitatii inalte pe care o poate oferi. Singurul dezavantaj reprezinta cantitatea mare de resurse din procesor atunci cand ruleaza, din cate am inteles, datorat de calculele matematice avansate.

Modelul YOLOV5 folosit in detectia obiectelor din imagini este foarte exact. Avand in vedere modul in care a detectat trenul din imaginea mea, care nu este una realista, se descurca destul de bine. Acest lucru, din cate am inteles, se datoreaza impartirii pe sectiuni a imaginii, facand anumite predictii.

Spatiul de culoare asociat CIE XYZ este un spatiu ce descrie toate culorile vizibile de catre ochiul uma, spre deosebire de celelalte spatii de culoare precum RGB sau HSL ce se bazeaza pe o anumita metoda de reproducere a culorilor. Acest spatiu de culoare se obtine din spatial RGB prin normalizarea valorilor RGB pentru a obtine valori relative ale intensitatii culorilor.

Acest spatiu de culoare este folosit in transformarea imaginii decupate din imaginea principal, iar mai departe acesteia i se aplica o masca pentru a obtine doar culoarea violet. Dupa aplicarea acestui spatiu de culoare, am selectat doar pixelii dintr-un interval setat de catre mine. Dupa acest lucru, am aplicat masca de transfomrare ca mai apoi am convertit in spatiu RGB imaginea pentru a o salva.

Pentru a transforma masca intr-o imagine fara fundal am folosit metoda cv2.cvtColor din biblioteca OpenCV. Practic, pentru a aplica aceasta metoda am convertit fundalul imaginii in fundal gri, apoi am aplicat o tehnica de prag. Dupa, am impartit imaginea in 3 canale B, G si R de culoare ca ulterior sa le imbin intr-o imagine cu 4 canale RGBA(Alpha).
