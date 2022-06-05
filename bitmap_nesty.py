if __name__ == '__main__':
    # Insert the number of test cases
    n = int(input())
    for k in range(n):
        # Insert rows and cols
        row, col = map(int, input().split())
        
        # Save bitmap
        bitmap = []
        for i in range(row):
            line = input()
            bitmap.append(line)
        
        # Prepare output with the same size of the input
        output = [[False for j in range(col)] for i in range(row)]
        front = []
        total_pixels = row * col
        processed = 0
        
        # Detecting the white pixelss
        for i in range(row):
            for j in range(col):
                if (bitmap[i][j] == '1'):
                    output[i][j] = 0
                    front.append((i,j))
                    processed += 1
        
        while processed < total_pixels:
            new_list = []
            for node in front:
                i, j = node[0], node[1]
                new_distance = output[i][j] + 1
                if (i> 0 and output[i-1][j] is False): # up
                    output[i-1][j] = new_distance                    
                    new_list.append((i-1, j))
                    processed += 1
                if (i< row -1 and output[i+1][j] is False): # down
                    output[i+1][j] = new_distance
                    new_list.append((i+1, j))
                    processed += 1
                if (j > 0 and output[i][j-1] is False): # left
                    output[i][j-1] = new_distance
                    new_list.append((i, j-1))
                    processed += 1
                if (j < col -1 and output[i][j+1] is False): # right
                    output[i][j+1] = new_distance
                    new_list.append((i, j+1))
                    processed += 1
            front = new_list
        
        # Print the output
        for line in output:
            s = map(str, line)
            print(" ".join(s))
        input()
