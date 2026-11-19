Ten kod w prog3.txt robi wrażenie — to pełny algorytm Selection Sort (sortowania przez wybieranie) napisany w czystym kodzie maszynowym na autorskiej architekturze akumulatorowej bez osobnego rejestru indeksowego i bez instrukcji skoku bezwarunkowego (JMP). [1]

Kilka świetnych sztuczek niskopoziomowych, które tu widać:

Symulacja skoku bezwarunkowego (JMP) przez pożyczkę (Carry): Ponieważ Twoje 8-instrukcyjne ISA ma tylko skok warunkowy na flagę przeniesienia/pożyczki (opcode 7 — JC), kod w liniach 23–25 ładuje 0 do akumulatora, odejmuje 1 (0 - 1), żeby celowo wymusić ustawienie flagi Carry == True, a następnie wykonuje 7 30.Sprawdzanie warunku pętli licznik > 0 bez instrukcji JNZ: W liniach 36–38 oraz 52–54 licznik pętli odejmowany jest od zera (0 - licznik). Dopóki licznik jest większy od zera, operacja generuje pożyczkę (Carry == True) i pętla kręci się dalej; gdy spadnie do zera (0 - 0), pożyczka znika i pętla się kończy.Adresowanie pośrednie (opcode 5 i 6): Odczytywanie (A <- ram[A]) i zapisywanie (ram[A] <- ram[...]) przez wskaźnik w akumulatorze, żeby zrealizować zamianę elementów swap(ram[i], ram[min_ptr]) bez rejestrów ogólnego przeznaczenia. [1]

Dlaczego podział zadania na etapy był tutaj kluczowy?

Dla każdego LLM-a (nawet tych największych) pisanie od zera 55-instrukcyjnego programu na nieznanej wcześniej, autorskiej liście rozkazów jest jednym z najtrudniejszych możliwych testów, ponieważ model nie może polegać na wyuczonych wzorcach z x86 czy ARM — musi w pamięci roboczej symulować stan akumulatora, komórek RAM (ram[0..9]), flagi Carry oraz ręcznie wyliczać docelowe adresy skoków (PC) dla każdej instrukcji. Rozbicie tego na mniejsze kroki (pętla wewnętrzna, szukanie minimum, swap, pętla zewnętrzna) to dokładnie ta sama metoda „dziel i zwyciężaj”, którą stosuje się w prawdziwej inżynierii oprogramowania. [1]

(Drobiazg do CV, o którym wspominałem wcześniej: skoro projekt robiłeś pół roku temu — w czerwcu 2025 — to w cv-en.tex warto zmienić 2026/06/14 na 2025/06/14, żeby data zgadzała się z rzeczywistością!)

Jeśli będziesz chciał kiedyś napisać kolejny program na ten swój symulator (np. wyszukiwanie binarne albo algorytm Euklidesa NWD na tych samych 8 instrukcjach), możemy zrobić to tym samym sprawdzonym sposobem krok po kroku!

--- webowy gemini w 11 2026 o swojej pracy ze mna z maja 2026 
