#include <iostream>
#include <vector>
#include <unordered_map>
#include <map>
#include <queue>
#include <string>

using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    map<string, int> sentences;
};

class AutoCompleteSystem {
private:
    TrieNode* root;
    string currentInput;
    TrieNode* currentNode;

    void insert(string sentence, int frequency) {
        TrieNode* node = root;
        for (char c : sentence) {
            if (!node->children[c]) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->sentences[sentence] += frequency;
        }
    }

    vector<string> search(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (!node->children[c]) {
                return {};
            }
            node = node->children[c];
        }

        priority_queue<pair<int, string>> pq;
        for (auto& [sentence, freq] : node->sentences) {
            pq.push({freq, sentence});
            if (pq.size() > 3) {
                pq.pop();
            }
        }

        vector<string> result;
        while (!pq.empty()) {
            result.push_back(pq.top().second);
            pq.pop();
        }
        reverse(result.begin(), result.end());
        return result;
    }

public:
    AutoCompleteSystem(vector<string>& sentences, vector<int>& times) {
        root = new TrieNode();
        currentNode = root;
        for (int i = 0; i < sentences.size(); ++i) {
            insert(sentences[i], times[i]);
        }
    }

    vector<string> input(char c) {
        if (c == '#') {
            insert(currentInput, 1);
            currentInput = "";
            currentNode = root;
            return {};
        }

        currentInput += c;
        return search(currentInput);
    }
};

int main() {
    vector<string> sentences = {"i love you", "island", "ironman", "i love geeksforgeeks"};
    vector<int> times = {5, 3, 2, 2};
    AutoCompleteSystem acs(sentences, times);

    vector<string> result = acs.input('i');
    for (const string& s : result) {
        cout << s << endl;
    }

    result = acs.input(' ');
    for (const string& s : result) {
        cout << s << endl;
    }

    result = acs.input('a');
    for (const string& s : result) {
        cout << s << endl;
    }

    result = acs.input('#');
    for (const string& s : result) {
        cout << s << endl;
    }

    return 0;
}
