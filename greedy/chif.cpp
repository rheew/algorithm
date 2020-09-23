#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;
bool comp(pair<int, int> a, pair<int, int> b) {
	if (a.second == b.second) {
		return a.first < b.first;
	}
	else return a.second > b.second;
}

int main(void) {
	multiset<int> bag;
	vector<pair<int, int>> items;
	multiset<int> ::iterator iter;
	vector<pair<int, int>> ::iterator viter;
	int N, M;
	
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		int weight, value;
		scanf("%d %d", &weight, &value);
		items.push_back(make_pair(weight, value));
	}

	for (int i = 0; i < M; i++) {
		int value;
		scanf("%d", &value);
		bag.insert(value);
	}
	sort(items.begin(), items.end(), comp);
	long long ans = 0;

	for (int i = 0; i < N; i++) {
		iter = bag.lower_bound(items[i].first);

		if (iter == bag.end())
			continue;

		bag.erase(iter);
		ans += items[i].second;
	}

	printf("%lld", ans);
}
