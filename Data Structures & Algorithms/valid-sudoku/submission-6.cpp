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
        int rows[9] = {}, cols[9] = {}, boxes[9] = {};
        int box {0}, digit {0}, bit {0};

        for (int row = 0; row < 9; ++row) {
            for (int col = 0; col < 9; ++col) {
                if (board[row][col] == '.') continue;

                box = (row / 3) * 3 + (col / 3);
                digit = board[row][col] - '0';
                bit = 1 << digit;

                if (rows[row] & bit || cols[col] & bit || boxes[box] & bit) return false;

                rows[row] |= bit;
                cols[col] |= bit;
                boxes[box] |= bit;
            }
        }

        return true;
    }
};
