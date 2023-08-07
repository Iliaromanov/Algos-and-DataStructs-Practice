#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

class MaxHeap {
    public:
        void insert(int val);
        int getMax();
        int popMax();

    private:
        vector<int> heap;
        int parentI(int i); // return idx of parent of node i
        int leftI(int i); // return idx of left child of node i
        int rightI(int i); // return idx of right cihld of node i
};

int MaxHeap::parentI(int i) {
    return floor((i - 1) / 2);
}

int MaxHeap::leftI(int i) {
    return 2*i + 1;
}

int MaxHeap::rightI(int i) {
    return 2*i + 2;
}

void MaxHeap::insert(int val) {
    heap.push_back(val);

    // bubble up the new leaf until its in correct position
    int i = heap.size() - 1;
    while (i != 0 and heap[parentI(i)] < heap[i]) { // while i isn't root
        swap(heap[i], heap[parentI(i)]);
        i = parentI(i);
    }
}

int MaxHeap::getMax() {
    assert(heap.size() > 0);  // can't get max of emtpy heap
    return heap[0];
}

int MaxHeap::popMax() {
    assert(heap.size() > 0);  // can't get max of emtpy heap
    int max = getMax();
    swap(heap[0], heap[heap.size()-1]);
    heap.pop_back();

    // bubble down the leaf we put at root
    int i = 0;
    while (leftI(i) < heap.size()) { // while i isn't leaf
        int maxChildI = leftI(i);
        if (rightI(i) < heap.size() and heap[rightI(i)] > heap[leftI(i)]) {
            maxChildI = rightI(i);
        }
        if (heap[i] >= heap[maxChildI]) break; // i is in valid position
        swap(heap[i], heap[maxChildI]);
        i = maxChildI;
    }

    return max;
}


int main() {
    MaxHeap mh = MaxHeap();
    mh.insert(5);
    
    assert(mh.getMax() == 5);

    mh.insert(4);
    mh.insert(3);
    mh.insert(2);
    assert(mh.getMax() == 5);
    mh.insert(6);

    assert(mh.popMax() == 6);
    assert(mh.popMax() == 5);
    assert(mh.getMax() == 4);
    mh.insert(10);
    mh.insert(-1);
    mh.insert(5);
    assert(mh.popMax() == 10);
    assert(mh.getMax() == 5);

    cout << "All Tests Passed!" << endl;
}