from typing import List

# Depth First Search to check for cycles and mark nodes in cycles
def has_cycle(u, adjacency_list, visited, in_current_stack, nodes_in_cycle):
    # Mark the node as visited and in the current stack
    visited[u] = 1
    in_current_stack[u] = 1

    # Explore adjacent nodes
    for v in adjacency_list[u]:
        if not visited[v]:
            # Recursively check if there is a cycle
            if has_cycle(v, adjacency_list, visited, in_current_stack, nodes_in_cycle):
                # Mark the current node as part of the cycle and return True
                nodes_in_cycle[u] = 1
                return 1
        # If an adjacent node is visited and in the current stack, a cycle is present
        elif in_current_stack[v]:
            nodes_in_cycle[u] = 1
            return 1

    # Mark the current node as not in the current stack
    in_current_stack[u] = False
    return False

class Solution:
    def eventualSafeNodes(self, V: int, adjacency_list: List[List[int]]) -> List[int]:
        safe_nodes = []
        visited = [0] * V
        in_current_stack = [0] * V
        nodes_in_cycle = [0] * V

        # Traverse each node and perform a DFS
        for i in range(V):
            if not visited[i]:
                has_cycle(i, adjacency_list, visited, in_current_stack, nodes_in_cycle)
        
        # Add nodes that are not part of any cycle to the safe_nodes list
        return [i for i in range(V) if not nodes_in_cycle[i]]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends