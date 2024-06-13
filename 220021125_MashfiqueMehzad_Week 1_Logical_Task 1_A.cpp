#include <iostream>
#include <vector>

using namespace std;

void _swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

void merge_sort(vector<int>& arr) {
    if (arr.size() <= 1)
        return;

    int length = arr.size();
    int middle = length / 2;

    vector<int> leftarr(middle);
    vector<int> rightarr(length - middle);

    // splitting into subarray
    for (int i = 0; i < middle; i++) leftarr[i] = arr[i];
    for (int i = 0; i < length-middle; i++) rightarr[i] = arr[middle+i];

    // for (auto i : leftarr) cout << i << " "; cout << endl;
    // for (auto i : rightarr) cout << i << " "; cout << endl; 
    // cout << endl;

    merge_sort(leftarr);
    merge_sort(rightarr);

    // sorting and merging part
    int i = 0, l = 0, r = 0;
    while (l < leftarr.size() && r < rightarr.size()) {
        if (leftarr[l] < rightarr[r]) {
            arr[i] = leftarr[l];
            l++;
        } else {
            arr[i] = rightarr[r];
            r++;
        }
        i++;
    }
    while (l < leftarr.size()) {
        arr[i] = leftarr[l];
        l++;
        i++;
    }
    while (r < rightarr.size()) {
        arr[i] = rightarr[r];
        r++;
        i++;
    }
}

int _partitionQS(vector<int>& arr, int low, int high) {
    // in our implementation of quick sort, we select rightmost as pivot
    int& pivot = arr[high];

    int i = low;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            _swap(arr[i], arr[j]);
            i++;
        }
    }

    _swap(arr[i], pivot);
    return i;
}
void quick_sort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = _partitionQS(arr, low, high);
        quick_sort(arr, low, pi - 1);
        quick_sort(arr, pi + 1, high);
    }
}

void _heapify(vector<int>& arr, int length, int i) {
    int largest = i;
    int left = 2*i + 1;
    int right = 2*i + 2;

    if (left < length && arr[left] > arr[largest]) {
        largest = left;
    }
    if (right < length && arr[right] > arr[largest]) {
        largest = right;
    }

    if (largest != i) {
        _swap(arr[i], arr[largest]);
        // recusively heaipfy the sub-trees
        _heapify(arr, length, largest);
    }
}
void heap_sort(vector<int>& arr) {
    int length = arr.size();

    // we are only looping from half the length to 0
    // this is because the rest of the array will get included as the child node
    // of the looped parent node
    for (int i = length / 2; i > -1; i--) {
        // bottom up heapify to procude a "max-heap"
        _heapify(arr, length, i);
    }
    for (int i = length-1; i > 0; i--) {
        // since the array is max-heap, we're basically swapping the max and min element
        _swap(arr[i], arr[0]);
        _heapify(arr, i, 0);
    }
}

int main() {
    vector<int> arr = {5, 7, 4, 9, 3, 1, 6, 3, 8};

    for (auto i : arr) cout << i << " "; cout << endl;
    // merge_sort(arr);
    // quick_sort(arr, 0, arr.size()-1);
    heap_sort(arr);
    for (auto i : arr) cout << i << " "; cout << endl;
}