#include<iostream>
#include<vector>

using namespace std;

// dp[i][j]表示机器人到达（i,j)坐标的路径数量，给你mxn的框，求dp[m-1][n-1]
// dp[i][j]下一步的行动有两个选择，要么向下（i+1），要么向右（j+1)，这个时候看动态方程
// dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
// dp[i+1][j] = dp[i][j]+ dp[i+1][j-1]
// dp[i][j+1] = dp[i-1][j+1]+dp[i][j]
// 也就是说dp[i+1][j+1],是左边和上边两个dp的和，对于每个点都是如此，
// 直到左边缘和上边缘，不难看出初始条件和动态方程
//dp[0][0] = 1, dp[0][1]=1, dp[0][2]=1...dp[0][n-1]=1
//dp[1][0]=1,dp[2][0] = 1,...dp[m-1][0] = 1


class Solution{
public:
    int pathNum(int m, int n)
    {
        vector<vector<int>> dp(m, vector<int>(n, 0)); 
        dp[0][0] = 1;
        for (int i = 0; i < m; i++)
        {
            dp[i][0] = 1;
        }
        for (int i = 0; i < n; i++)
        {
            dp[0][i] = 1;
        }
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                dp[i][j] = dp[i-1][j]+dp[i][j-1];
            }
            
        }
        return dp[m-1][n-1];
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    int m= 3;
    int n=3;
    cout<< sol.pathNum(m,n)<<endl;
    return 0;
}
