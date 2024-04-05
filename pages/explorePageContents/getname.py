from pathlib import Path

folder = Path(r"C:\Users\Harry\OneDrive - The University of Western Australia\2024 Sem1\Agile\project\agile-project\pages\explorePageContents\test")

n=[]

for ig in folder.iterdir():
    n.append(ig.stem)

print(n)
