#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	char str[51];
	char calculator[50];
	int num[30], temp = 0, sum = 0, total = 0;
	scanf("%s", &str);
	fill_n(num, 30, 0);
	for (int i = 0; *(str+i); i++) {
		if (str[i] == '-' || str[i] == '+') {
			calculator[temp] = str[i];
			temp++;
			continue;
		}
		num[temp] = num[temp] * 10 + str[i] - 48;
	}
	sum = num[temp];
	for (int i = temp-1; i >= 0; i--) {
		if (calculator[i] == '-') {
			total = total-sum;
			sum = num[i];
		}
		else if (calculator[i] == '+') sum += num[i];
	}
	total += sum;
	printf("%d\n", total);
	return 0;
}