#include <iostream>
#include <algorithm>
using namespace std;
int dp[1001];
int box[1001];

int main(void) {
    int N;
    
    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%d", &box[i]);
        dp[i] = 1;
    }

    for(int i = 0; i < N; i++) {
        for(int j = i + 1 ; j < N; j++) {
            if(box[i] < box[j]) {
                dp[j] = max(dp[j], dp[i] + 1);
            }
        }
    }
    int ans = 0;
    for(int i = 0; i < N; i++) {
        ans = max(ans, dp[i]);
    }
    
    printf("%d\n", ans);
    return 0;
}
