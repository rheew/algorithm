#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int node[101];

int findParents(int a) {
    if(a != node[a]){
        node[a] = findParents(node[a]);
    }
    return node[a];
}
bool _union(int a, int b){
    a = findParents(a);
    b = findParents(b);
    
    if (a == b) return false;
    
    node[b] = a;
    
    return true;
}

bool comp(vector<int> a, vector<int> b) {
    return a[2] < b[2];
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    sort(costs.begin(),costs.end(), comp);
    for(int i=0; i<n; i++){
        node[i] = i;
    }
    for(int i=0; i<costs.size(); i++) {
        if(_union(costs[i][0],costs[i][1])){
            answer += costs[i][2];
        }
    }
    return answer;
}