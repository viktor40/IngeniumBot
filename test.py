for i in range(10):
    with open('console.out', 'w') as f:
        tekst = f'test{i}'
        f.write(tekst)
