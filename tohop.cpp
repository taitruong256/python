/*=====================================================================================
                Nothing is impossible, only you think it is impossible                 
                        Try, try, try again until you succeed     
                           Pratice, practice, and practice
I hated every minute of training, but I said, ‘Don’t quit. Suffer now and live the rest of your life as a champion.' - Mohamed Ali 
                  You may not be the best, but must be the most effort
=====================================================================================*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
bool danhdau[15];
ll n, k;
ll tohop[15];

void intohop()
{
    for (ll i=1; i<=k; i++) cout<<tohop[i]<<" "; cout<<endl;
}


void tohop_k_n(ll i)
{
    for (ll j=tohop[i-1]+1; j<=n-k+i; j++)
    {
        tohop[i]=j;
        if (i==k) intohop(); else tohop_k_n(i+1);
    }
}

void solve()
{
    cin>>n>>k;
    tohop[0]=0;
    tohop_k_n(1);
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    solve();
    return 0;
}