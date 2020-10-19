#include <iostream>
#include <vector>

using namespace std;

void postOrder(vector<int> node) {
    if(!node.size()) return;
    int root = node[0];
    vector<int> left;
    vector<int> right;

    for(int i=0; i<node.size(); i++) {
        if(node[i] < root) {
            left.push_back(i);
        }
        else if (node[i] > root) {
            right.push_back(i);
        }
    }

    postOrder(left);
    postOrder(right);
    cout << root << endl;

}
int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(0);
    int n = 1;
    vector<int> node;

    while(cin >> n) {
        node.push_back(n);
    }
    postOrder(node);

    return 0;
}
