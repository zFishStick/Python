# Funzione per leggere i contenuti di un file e restituire un set di nomi
def read_file_to_set(filename):
    with open(filename, 'r') as file:
        return set(line.strip() for line in file)

# Leggi i nomi dai file
seguitedi_set = read_file_to_set('followees.txt')
followers_set = read_file_to_set('followers.txt')

# Trova la differenza (followers ma non seguiti)
difference_set = seguitedi_set - followers_set

# Scrivi il risultato in un file di testo
with open('followees_not_followers.txt', 'w') as file:
    for person in sorted(difference_set):
        file.write(person + '\n')

print("File 'followees_not_followers.txt' creato con successo.")
