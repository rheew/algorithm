#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	vector<int> v;
	v.push_back(10);

	vector<int> ::iterator iter = lower_bound(v.begin(), v.end(), 22);
	
	return 0;
}