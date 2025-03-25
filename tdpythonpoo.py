def sum_dict(mydict:dict):
    if all(isinstance(v,int) for v in mydict.values()):
        sum_values = sum(mydict.values())
        return sum_values
    else:
        print("Not all values are integers.")

     
class Personne():
    def __init__(self,nom:str,prenom:str):
        self._nom = nom
        self._prenom= prenom
    
    def afficher_info(self):
        print(
            f"""
            information de la personne:
            nom : {self._nom},
            prenom : {self._prenom}
            """
        )
    
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self,value):
        if isinstance(value, str):
            self._nom = value
        else:
            raise ValueError("Le nom doit être une chaîne de caractères")
          
    @property
    def prenom(self):
        return self._prenom
    
    @prenom.setter
    def prenom(self,value):
        if isinstance(value, str):
            self._prenom = value
        else:
            raise ValueError("Le prenom doit être une chaîne de caractères")
    
    
    
class Etudiant(Personne):
    def __init__(self, nom:str, prenom:str, matricule:str, date_naissance:str, notes:dict):
        super().__init__(nom, prenom)
        self._matricule =  matricule
        self._date_naissance = date_naissance
        self._notes = notes
    @property
    def notes(self):
        return self._notes
    
    def ajouter_note(self, matiere: str, note: float):
        if matiere in self._notes:
            print(f"La matière {matiere} existe déjà. La nouvelle note sera ajoutée.")
            # Vous pouvez également mettre à jour la note si nécessaire
            self._notes[matiere] = max(self._notes[matiere], note)  # Garder la meilleure note
        else:
            self._notes[matiere] = note
            print(f"Note ajoutée pour {matiere} : {note}")
    
    def moyenne(self):
        moyenne = sum_dict(self._notes)/len(self._notes)
        return moyenne
    
    def afficher_info(self):
        super().afficher_info()
        print(f"matricule : {self._matricule}")
        print("notes : ")
        for matiere, note in self._notes.items():
            print(f"{matiere} : {note}")
    
    def performence(self):
        if not self._notes:
            print("Aucune note disponible.")
        else:
            print(
                f"""
                    meilleure note : {max(self._notes.values())}
                    pire note : {min(self._notes.values)}
                    moyenne generale : {self.moyenne(self)}
                """
            )

def matiere_note(matiere,etudiant:Etudiant):
    for imatiere,note in etudiant.notes.items():
        if imatiere == matiere:
            return note
        
        


class Professeur(Personne):
    def __init__(self, nom:str, prenom:str, id_professeur:str, matieres:list):
        super().__init__(nom, prenom)
        self._id_professeur = id_professeur
        self._matieres = matieres

    def ajouter_matiere(self, matiere):    
        if isinstance(matiere, str):
            self._matiers.append(matiere)

        else:
            raise ValueError("La matiere doit être une chaîne de caractères")
        
    def afficher_info(self):
        super().afficher_info()
        print(f"id professeur: {self._id_professeur}")
        print("matieres : ")
        for matiere in self._matieres:
            print(matiere)
        
    def performence(self,Etudiant:Etudiant):
        for matiere in self._matieres:
            
        
