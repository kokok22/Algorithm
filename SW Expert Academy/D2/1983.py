## 성적 매기기

T = int(input())
rank = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for t in range(T):
    N, K = list(map(int, input().strip(' ').split(' ')))

    score = []

    for i in range(N):
        mid, final, homework = list(map(int, input().strip(' ').split(' ')))

        score.append(mid*0.35+final*0.45+homework*0.2)

    idx = sorted(score, reverse=True).index(score[K-1])

    idx = idx//(N//10)

    print("#{} {}".format(t+1, rank[idx]))