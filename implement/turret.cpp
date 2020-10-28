#include <iostream>
#include <math.h>
using namespace std;
const double pi = acos(-1);
int main(void) {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int x1, x2, y1, y2, r1, r2;
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		if (x1 == x2&&y1 == y2) {
			cout << (r1 == r2 ? -1 : 0) << endl;
		}
		else {
			double i = sqrt(pow(x1 - x2,2) + pow(y1 - y2,2));
			//cout << i << endl;
			if (i > r1 + r2 || i < abs(r1-r2)) cout << 0 << endl;
			else if (abs(r1 - r2) == i || abs(r1 + r2) == i) cout << 1 << endl;
			else cout << 2 <<endl;
		}
	}
	return 0;
}