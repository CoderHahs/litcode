def minKnightMoves (n, startRow, startCol, endRow, endCol):
    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    q = []
    q.append([startRow, startCol, 0])
    visited = set()
    visited.add((startRow, startCol))

    # can optimize by using pythagorean distance to find positions closest to target

    while(len(queue) > 0): 
        
        pos = q.pop(0) 
            
        # if current cell is equal to target  
        # cell, return its distance  
        if(pos[0] == endRow and pos[1] == endCol): 
            return pos[2]
                
        # iterate for all reachable states  
        for i in range(8): 
                
            x = pos[0] + dx[i] 
            y = pos[1] + dy[i] 
                
            if(x >= 0 and x <= n and y >= 0 and y <= n and (x,y) not in visited): 
                visited.add((x,y))
                q.append([x,y,pos[2]+1]) 
