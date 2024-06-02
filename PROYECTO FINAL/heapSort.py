import heapq

def heapSort(lista):
    heapq.heapify(lista)
    return [heapq.heappop(lista) for _ in range(len(lista))]
