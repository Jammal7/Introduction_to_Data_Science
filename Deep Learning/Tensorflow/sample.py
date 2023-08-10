# A video player allows users to choose videos to play but it has some rules. The videos must be chosen in pairs and 
# each pair must have a duration which is a multiple of 60 seconds (e.g. 40 + 20, 90 + 30). Given the number of videos 
# and the list of video durations, calculate the total number of different video pairs that can be chosen. 
# Each video can only appear once in each pair, but can appear in multiple pairs. The order of videos in each pair is 
# not important.

# Complete the 'playlist' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY songs as parameter.
#

def playlist(songs):
    N = len(songs)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (songs[i] + songs[j]) % 60 == 0:
                count += 1
    return count


        


    
    
    
    