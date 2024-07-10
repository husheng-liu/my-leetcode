#include<iostream>
#include<vector>
using namespace std;
//dp[i][0]第i天不持有股票的利润，dp[i][1]表示第i天持有股票的利润
// 第一种情况下 可能第i-1天也不持有，也可能第i-1天持有股票，现在可以卖出，所以转移方程：
// dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
// 反过来，dp[i][1]=max(dp[i-1][1], dp[i-1][0]-prices[i])
// 当然也可以采用贪心算法，只考虑当前利润，局部最优最终达到全局最优
class Solution{
    public:
    int maxProfit(vector<int> &prices){
        int n = prices.size();
        vector<vector<int>> dp(n);
        
        for (int i = 0; i < n; i++)
        {
            dp[i] ={0,0};
        }
        cout<<"fd"<<endl;
        dp[0][1]=-prices[0];
        for (int i = 1; i < n; i++)
        {
            dp[i][1]=max(dp[i-1][1], dp[i-1][0]-prices[i]);
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]);
        }
        return dp[n-1][0];
        
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> prices= {7,1,5,3,6,4};
    cout<<sol.maxProfit(prices)<<endl;
    return 0;
}
