#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution{
public:
    int max_sub_sum(vector<int>& nums){
        int maxsum;
        vector<int> dp;
        
        for (int i = 0; i < nums.size(); i++)
        {
            dp.push_back(0);
        }
        dp[0] = nums[0];
        maxsum=dp[0];

        for (int i = 1; i < nums.size(); i++)
        {
            if (dp[i-1]>0)
            {
                dp[i] = dp[i-1]+nums[i];
            }
            else {dp[i]=nums[i];}
            
            {
                maxsum=dp[i];
            }
            
        }
        return maxsum;
        
    }
};



// class Solution{
// public:
//   int max_sub_sum(vector<int>& nums){
//     int maxsum; 
//     vector<int> dp;

//     for (int i = 0; i < nums.size(); i++) {
//       dp.push_back(0);
//     }
//     dp[0] = nums[0];
//     maxsum = dp[0];

//     for (int i = 1; i < nums.size(); i++) {
//       if (dp[i-1]>0) {
//         dp[i] = dp[i-1]+nums[i]; 
//       }else{ 
//         dp[i]=nums[i];
//       }
      
//       if (dp[i]>maxsum) {
//         maxsum = dp[i];  
//       }
//     }
//     return maxsum;
//   }
// };

int main(int argc, char const *argv[])
{
    vector<int> nums= {-2,1,-3,4,-1,2,1,-5,4};
    Solution sol;
    cout<< "fsd: "<<sol.max_sub_sum(nums)<<endl;
    return 0;
}


