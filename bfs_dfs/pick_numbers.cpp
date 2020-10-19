#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int numbers[101];
bool isAns(int init, int node, bool visit[], int *cnt) {
	//cout << node << visit[node] << endl;
	if (init == node and visit[node]) {
		return true;
	}
	if (visit[node]) return false;

	visit[node] = true;
	*cnt += 1;
	return isAns(init, numbers[node], visit, cnt);
}
int main(void) {
	cin.tie(0);
	ios::sync_with_stdio;

	vector<int> ans;
	int total = 0;
	int n;
	cin >> n;
	
	bool visit[101] = { false };

	for (int i = 1; i <= n; i++) {
		cin >> numbers[i];
	}

	for (int i = 1; i <= n; i++) {
		if (visit[i]) continue;
		bool nvisit[101] = {false};
		int cnt = 0;

		for (int j = 1; j <= n; j++) {
			if (!visit[j]) continue;
			nvisit[j] = true;
		}

		if (isAns(i, i, nvisit, &cnt)) {
			for (int j = 1; j <= n; j++) {
				if (visit[j] == nvisit[j]) continue;
				visit[j] = true;
				ans.push_back(j);
			}
			total += cnt;
		}
	}
	sort(ans.begin(), ans.end());
	cout << total << endl;
	for (int i = 0; i < total; i++) {
		cout << ans[i] << endl;
	}
	return 0;
}