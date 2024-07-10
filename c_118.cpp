#include<iostream>
#include<vector>
using namespace std;
//dp[1] => [[1]] dp[2] => [[1],[1]],dp[3] => [[1],[2],[1]], dp[4]=>[1,3,3,1]
// dp[i] = dp[i-1]+tmp
// 输入: numRows = 5
// 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
class Solution{
    public:
    vector<vector<int>> generate(int n){
        vector<vector<int>>dp(n);
        for (int i = 0; i < n; i++)
        {
            vector<int> row((i+1),1);
            for (int j = 1; j < i; j++)
            {
                row[j] = dp[i-1][j-1]+dp[i-1][j];
;            }
            
            dp[i] = row;
            
        }
 
        return dp;
    }
};


int main(int argc, char const *argv[])
{
    Solution sol;
    vector<vector<int>> result = sol.generate(3);
    for (int i = 0; i < result.size(); i++)
    {
        for (int j = 0; j < result[i].size(); j++)
        {
            cout<<result[i][j]<<endl;
        }
         
    }
    
    return 0;
}

        
