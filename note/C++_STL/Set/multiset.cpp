#include <iostream>
#include <set>
using namespace std;

int main(void) {
	multiset<int> ms;

	ms.insert(9);
	ms.insert(9);
	ms.insert(10);
	ms.insert(8);

	multiset<int> ::iterator iter;
	for (iter = ms.begin(); iter != ms.end(); iter++) {
		cout << *iter << ' ';
	}
	cout << endl;
	cout << ms.count(9) << endl;
	
}
