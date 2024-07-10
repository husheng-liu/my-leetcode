#include<iostream>
#include<vector>
using namespace std;
class Solution{
public:
    vector<int> productExceptself(vector<int> &nums){
        vector<int> prefix;
        for (int i = 0; i < nums.size(); i++)
        {
           prefix.push_back(1); 
           
        }
        
        for (int i = 1; i < nums.size(); i++)
        {
            prefix[i] = prefix[i-1] * nums[i-1];
        }
        
        vector<int> suffix;
        for (int i = 0; i < nums.size(); i++)
        {
            suffix.push_back(1);
        }  
        
        for (int i = nums.size()-2; i > -1; i--)
        {
           suffix[i] = suffix[i+1] * nums[i+1];
        }
        
        vector<int> result;
        for (int i = 0; i < nums.size(); i++)
        {
            result.push_back(prefix[i] * suffix[i]);
        }
        
        return result;
    }
};

int main(){
    vector<int> nums={1,2,3,4};
    Solution sol;
    vector<int> res = sol.productExceptself(nums);
    cout<<"res:"<<endl;
    for (int i = 0; i < res.size(); i++)
    {
        cout<<res[i]<<",";
        
    }
    cout<<endl; 
    return 0;
}