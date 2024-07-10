#include "D:\program\MinGW\include\c++\11.2.0\iostream"
#include "D:\program\MinGW\include\c++\11.2.0\vector"
using namespace std;
class Solution{
    public:
    bool searchMatrix(vector<vector<int>>& matrix, int target)
    {
        // int rows = sizeof(matrix)/sizeof(matrix[0]);
        int rows = matrix.size();
        int columns = matrix[0].size();
        int row = 0;
        int col = columns-1;
        while(row<rows && col>0)
        {if (matrix[row][col] == target)
        {
            return true;
        }
        else if (matrix[row][col] >target)
        {
            col --;
        }
        else row ++;
        }
        return false;
    }
};

int main() {
  vector<vector<int>> matrix = {
    {1,3,5}, 
    {2,6,9},
    {3,6,9}
  };

  Solution sol;

  if(sol.searchMatrix(matrix, 3)) {
    cout << "Found 3" << endl;
  } else {
    cout << "Not found 3" << endl;
  }
  if (sol.searchMatrix(matrix, 8))
  {
    cout<< "Found 8"<< endl;
  } else {
    cout<<"Not found 8"<<endl;
  }
  
  return 0;
}