#include<string>
#include<vector>
#include<iostream>
using namespace std;

class Solution{
public:
    string longestPalindrome(string s){
        int n= s.size();
        int max_len = 0;
        int start=0;
        vector<vector<int>> dp;
        vector<int>tmp;
        for (int i = 0; i < n; i++)
        {
           for (int i = 0; i < n; i++)
           {
                tmp.push_back(0); 
           }
           dp.push_back(tmp); 
        }
        for (int i = 0; i < n; i++)
        {
            dp[i][i]=1;
        }
        for (int i = 0; i < n; i++)
        {
           for (int j = 0; j < n; j++)
           {
            cout<<dp[i][j];
           }
           cout<<endl;
            
        }
                 
        // length 应该为[2，n]
        for (int length = 2; length<n+1; length++)
        {
            // i j 是片段两头指针，i从0开始，
            // 到i+length应该是s的末尾n,但是for不含有断点，所以加1
            for (int i = 0; i <n-length+1 ; i++)
            {
                int j = i+length-1;
                cout<<i<<","<<j<<endl;
                if (s[i]==s[j])
                {
                  if (length<=3 or dp[i+1][j-1]==1)
                    {
                        dp[i][j] = 1;
                        if (max_len<length){
                            max_len=length;
                            start = i; 
                        }
                    }
                }
                
            }   
        }
        return s.substr(start, start+max_len);
    }
};

int main(){
    string s="babad";
    Solution sol;
    string result = sol.longestPalindrome(s);
    cout<<result<<endl;
}