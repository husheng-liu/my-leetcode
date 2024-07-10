#include<iostream>
#include<vector>

using namespace std;
//dp[i]表示爬到第i个台阶上的方法，dp[i]应该是
//dp[i-1]或dp[i-2]爬上来的,所以转移方程
//dp[i] = dp[i-1]+dp[i-2]
//举例dp[1] = 1 dp[2] = 1+1或者2+0，dp[3]
class Solution{
    public:
    int pathNum(int n){
        vector<int> dp(n+1,0);
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i < n+1; i++)
        {
            dp[i] = dp[i-1]+dp[i-2];
            cout<<dp[i]<<endl;
        }
        return dp[n];
    }

};
int main(){
    Solution sol;
    
    cout<<sol.pathNum(3)<<endl;
    return 0;
}