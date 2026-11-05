class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows, cols, boxes;
        rows.resize(9); cols.resize(9); boxes.resize(9);

        for (int row = 0; row < board.size(); ++row) {
            for (int col = 0; col < board[0].size(); ++col) {
                if (board[row][col] != '.') {
                    if (rows[row].count(board[row][col])) return false;
                    if (cols[col].count(board[row][col])) return false;
                    if (boxes[((row / 3) * 3 + (col / 3))].count(board[row][col])) return false;
                    rows[row].insert(board[row][col]);
                    cols[col].insert(board[row][col]);
                    boxes[((row / 3) * 3 + (col / 3))].insert(board[row][col]);
                }
            }
        }

        return true;
    }
};
