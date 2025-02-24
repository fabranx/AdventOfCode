# class Region:
#     def __init__(self, ch):
#         self.ch = ch
#         self.positions = []
#
#     def add_pos(self, new_pos):
#         self.positions.append(new_pos)
#
#
# def main():
#     with open('data.txt', 'r') as f:
#         garden = [[ch for ch in row.strip()] for row in f.readlines()]
#         print(garden)
#
#     all_pos = [(row, col) for row in range(len(garden)) for col in range(len(garden[0]))]
#     print(all_pos)
#
#     regions = []
#     visited = []


def trova_gruppi_simboli(matrice):
    n = len(matrice)  # Dimensione della matrice quadrata
    visitato = [[False] * n for _ in range(n)]  # Matrice per tenere traccia dei simboli visitati

    # Direzioni per spostarsi orizzontalmente e verticalmente
    direzioni = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Destra, Giù, Sinistra, Su

    def dfs(x, y, simbolo, gruppo):
        """Esegue DFS per trovare simboli contigui."""
        visitato[x][y] = True
        gruppo.append((x, y))

        for dx, dy in direzioni:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visitato[nx][ny] and matrice[nx][ny] == simbolo:
                dfs(nx, ny, simbolo, gruppo)

    gruppi = []

    # Scansione della matrice
    for i in range(n):
        for j in range(n):
            if not visitato[i][j]:  # Se il simbolo non è stato ancora visitato
                gruppo_corrente = []
                dfs(i, j, matrice[i][j], gruppo_corrente)
                if gruppo_corrente:  # Aggiungiamo il gruppo trovato
                    gruppi.append((matrice[i][j], gruppo_corrente))

    return gruppi


def main():
    with open('data.txt', 'r') as f:
        garden = [row.strip() for row in f.readlines()]

    # Chiamata alla funzione
    gruppi = trova_gruppi_simboli(garden)

    # Stampa dei risultati
    for simbolo, gruppo in gruppi:
        print(f"Simbolo: {simbolo}, Gruppo: {gruppo}")

    total_price = 0
    for simbolo, gruppo in gruppi:
        count_adjacent = 0
        for pos in gruppo:
            row, col = pos
            if (row, col + 1) in gruppo:
                count_adjacent += 1
            if (row + 1, col) in gruppo:
                count_adjacent += 1
        area = len(gruppo)
        perimeter = (4 * len(gruppo)) - (2 * count_adjacent)
        total_price += (len(gruppo) * perimeter)
        print(f"Simbolo: {simbolo} : {area}*{perimeter} = {area * perimeter}")

    print(total_price)


if __name__ == '__main__':
    main()
