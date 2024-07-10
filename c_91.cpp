#include<iostream>
#include<vector>
using namespace std;
//举例 226-- 2 26 , 22 6,，2，2，6 dp[i]表示解码到第i个元素长度的方法。
// 首先排除开头为0，其次排除如果s[i]是大于6的数字，s[i-1]大于1，那么就只能s[i]单独
//例如 227，237，277
//最后还要排除这种情况，208, s[i-1]=0，那就只能单独s[i],但如果0的前面大于2，那就false
// dp[0] = 1,dp[1] = 1,dp[2]=dp[2]+dp[1]= 0+1 dp[2]= dp[2]+dp[0]
// 排除以上特殊情况后，dp[i] = dp[i-1](单独解码)+dp[i-2]（合并解码），
//但是单独解码需要考虑特殊情况，同时合并解码也有条件，
//单独解码意味着前两位要在10-26之间，
//合并解码意味着前一位不能为零，所以按照这两种方式来解码,由于dp[i]初始为0，所以可以相加
class Solution{
    public:
    int numDecodings(string s){
        int n = s.size();
        vector<int> dp(n+1,0);
        dp[0]=1;
        dp[1] =1;
        for(int i= 2; i<n+1; i++){
            if (10<=stoi(s.substr(i-2, i))<=26){
                dp[i] = dp[i]+dp[i-1];
            }
            if (s.substr(i-2)!="0"){
                dp[i] = dp[i]+dp[i-2];
            }
        }
        for (int i = 0; i < dp.size(); i++)
        {
            cout<<dp[i]<<endl;
        }
        
        return dp[n];
    }
};
int main(){
    Solution sol;
    string s;
    cout<<"input please: ";
    cin>>s;
    printf("your input: ");
    cout<<s<<endl;
    cout<<sol.numDecodings(s)<<endl;
    return 0;
}