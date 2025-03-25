 
voyelles ={'A':1,'E':5,'I':9,'O':15,'U':21,'Y':25}

def poid_mot(mot:str):
    mot = mot.upper()
    score:int=0
    for i,char in enumerate(mot):
        if char in voyelles:
            score+=(i+1)*voyelles[char]
    return score

print(poid_mot("bonne"))feat: Integrate FailModal into Card component

- Added FailModal component to handle user log data input.
- Implemented state management for modal visibility and log data.
- Updated fail button to open the modal on press.
- Enhanced user experience with keyboard dismissal and auto-focus on input.