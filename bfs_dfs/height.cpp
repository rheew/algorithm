#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int BFS(vector<vector<int>> node, int start) {
    int cnt = 0;
    queue<int> q;
    q.push(start);
    bool visit[501] = { false };

    while(!q.empty()) {
        int now = q.front();
        q.pop();

        for(int i=0; i<node[now].size(); i++) {
            int child = node[now][i];
            
            if (visit[child]) continue;
            visit[child] = true;
            q.push(child);
            cnt++;
        }
    }
    return cnt;
}
int main(void) {
    vector<vector<int>> down;
    vector<vector<int>> up;
    int N, M;

    scanf("%d %d", &N, &M);

    for(int i=0; i<=N; i++){
        vector<int> a;
        down.push_back(a);
        up.push_back(a);
    }

    for(int i=0; i<M; i++){
        int a, b;
        scanf("%d %d", &a, &b);
        down[b].push_back(a);
        up[a].push_back(b);
    }
    int ans = 0;

    for(int i=1; i<=N; i++) {
        int temp = 0;
        temp += BFS(up, i);
        temp += BFS(down, i);
        if (temp == N - 1) ans++;
    }

    printf("%d\n",ans);
    return 0;
}
