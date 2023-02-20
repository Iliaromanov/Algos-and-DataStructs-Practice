#include <iostream>
#include <string>

// macro
#define ALPHABET_SIZE 26 //assume alphabet is 

using namespace std;

class TrieNode {
    public:
        TrieNode() {
            for (int i = 0; i < ALPHABET_SIZE; ++i) {
                children[i] = nullptr;
            }
            isEndOfWord = false;
        }
        ~TrieNode() {}

        TrieNode *children[ALPHABET_SIZE];
        bool isEndOfWord;
};

class Trie {
    public:
        TrieNode *root;

        Trie() { root = new TrieNode(); }
        ~Trie() { destroy_recursive(root); }
        void destroy_recursive(TrieNode *node);
        void insert(string s);
        bool search(string s);
};

void Trie::destroy_recursive(TrieNode *node) {
    for (int i = 0; i < ALPHABET_SIZE; ++i) {
        if (node->children[i] != nullptr) {
            destroy_recursive(node->children[i]);
        }
    }
    delete node;
}

void Trie::insert(string s) {
    TrieNode *cur = root;
    for (int i = 0; i < s.length(); ++i) {
        int idx = s[i] - 'a';
        cout << "idx: " << idx << endl;
        if (not cur->children[idx]) {
            cur->children[idx] = new TrieNode();
        }
        cur = cur->children[idx];
    }
    cur->isEndOfWord = true;
}

bool Trie::search(string s) {
    TrieNode *cur = root;

    for (int i = 0; i < s.length(); ++i) {
        int idx = s[i] - 'a';
        if (not cur->children[idx]) {
            return false;
        }
        cur = cur->children[idx];
    }
    return cur->isEndOfWord;
}



int main() {
    Trie *t = new Trie();
    t->insert("hello");
    t->insert("hi");
    t->insert("hell");
    t->insert("all");

    cout << "search for hello: " << t->search("hello") << endl;
    cout << "search for hi: " << t->search("hi") << endl;
    cout << "search for hell: " << t->search("hell") << endl;
    cout << "search for help: " << t->search("help") << endl;
    cout << "search for all: " << t->search("all") << endl;
    cout << "search for hellos: " << t->search("hellos") << endl;
}