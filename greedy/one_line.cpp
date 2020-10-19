#include <iostream>
#include <vector>
using namespace std;

int main (void) {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int n;
	cin >> n;
	int people[11];
	vector<int> ans;

	for (int i = 0; i < n; i++) {
		cin >> people[i];
	}
	
	for (int i = n; i > 0; i--) {
		int value = people[i - 1];
		ans.insert(ans.begin() + value, i);
	}

	for (int i = 0; i < n; i++) {
		cout << ans[i] << ' ';
	}
	return 0;
}