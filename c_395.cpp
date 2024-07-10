#include<iostream>
#include<vector>
#include<unordered_map>
#include<string>
using namespace std;

class Solution{
    public:
    int longestksubstring(string s, int k){
        cout<< "s: "<< s <<endl;
        unordered_map<char,int> char_count;
        for (int i = 0; i < s.size(); i++)
        {
            char_count[s[i]]++;
        }
        for (auto it = char_count.begin(); it != char_count.end(); it++)
        {
            cout<<it->first<<":"<<it->second<<endl;
        }
        

        for (int i = 0; i < s.size(); i++)
        {
            if (char_count[s[i]]<k)
            {
                cout<<"s.substr(0,i): "<<s.substr(0, i)<<endl;
                int left = longestksubstring(s.substr(0,i), k);
                cout<<"s.substr(i+1): "<<s.substr(i+1)<<endl;
                int right = longestksubstring(s.substr(i+1),k);
                return max(left, right);
            }
        }
        return s.size();    
    }
};

int main(){
    string s = "ababbc";
    int k = 2;
    Solution solution;
    int res = solution.longestksubstring(s,2);
    cout << "res: "<<res<<endl;
}