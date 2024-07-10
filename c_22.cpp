#include<iostream>
#include<vector>
#include<string>

using namespace std;
class Solution{
private:
    // 引用传递，因为每次调用都会修改result, 而如果是函数内部，修改某个变量，不需要加上 引用
    void backtrack(string cur, int open_count,int close_count,int n,vector<string>& result ){
        vector<string> res = result;
        if (cur.length()==2*n)
        {
            cout<<"cur: "<<cur<<endl;
            result.push_back(cur);
            return;
        }
        if (open_count<n)
        {
            cout<<cur<<endl;
            backtrack(cur+'(', open_count+1, close_count, n, result);
        }
        if (close_count<open_count)
        {
            backtrack(cur+')', open_count, close_count+1, n, result);
        }
         
    }
public:
    vector<string> generateParentheses(int n){
        vector<string> result;
        backtrack("", 0,0, n, result);
        cout<<result.size()<<endl;
      
        
        for (int i = 0; i < result.size(); i++)
        {
        cout<<result[i]<<"\n"<<endl;
            } 
        return result;
    }
};
int main(int argc, char const *argv[])
{
    Solution sol;
    int n= 3;
    vector<string> res =  sol.generateParentheses(n);
    for (int i = 0; i < res.size(); i++)
    {
        cout<<res[i]<<"\n"<<endl;
    }
    
    return 0;
}
