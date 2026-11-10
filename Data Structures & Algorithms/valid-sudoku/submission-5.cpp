// an algorithm taking a 2d array sudoku board and giving boolean output whether the given board is valid at the current stage or not
// one loop checking each index, having a formula to get it's row, col and box number
// then checking whether that same number exists in those row, col and/or box, if yes return false (not a valid sudoku), else add in those row, col and box
// return true after the entire loop is done
// formula: board[i][j] -- row = i, col = j
// box -- (row / 3) * 3 + (col / 3)
// data structure for storage: boxes array of arrays

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> boxes(9, vector<int>(10, 0));
        vector<vector<int>> rows(9, vector<int>(10, 0));
        vector<vector<int>> cols(9, vector<int>(10, 0));
        int box {0}, digit {0};

        for (int row = 0; row < 9; ++row) {
            for (int col = 0; col < 9; ++col) {
                box = (row / 3) * 3 + (col / 3); // 0 - 8
                digit = board[row][col] - '0'; // 1 - 9
                
                if (board[row][col] == '.') continue;

                if (rows[row][digit] != 0 || cols[col][digit] != 0 || boxes[box][digit] != 0) return false;

                rows[row][digit] = cols[col][digit] = boxes[box][digit] = 1;
            }
        }

        return true;
    }
};
