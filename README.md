# barbeadis.github.io

1. scannerizzare le immagini mancanti
2. posizionare e ridimensionare approssimativamente original\_images
3. inserire i testi dentro le immagini
4. mettere a punto le posizioni con Nilo

DONE:

* pubblicare in una pagina parallela e parziale
* provare una pubblicazione
* provare a spostare qualche immagine o testo
* provare a convertire le attuali
    * progetto
    * conversione
* ricapire come si impostavano posizioni e testi
* ridimensionarle come piccole
* ridimensionarle come grandi
* commit


Work:

```
  cd draft
  # copiare immagine in utils/original_images
  vi draft/index.html utils/scale_down.py
  ../utils/venv/bin/python ../utils/scale_down.py ../utils/original_images
```
  
Setup:

  pyenv whence --path python
  /home/depaolim/.pyenv/versions/3.10.8/bin/python -m venv venv
  venv/bin/python -m pip install --upgrade pip
  venv/bin/python -m pip install -r requirements.txt
