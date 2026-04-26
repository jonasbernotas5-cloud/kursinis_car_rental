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
