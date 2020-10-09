#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    long long start = 1;
    long long end = 1000000000 * (long long)n;
    
    while (start <= end) {
        long long mid = (start + end) / 2;
        long long cnt = 0;
        for(int i=0; i<times.size(); i++) {
            long long time = (long long)times[i];
            cnt += mid / times[i];
        }
        if(cnt >= n) {
            end = mid - 1;
        }
        else {
            start = mid + 1;
        }
    }
    answer = end + 1;
    return answer;
}