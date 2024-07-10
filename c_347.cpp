# include <iostream>
# include <vector>
# include <unordered_map>
# include <random>
#include <algorithm>
# include <string>
# include <sstream>
using namespace std;
class Solution{
public:
    vector<int> topKele(vector<int>& nums, int k){
        unordered_map<int, int> map_nums;
        // for (int i = 0; i < nums.size(); i++)
        // {
        //     count[nums[i]]++;
        // }
        for (int num :nums)
        {
            map_nums[num]++;
        }
        vector<int> freqs;
        freqs.reserve(map_nums.size());
        for (auto it=map_nums.begin(); it!=map_nums.end();it++)
        {
            freqs.push_back(it->second);
        }
        //  也可以直接构造
        // vector<int> freqs(map_nums.begin(), map_nums.end());
        int kth_freq = quickSelect(freqs, k);
        vector<int> result;
        for(auto it=map_nums.begin(); it!=map_nums.end();it++){
            if (it->second>=kth_freq)
            {
                result.push_back(it->first);
            }
            
        }
        return result;
    }
private:
    int quickSelect(vector<int>& freqs, int k){
        vector<int> big;
        vector<int> equal;
        vector<int> small;
        default_random_engine generator;
        uniform_int_distribution<int> distribution(0, freqs.size()-1);
        int random_index = distribution(generator);
        int povit = freqs[random_index];
        for (int i=0; i< freqs.size(); i++){
            if (freqs[i]< povit)
            {
                small.push_back(freqs[i]);
            }
            else if  (freqs[i]>povit)
            {
                big.push_back(freqs[i]);
            }
            else equal.push_back(freqs[i]);
        }
        // 如果kth恰好在big里面,那么big的size正好是k
        if (big.size()>=k)
        {
            return quickSelect(big, k);
        }
        // 如果kth恰好在small 里面，那么k-1个在big和equal里面，减去这些就是small的数量
        // 如果big<k,kth有可能在small ,有可能big
        if (small.size()>=freqs.size()-k+1)
        {
            return quickSelect(small, k-big.size()-equal.size());
        }
        return povit;
        
    }
};

int main(){
    vector<int> nums={1,1,1,2,2,2,4};
    int k=2;
    Solution solution;
    vector<int>res = solution.topKele(nums,k);
    ostringstream oss;
    oss << "res: [";
    for(int i=0; i<res.size(); i++) {
    oss << res[i];
  
    
    if(i!=res.size()-1) {
    oss << ", "; 
    }
  }
  oss << "]";

  string result = oss.str();
  cout << result << endl;
}