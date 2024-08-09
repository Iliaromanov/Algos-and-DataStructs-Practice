#include <vector>
#include <iostream>

class DisjointSet {
public:
    DisjointSet(int num_elems) : size(std::vector<int>(num_elems, 1)) {
        for (int i = 0; i < num_elems; ++i) 
            parent.push_back(i); // parent[i] = i
    }

    int find(int x) {
        if (parent[x] == x) return x;
        
        // path compression
        parent[x] = find(parent[x]);

        return parent[x];
    }

    bool union_by_size(int x, int y) {
        //returns true if already unioned else false

        int x_rep = find(x);
        int y_rep = find(y);

        if (x_rep == y_rep) return true;

        if (size[x_rep] < size[y_rep]) {
            parent[x_rep] = y_rep;
            size[y_rep] += size[x_rep];
        } else {
            parent[y_rep] = x_rep;
            size[x_rep] += size[y_rep];
        }
        return false;
    }

private:
    std::vector<int> parent;
    std::vector<int> size;
};

int main() {
    int n = 5;
    DisjointSet d{n};

    std::cout << "par 2 = " << d.find(2) << std::endl; 
    std::cout << "union 0,1 = " << d.union_by_size(0, 1) << std::endl;
    std::cout << "par 1 = " << d.find(1) << "| par 0 = " << d.find(0) << std::endl;
    d.union_by_size(2, 3);
    d.union_by_size(4, 3);
    std::cout << "par 4,3,2 = " << d.find(4) << d.find(3) << d.find(2) << std::endl;
    std::cout << "union 1,4 = " << d.union_by_size(1, 4) << std::endl;
    std::cout << "par 1, 4 = " << d.find(1) << d.find(4) << std::endl;
}