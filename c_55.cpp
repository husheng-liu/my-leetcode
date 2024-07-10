#include <iostream>
#include <vector>
using namespace std;
class Solution{
    public:
    bool canJump(vector<int> nums){
        int maxReach =0;
        for(int i=0; i<nums.size(); i++){
            if (i>maxReach)
            {
                return false;
            }
            if(maxReach<nums[i]+maxReach){
                maxReach = nums[i]+maxReach;
            }
            if (maxReach>nums.size()-1){
                return true;
            }
        
        }
        return false;
    }
};

int main()
{
    Solution sol;
    vector<int> nums= {2,3,1,1,4};
    cout<<sol.canJump(nums)<<endl;
    return 0;
}
