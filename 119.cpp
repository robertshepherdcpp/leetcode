class Solution {
public:
    vector<int> getRow(int rowIndex) {
        int numRows = rowIndex + 1;
        std::vector<std::vector<int>> rows{};
        for(int i = 1; i < numRows + 1; i++)
        {
            rows.push_back(std::vector<int>(i, 1));
        }
        // now we have go to go through 
        for(int j = 2; j < numRows; j++)
        {
            for(int i = 1; i < rows[j].size() - 1; i++)
            {
                rows[j][i] = rows[j - 1][i - 1] + rows[j - 1][i];
            }
        }
        return rows[rowIndex];
    }
};
