# emergency_queue.py

class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

    def __lt__(self, other):
        # Lower urgency number = higher priority
        return self.urgency < other.urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.data[index] < self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            self.heapify_up(parent)

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left] < self.data[smallest]:
            smallest = left
        if right < len(self.data) and self.data[right] < self.data[smallest]:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify_down(smallest)

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        return self.data[0] if self.data else None

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        root = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root

    def print_heap(self):
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")


# Example usage:
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))

    heap.print_heap()

    next_up = heap.peek()
    print("\nNext up:", next_up.name, next_up.urgency)

    served = heap.remove_min()
    print("\nServed:", served.name)
    heap.print_heap()
