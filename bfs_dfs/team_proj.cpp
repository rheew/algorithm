#include <iostream>
#include <queue>
using namespace std;

int student[100001];
int degree[100001];
bool visit[100001];

int BFS(int start) {
    visit[start] = true;
    queue<int> q;
    q.push(start);
    int cnt = 0;

    while(!q.empty()) {
        int now = q.front();
        visit[now] = true;
        q.pop();

        int parents = student[now];
        cnt++;
        
        degree[parents]--;

        if(degree[parents] == 0) {
            q.push(parents);
        }

    }

    return cnt;
}

int main(void) {
    
    int T;
    scanf("%d", &T);

    for(int t = 0; t < T; t++) {
        int N;
        scanf("%d", &N);

        for(int i = 1; i <= N; i++) {
            degree[i] = 0;
            visit[i] = false;
        }

        for(int i = 1; i <= N; i++) {
            scanf("%d", &student[i]);
            degree[student[i]]++; 
        }

        int ans = 0;
        for(int i = 1; i <= N; i++) {
            if(visit[i]) continue;

            if(degree[i] == 0) {
                ans += BFS(i);
            }
        }
        printf("%d\n", ans);
    }

    return 0;
}
