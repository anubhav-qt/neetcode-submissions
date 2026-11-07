// a simple algorithm to encode with delimiter(s) to encode an array of strings into a single string
// then another simple algorithm to decode that encoded string into the same array of strings
// the main thought is to create such a delimiter combination that can be used as the delimiter but the problem is also that any combination of delimiters can be also a string or a substring of a string inside the array which we are combining so how will the machine decide what is a delimiter and what is not a delimiter
// let's say we have a combination of "##*#" as the delimiter, a string having "hello##*# world" will become: hello##*###*###*###*#world##*# which will be decoded into "hello ##*# world " and that is not what we wanted
// how can we make the machine realize this is the start and this is the end, and don't read anything inside?
// we do: N1##*#<string>N2##*#<string>... like this

// algorithm:
// encode:
// initialize string output and delimiter
// for each str in strs: start with appending the counting the length of that str, then append the delimiter, then append the string in output
// return output

// decode:
// intitialize vector<string> output
// initilialize the delimiter as string
// while index less than string.size(): read the digits before the delimiter, append the length that is the integer we just read of the string after that delimiter, jump to that index
// return output

class Solution {
public:
    string encode(vector<string>& strs) {
        string output;
        string delimiter = "#";

        for (const auto& str : strs) {
            int length = str.size();
            output += to_string(length) + delimiter + str;
        }

        return output;
    }

    vector<string> decode(string s) {
        vector<string> output;
        string delimiter = "#";

        int i = 0;
        while (i < s.size()) {
            string temp;
            while (s[i] != '#') {
                temp += s[i++];
            }
            int str_length = stoi(temp);

            // now the index i is at the delimiter
            temp.clear();
            temp += s.substr(++i, str_length);
            i += str_length;

            // now temp has the actual string
            output.push_back(temp);
        }

        return output;
    }
};
