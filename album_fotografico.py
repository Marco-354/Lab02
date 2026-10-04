def carica_da_file(file_path):
  try:
      with open(file_path, "r") as file:
          next(file)
          album = {}
          for riga in file:
              riga = riga.strip().split(",")
              anno = riga[4]
              foto = riga
              if anno not in album.keys():
                  album[anno] = []
                  album[anno].append(foto)
              else:
                  album[anno].append(foto)
      return album
  except FileNotFoundError:
      return None
#^^crea album come dizionario con chiave anno a cui corrispondono nfoto


def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
   foto=( codice, titolo, autore, mese, anno)
   anno_str=str(anno)
   if mese<1 or mese>12:
       return None
   for lista_foto in album.values():
       for f in lista_foto:
           if f[0] == codice:
               return None
   if anno_str not in album.keys():
       album[anno_str] = []
   album[anno_str].append(foto)
   try:
       with open(file_path, "a") as FileFoto:
           FileFoto.write(f"\n{codice},{titolo},{autore},{mese},{anno_str}")
   except FileNotFoundError:
       return None
   return foto
#^^permette di aggiungere foto ad album: -controlla se anno di foto da aggiungere è gia presente
# in album e in caso aggiunge anno
# -se anno gia presente aggiunge semplicemente foto
# -- inoltre scrive informazioni di foto su file indicato)


def cerca_foto(album, codice):
   for foto in album.values():
       for elemento_foto in foto:
               if elemento_foto[0]==codice:
                       codice=elemento_foto[0]
                       titolo = elemento_foto[1]
                       autore = elemento_foto[2]
                       mese = elemento_foto[3]
                       anno = elemento_foto[4]
                       risultato=f"{codice}, {titolo}, {autore}, {mese}, {anno}"
                       return risultato
   return None
#^^serve a cercare una foto tramite suo codice, se foto non presente da None
#se è presente restituisce informazioni di foto


def elenco_foto_anno_per_titolo(album, anno):
   titoli=[]
   anno_str=str(anno)
   if anno_str in album.keys():
       for foto in album[anno_str]:
           titoli.append(foto[1])
       return sorted(titoli)
   else: return None
#restituisce elenco foto(in ord alfabetico) scattate in un determinato anno


def main():
   album = {}
   file_path = "album_fotografico.csv"


   while True:
       print("\n--- MENU ALBUM FOTOGRAFICO ---")
       print("1. Carica album da file")
       print("2. Aggiungi una nuova foto")
       print("3. Cerca una foto per codice")
       print("4. Elenco foto di un anno (ordinato per titolo)")
       print("5. Esci")


       scelta = input("Scegli un'opzione >> ").strip()


       if scelta == "1":
           while True:
               file_path = input("Inserisci il path del file da caricare: ").strip()
               album = carica_da_file(file_path)
               if album is not None:
                   break


       elif scelta == "2":
           if not album:
               print("Prima carica l'album da file.")
               continue


           codice = input("Codice della foto: ").strip()
           titolo = input("Titolo: ").strip()
           autore = input("Autore: ").strip()
           try:
               mese = int(input("Mese (1-12): ").strip())
               anno = int(input("Anno: ").strip())
           except ValueError:
               print("Errore: inserire valori numerici validi per mese e anno.")
               continue


           foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
           if foto:
               print(f"Foto aggiunta con successo!")
           else:
               print("Non è stato possibile aggiungere la foto.")
       elif scelta == "3":
           if not album:
               print("L'album è vuoto.")
               continue


           codice = input("Inserisci il codice della foto da cercare: ").strip()
           risultato = cerca_foto(album, codice)
           if risultato:
               print(f"Foto trovata: {risultato}")
           else:
               print("Foto non trovata.")
       elif scelta == "4":
           if not album:
               print("L'album è vuoto.")
               continue


           try:
               anno = int(input("Inserisci l'anno da consultare: ").strip())
           except ValueError:
               print("Errore: inserire un valore numerico valido.")
               continue


           titoli = elenco_foto_anno_per_titolo(album, anno)
           if titoli is not None:
               print(f'\nFoto del {anno}:')
               print("\n".join([f"- {titolo}" for titolo in titoli]))
           else:
               print(f"Nessuna foto trovata per l'anno {anno}.")
       elif scelta == "5":
           print("Uscita dal programma...")
           break
       else:
           print("Opzione non valida. Riprova.")
if __name__ == "__main__":
   main()

