class MinStack {
private:
    vector<int> stack, min_stack;

public:
    MinStack() {}

    void push(int val) {
        stack.push_back(val);
        if (min_stack.empty() || min_stack[min_stack.size() - 1] >= val) {
            min_stack.push_back(val);
        }
    }

    void pop() {
        if (stack[stack.size() - 1] == min_stack[min_stack.size() - 1]) min_stack.pop_back();
        stack.pop_back();
    }

    int top() {
        return stack[stack.size() - 1];
    }

    int getMin() {
        return min_stack[min_stack.size() - 1];
    }
};
