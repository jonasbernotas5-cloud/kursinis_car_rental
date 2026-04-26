# Automobilių Nuomos Sistema

Šis projektas yra objektinio programavimo (OOP) kursinis darbas, parašytas Python kalba. Sistema skirta valdyti transporto priemonių parką, klientų nuomas bei užtikrinti duomenų išlikimą naudojant JSON failus.

## Funkcijos

* **Transporto priemonių valdymas**: Sistema leidžia administruoti trijų tipų transporto priemones: automobilius, sunkvežimius ir motociklus. Kiekvienas tipas turi unikalias savybes (pvz., sėdimos vietos, keliamoji galia), kurios įtakoja galutinę nuomos kainą.
* **Klientų sistema**: Klientų registracija su unikaliais ID ir nuomojamų transporto priemonių sąrašais.
* **Nuomos procesas**: Transporto priemonių nuoma ir grąžinimas, automatiškai skaičiuojant kainą pagal transporto priemonės tipą.
* **Duomenų išsaugojimas**: Programa fiksuoja, kurios priemonės yra laisvos, o kurios – išnuomotos. Ši informacija išlieka net ir išjungus programą. Yra galimybė išsaugoti visą sistemos būseną t.y. transporto priemonių ir klientų sąrašus su jū duomenimis  į `data.json` failą ir ją vėl užkrauti iš failo.
* **Validacija**: Sistema neleidžia įvesti klaidingų duomenų. Pavyzdžiui, negalima sukurti kliento su neteisingu ID formatu arba nustatyti neigiamos nuomos kainos.

##  Naudotos OOP technologijos

* **Enkapsuliacija**: Naudojami `@property` ir `@setter` dekoratoriai duomenų apsaugai ir validacijai.<img width="400" height="300" alt="Ekrano kopija 2026-04-26 210430" src="https://github.com/user-attachments/assets/78008323-1b59-4804-ad19-a67cff4dc965" />

* **Paveldėjimas**: Visos transporto priemonės paveldi bazinę `Vehicle` klasę iš jos pasiėma `get_total_price` ir `get_info` metodus.
* **Polimorfizmas**: Kiekviena klasė (`Car`, `Truck`, `Motorcycle`) savaip realizuoja `get_total_price` ir `get_info` metodus. Kiekviena klasė turi sau atskira unikalų parametra kuri naudoja skaičiuoti `get_total_price` Car klasė turi seats, Motorcycle klasė turi engine_capacity ir Truck klasė turi load_capacity.
 
  Car Klasėje:<img width="556" height="138" alt="Ekrano kopija 2026-04-26 211216" src="https://github.com/user-attachments/assets/aabf0b30-f8c2-4a7e-ba43-e8ade386777b" />
  
  Motorcycle Klasėje:<img width="743" height="142" alt="Ekrano kopija 2026-04-26 211433" src="https://github.com/user-attachments/assets/c846fe22-c178-4945-a4cb-068e671a0084" />
  
  Truck Klasėje:<img width="706" height="130" alt="image" src="https://github.com/user-attachments/assets/a62747f7-9523-49c6-896b-9b1191962c90" />



* **Abstrakcija**: `Vehicle` klasė yra abstrakti (naudojama `ABC` biblioteka) ir turi abstract metodą `get_total_price`.
  Abstrakti klasė:<img width="563" height="145" alt="image" src="https://github.com/user-attachments/assets/1f0e0bc8-ce88-4678-9c49-b6f77bb06605" />

  Abstraktus metodas:<img width="323" height="78" alt="image" src="https://github.com/user-attachments/assets/ba04613c-4b81-451e-9e81-d9d448d7e678" />


* **Projektavimo šablonai (Design Patterns)**: Panaudotas **Factory Pattern** objektų kūrimui per `Factory` klasę. Transporto priemonės kuriamos naudojant centralizuotą gamyklos metodą, kuris užtikrina kodo lankstumą ir lengvą naujų tipų pridėjimą ateityje.<img width="845" height="263" alt="image" src="https://github.com/user-attachments/assets/3f0962de-ef28-42a5-96c9-73100fa81273" />


## Diegimas ir paleidimas

1. Įsitikinkite, kad turite įsidiegę bent jau Python 3.6+ bet rekomenduojama naudoti 3.11
2. Atsisiųskite projekto failus.
3. Paleiskite pagrindinę programą:
   ```bash
   python kursinis_car_rental.py

##  Testavimas 

Sistemos stabilumui užtikrinti buvo paruoštas platus Unit testų rinkinys naudojant standartinę Python `unittest` biblioteką. Iš viso realizuota 21 testas, apimančių visas kritines sistemos dalis.

### Patikros sritys:
* **Duomenų validacija**: Tikrinama, ar sistema tinkamai reaguoja į neteisingus valstybinius numerius, neigiamas kainas bei klaidingus klientų ID formatus.
* **Kainų skaičiavimo polimorfizmas**: Testuojama, ar kiekviena transporto priemonės klasė (`Car`, `Truck`, `Motorcycle`) teisingai apskaičiuoja galutinę nuomos kainą pagal savo unikalią formulę.
* **Nuomos logika**: Tikrinama, ar automobilis tampa „užimtas“ po nuomos, ar neleidžiama nuomotis jau užimtos transporto priemonės ir ar klientas sėkmingai mato savo nuomų sąrašą.
* **Duomenų išsaugojimas (JSON)**: Testuojama, ar duomenys teisingai įrašomi į failą ir ar po užkrovimo visos objektų savybės bei būsenos išlieka nepakitusios.

### Testų paleidimas:
Paleidus `test_kursinis_car_rental.py` gauname tokį vaizdą:<img width="387" height="101" alt="image" src="https://github.com/user-attachments/assets/7f83f5b0-5378-4ac4-8529-73262df55050" />



## Rezultatai 

* **Sėkmingas testavimas**: Visi 21 parengtų unit testų sėkmingai praėjo patikrą, patvirtindami, kad transporto priemonių nuomos, kainų skaičiavimo ir duomenų validacijos logika veikia be klaidų.
* **Duomenų išsaugojimas**: Įgyvendintas pilnas duomenų serializavimas į JSON formatą, užtikrinantis, kad visa sistemos būsena (automobilių užimtumas ir klientų nuomos) išlieka po programos perkrovimo.
* **Iššūkis – duomenų vientisumas**: Didžiausias iššūkis buvo užtikrinti teisingą ryšių atstatymą tarp klientų ir transporto priemonių kraunant duomenis iš failo, tačiau tai buvo sėkmingai išspręsta susiejant objektus pagal unikalius numerius.
* **Validacijos stabilumas**: Panaudojus Python `@property` dekoratorius, sukurta patikima apsauga nuo neteisingų duomenų įvedimo, kuri automatiškai sustabdo programą ir pateikia informatyvius klaidų pranešimus.
* **Kodo lankstumas**: Panaudotas Factory projektavimo šablonas leido lengvai integruoti naujus transporto priemonių tipus (motociklus ir sunkvežimius) nekeičiant pagrindinės sistemos logikos.

##  Išvados

Šio kursinio darbo metu buvo sėkmingai sukurta funkcionuojanti transporto priemonių nuomos sistema, atitinkanti visus objektinio programavimo (OOP) reikalavimus.

### Pagrindiniai pasiekimai:
* **Tikslų įgyvendinimas**: Sukurta lanksti architektūra, leidžianti valdyti skirtingų tipų transporto priemones (automobilius, sunkvežimius, motociklus) bei automatizuoti nuomos kainų skaičiavimą naudojant polimorfizmą.
* **Darbo rezultatas**: Parengta stabili programa su integruota duomenų saugykla (JSON formatu) ir išsamiu 15+ Unit testų rinkiniu, užtikrinančiu kodo patikimumą.
* **OOP principų taikymas**: Praktiškai pritaikyti abstrakcijos, paveldėjimo ir enkapsuliacijos principai bei „Factory“ projektavimo šablonas, kas padidino kodo skaitomumą ir plečiamumą.

### Ateities perspektyvos:
* **Vartotojo sąsaja**: Programą būtų galima papildyti grafine sąsaja (GUI) arba žiniatinklio (Web) sąsaja, kad sistema būtų patogesnė galutiniam vartotojui.
* **Duomenų bazės integracija**: Ateityje JSON failus būtų tikslinga pakeisti SQL duomenų baze (pvz., SQLite ar PostgreSQL) didesniam duomenų kiekiui valdyti.
* **Papildoma logika**: Galima įdiegti nuolaidų sistemas lojaliems klientams bei transporto priemonių techninės priežiūros (serviso) sekimo modulį.
