class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        
        for(auto originalWord: strs){
            string sortedWord = originalWord;
            sort(sortedWord.begin(), sortedWord.end());
            mp[sortedWord].push_back(originalWord);
        }
        
        vector<vector<string>> ans;
        for(auto pair: mp){
            ans.push_back(pair.second);
        }
        for (const auto& group : ans) {
            for (const auto& str : group) {
                cout << str << " ";
            }
            cout << endl;
        }
        return ans;
    };
};
    
