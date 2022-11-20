#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll  cnt[1010];
ll  arr[1010101];

int main()
{
    int n, m;

    cin >> n >> m;
    for (int i =1; i <= n; i++)
    {
        cin >> arr[i];
        arr[i] += arr[i-1];
        arr[i] %= m;
        cnt[arr[i]]++;
    }

    ll ans = cnt[0];
    for (int i=0; i<m; i++)
    {
        ll  now = cnt[i];
        ans += now * (now - 1) / 2;
    }
    cout << ans;
    return (0);
}

/*
다시 문제로 돌아와서, [i, j] 구간의 합은 sum[j] - sum[i-1] 이고, 
문제에서는 (sum[j] - sum[i-1]) % M 이 0인 순서쌍 (i, j)의 개수를 묻고 있습니다.
(sum[j] - sum[i-1]) % M = 0 이라면 (sum[j]%M) - (sum[i]%M) = 0 입니다.
이 점을 활용해서 sum[i]%M = sum[j]%M 인 쌍의 개수를 구해주면 됩니다.

*/