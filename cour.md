

### Classes en Python

En Python, toutes les classes héritent de manière implicite de la classe `object`. Cette classe est la racine de l'arbre d'héritage et contient des fonctions magiques appelées méthodes spéciales ou méta-méthodes.

### Héritage Simple et Multiple

#### Héritage Simple
Lorsqu'une classe (fille) hérite d'une autre classe (mère), elle obtient tous ses attributs et méthodes. L'héritage simple est le type de relation où une classe ne peut avoir qu'un seul parent.

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def description(self):
        return f"Nom: {self.nom}, Age: {self.age}"

class Enseignant(Personne):
    def __init__(self, nom, age, matiere):
        super().__init__(nom, age)  # Appel du constructeur de la classe mère
        self.matiere = matiere

    def description_complete(self):
        return f"Nom: {self.nom}, Age: {self.age}, Matière: {self.matiere}"
```

#### Héritage Multiple
Lorsqu'une classe hérite de plusieurs classes, on parle d'héritage multiple. Python utilise un algorithme de résolution de méthodes (Method Resolution Order - MRO) pour éviter les conflits et trouver la bonne méthode à appeler.

```python
class A:
    def methode(self):
        return "A"

class B:
    def methode(self):
        return "B"

class C(A, B):
    pass

c = C()
print(c.methode())  # Output: A (car A est avant B dans l'ordre de déclaration)
```

### Méthodes Spéciales (Méta-méthodes)
Les méta-méthodes sont des méthodes spéciales en Python qui commencent et se terminent par deux sous-tirets bas (`__`). Elles sont utilisées pour surcharger certains comportements intégrés.

```python
class MaClasse:
    def __init__(self, valeur):
        self.valeur = valeur

    def __str__(self):  # Méthode spéciale pour la conversion en chaîne de caractères
        return f"Valeur: {self.valeur}"
```

### Fonction `sorted`
La fonction `sorted` est une fonction intégrée en Python qui trie les éléments d'une séquence (comme une liste) et retourne une nouvelle liste triée. Elle utilise le tri par insertion si l'argument n'est pas une chaîne de caractères, mais par ordre ASCII si c'en est une.

```python
ma_liste = [3, 1, 4, 1, 5, 9]
sorted(ma_liste)  # Tri par défaut des nombres
print(sorted(ma_liste))  # Output: [1, 1, 3, 4, 5, 9]

chaine = "banana"
sorted(chaine)  # Tri par ordre ASCII de chaque caractère
print(sorted(chaine))  # Output: ['a', 'a', 'a', 'b', 'n', 'n']
```

### Conclusion
En résumé, les classes en Python peuvent avoir des relations d'héritage avec la classe `object` et permettent l'héritage multiple grâce à un algorithme de résolution de méthodes. Les méta-méthodes sont utiles pour surcharger certains comportements intégrés, et la fonction `sorted` trie les éléments en fonction de leur type.


 ### Encapsulation et Accesseurs

L'encapsulation est un concept fondamental en programmation orientée objet qui vise à masquer les détails d'implémentation des objets. En Python, cela se fait généralement en utilisant des conventions pour indiquer quels attributs et méthodes sont privés ou protégés.

#### Attributs Privés
Les attributs privés ne doivent pas être modifiés directement à partir de l'extérieur de la classe. Pour cela, on utilise généralement un underscore (`_`) au début du nom de l'attribut pour le marquer comme privé.

```python
class MaClasse:
    def __init__(self, valeur):
        self._valeur = valeur  # Attribut privé

    def get_valeur(self):
        return self._valeur

    def set_valeur(self, nouvelle_valeur):
        if nouvelle_valeur > 0:
            self._valeur = nouvelle_valeur
        else:
            print("La valeur doit être positive.")
```

Dans cet exemple, `_valeur` est un attribut privé. Les méthodes `get_valeur` et `set_valeur` permettent d'accéder et de modifier la valeur de l'attribut `_valeur`.

#### Accesseurs et Mutateurs
Les méthodes `get_valeur` et `set_valeur` sont des exemples d'accesseurs (getters) et de mutateurs (setters). Elles permettent d'accéder et de modifier l'attribut privé `_valeur` tout en validant ou modifiant la valeur avant de le faire.

#### Propriétés
En Python, les propriétés peuvent être utilisées pour encapsuler des accesseurs et mutateurs de manière plus élégante :

```python
class MaClasse:
    def __init__(self, valeur):
        self._valeur = valeur  # Attribut privé

    @property
    def valeur(self):
        return self._valeur

    @valeur.setter
    def valeur(self, nouvelle_valeur):
        if nouvelle_valeur > 0:
            self._valeur = nouvelle_valeur
        else:
            print("La valeur doit être positive.")
```

 
Avec cette implémentation, vous pouvez accéder à `valeur` comme si c'était un attribut public, mais en réalité, vous appelez la méthode `get_valeur` ou `set_valeur`.

#### Encapsulation et Protection des Données
L'encapsulation est également utile pour protéger les données d'une classe. En encapsulant les attributs, vous pouvez empêcher l'accès direct aux données internes de la classe, ce qui peut aider à prévenir les erreurs et les modifications non intentionnelles.

### Exemple Complet
Voici un exemple complet d'une classe avec encapsulation :

```python
class Personne:
    def __init__(self, nom, age):
        self._nom = nom  # Attribut privé
        self._age = age  # Attribut privé

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nouveau_nom):
        if isinstance(nouveau_nom, str) and len(nouveau_nom) > 0:
            self._nom = nouveau_nom
        else:
            print("Le nom doit être une chaîne de caractères non vide.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, nouvel_age):
        if isinstance(nouvel_age, int) and nouvel_age > 0:
            self._age = nouvel_age
        else:
            print("L'âge doit être un entier positif.")
```

Dans cet exemple, les attributs `_nom` et `_age` sont encapsulés avec des accesseurs et mutateurs respectifs. Cela permet de contrôler l'accès aux données internes de la classe et d'appliquer des règles de validation si nécessaire.

### Conclsusion
L'encapsulation est une pratique essentielle en programmation orientée objet qui aide à protéger les données et le comportement des objets. En utilisant des conventions comme l'underscore pour indiquer que certains attributs sont privés, ou des propriétés pour encapsuler des accesseurs et mutateurs, vous pouvez créer des classes plus robustes et maintenables.

 
 Les `namedtuple` de Python sont un type de données immuable (non modifiable) qui fournit une manière efficace d'organiser les informations sous forme de petites structures de données. Elles sont très utiles pour créer des objets légers et immuables avec un nommage explicite pour leurs champs, ce qui peut améliorer la lisibilité du code. Voici quelques exemples d'utilisation des `namedtuple` :

### 1. Définition et Initialisation

```python
from collections import namedtuple

# Définition de la namedtuple
Person = namedtuple('Person', ['nom', 'age', 'ville'])

# Création d'une instance de Person
personne = Person(nom='Alice', age=30, ville='Paris')

print(personne)  # Output: Person(nom='Alice', age=30, ville='Paris')
```

### 2. Accès aux Champs

Les `namedtuple` permettent d'accéder aux champs par leur nom, ce qui rend le code plus lisible :

```python
print(personne.nom)     # Output: Alice
print(personne.age)     # Output: 30
print(personne.ville)   # Output: Paris
```

### 3. Utilisation dans une Fonction

Les `namedtuple` peuvent être utilisées comme arguments de fonctions :

```python
def afficher_personne(person):
    print(f"Nom: {person.nom}, Age: {person.age}, Ville: {person.ville}")

afficher_personne(personne)  # Output: Nom: Alice, Age: 30, Ville: Paris
```

### 4. Conversion en Dictionnaire

Les `namedtuple` peuvent être converties en dictionnaires :

```python
dictionnaire = personne._asdict()
print(dictionnaire)  # Output: {'nom': 'Alice', 'age': 30, 'ville': 'Paris'}
```

### 5. Comparaison avec un Tuple Classique

Les `namedtuple` peuvent être utilisées comme des tuples classiques, mais offrent une meilleure lisibilité et une protection contre les modifications accidentelles :

```python
personne_tuple = ('Alice', 30, 'Paris')
print(personne_tuple)  # Output: ('Alice', 30, 'Paris')

# Les tuples classiques peuvent être modifiés sans erreur
# personne_tuple[0] = 'Bob'  # Cela causera une erreur

# Les namedtuples empêchent les modifications accidentelles
# personne.nom = 'Bob'  




