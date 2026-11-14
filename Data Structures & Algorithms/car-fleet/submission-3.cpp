// sort the positions - O (n log n)
// calculate (float) time for each position from the last
// store it in a stack<float> fleet only if the top() time is strictly less than the current car's time
// return length of the stack as output

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> pos_speed;
        for (int i = 0; i < speed.size(); ++i) {
            pos_speed.push_back({position[i], speed[i]});
        }
        
        sort(pos_speed.begin(), pos_speed.end(), [](const pair<int, int>& x, const pair<int, int> y) {
            return x.first > y.first;
        });

        vector<float> fleet_time;
        for (const auto& [p, s] : pos_speed) { // time = distance / speed; distance = target - pos;
            float t = (target - p) / (float) s;
            if (fleet_time.empty()) fleet_time.push_back(t);
            else if (fleet_time[fleet_time.size() - 1] < t) fleet_time.push_back(t);
        }

        return fleet_time.size();
    }
};
