# Do brancha można ustawić "upstream" i wtedy pushować do niego

# można dodać do git ignore *.exec by ignorować konkretne pliki

# Strategie mergowania:
## fast forward:
- tylko jak docelowy branch to przodek obecnego
- merge by default to zrobi
## rebase
- najpierw poprawiamy obecnego brancha, a dopiero później merge
- będąc na Branchu A zrebersuj się na B: git spróbuje poprawić przodka B by nie doszło do merge konflictu
## rebase - squash
- jeśli obydwa branche zmieniają te same linijki kodu, to rebase nas zatrzyma przy KAŻDYM commicie
- by nie musieć zatrzymywać się na dużej ilości plików robimy squash: bierzemy wszystkie zmiany z ciągu commitów i prosimy gita o "złożenie" tych commitów
- wada: tracimy historię tych zmian, message commitów są "złączane"
## merge commit
  
