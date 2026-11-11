// here if we keep track of the min element while inserting it, but not just one min element, all min elements
// for that we need a data structure, what would that be?
// a monotonic stack alongwith the minstack to keep track of the min element, ez
// 

class MinStack {
    vector<int> normal_stack, min_stack;
public:
    MinStack() {}
    
    void push(int val) {
        if (normal_stack.empty()) {
            min_stack.push_back(val);
        } else if (val <= min_stack[min_stack.size() - 1]) min_stack.push_back(val);
        
        normal_stack.push_back(val);
    }
    
    void pop() {
        if (normal_stack[normal_stack.size() - 1] == min_stack[min_stack.size() - 1]) {
            normal_stack.pop_back();
            min_stack.pop_back();
        } else normal_stack.pop_back();
    }
    
    int top() {
        return normal_stack[normal_stack.size() - 1];
    }
    
    int getMin() {
        return min_stack[min_stack.size() - 1];
    }
};
