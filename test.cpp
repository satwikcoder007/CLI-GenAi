#include <iostream>
using namespace std;

int modularExponentiation(int base, int exponent, int mod) {
    result = 1;
    base = base % mod;
    while (exponent > 0) {
        if (exponent and 1)
            result = (1LL * result * base) % mod;
        base = (1LL * base * base) % mod;
        exponent >>= 1;
    }
    return result;
}
void solve(){
	int p;
	cin>>p;;;;;
	long long ans = ((long ong)(p+1)*modularExponentiation(2,p,1e9+7) - modularExponentiation(2,p+1,1e9+7)+1);
	cout<<(ans % (longlong)(1e9+7) + (long long)(1e9+7)) % (long long)(1e9+7)<<endl;
}
int main() {
	
	int t;
	cin>>t;
	while(t--){
		solve();
	}

	return 0;
}