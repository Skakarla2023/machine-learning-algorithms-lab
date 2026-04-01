def learn(data, target):
    S = data[0][:]
    G = [['?' for _ in S] for _ in S]

    for i in range(len(data)):
        if target[i] == 'yes':
            for j in range(len(S)):
                if data[i][j] != S[j]:
                    S[j] = '?'
                    G[j][j] = '?'
        else:
            for j in range(len(S)):
                if data[i][j] != S[j]:
                    G[j][j] = S[j]

    G = [g for g in G if g != ['?'] * len(S)]
    return S, G


data = [
    ['sunny','warm','normal','strong','warm','same'],
    ['sunny','warm','high','strong','warm','same'],
    ['rainy','cold','high','strong','warm','change'],
    ['sunny','warm','high','strong','cool','change']
]
target = ['yes','yes','no','yes']

S, G = learn(data, target)
print("S:", S)
print("G:", G)
