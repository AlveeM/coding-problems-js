class Solution:
    def canVisitAllRooms(self, rooms):
        visited = set()
        stack = [0]
        
        while stack:
            room_num = stack.pop()
            if room_num not in visited:
                visited.add(room_num)
                keys = rooms[room_num]
                for key in keys:
                    stack.append(key)
                    
        return len(visited) == len(rooms)