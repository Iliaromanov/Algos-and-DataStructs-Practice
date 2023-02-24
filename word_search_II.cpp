class Node{  //*** trie Node
    public:
        string word;
        bool isTerminal;  
        vector<Node*> next;
        Node():next(26,NULL){
            isTerminal = false; 
            
        }
};

class Solution {
    
    void put(string &s,int si, Node* cur){ //** adds a word to the trie 
            int a = s[si]-'a';    //*********** also stores the word at the terminal node
            if(!cur->next[a]){
            Node* newnode = new Node();
            cur->next[a] = newnode;
            }

            if(si != s.size()-1){
            put(s,si+1,cur->next[a]); }
            else
             { cur->next[a]->isTerminal = true;
               cur->next[a]->word = s;
              }
      }

void dfs(vector<vector<char>>& board,int i,int j,Node* t,set<string>& res,vector<vector<bool>>& visit){ 
    if(i<0 || j<0 || i>=board.size() || j>= board[0].size())return; //** dfs call to search for word
    char x = board[i][j]-'a';
    t = t->next[x];
    if(visit[i][j] || !t)return ;
   
    if(t->isTerminal)res.insert((t->word));
    visit[i][j] = true;
    dfs(board,i+1,j,t,res,visit);
    dfs(board,i-1,j,t,res,visit);
    dfs(board,i,j+1,t,res,visit);
    dfs(board,i,j-1,t,res,visit);
    visit[i][j]= false;
}

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        set<string> res;
        Node* t = new Node();
        for(string &s:words){
            put(s,0,t);
        }
       vector<vector<bool>> visit(board.size(),vector<bool>(board[0].size(),false));
        for(int i = 0 ;i<board.size();i++){
            for(int j=0;j<board[0].size();j++){
               dfs(board,i,j,t,res,visit);
            }
        }
        vector<string> ans(res.begin(),res.end());
       return ans;
    }
};