
def minimax(depth,nodeindex,ismax,scores,height):
  #base case:leaf node reached
  if depth==height:
      return scores[nodeindex]

  if ismax:
       return max(
          minimax(depth+1,nodeindex*2,False,scores,height),
          minimax(depth+1,nodeindex*2 +1,False,scores,height)
      )
  else:
    return min(
        minimax(depth+1,nodeindex*2,True,scores,height),
        minimax(depth+1,nodeindex*2 +1,True,scores,height)
    )
height=3
scores=list(map(int,input("enter 8 leaf node values:").replace(",", " ").split()))
if len(scores) != 2**height:
    raise ValueError(f"Expected {2**height} leaf node values, but received {len(scores)}.")

result=minimax(0,0,True,scores,height)
print("\n the optimal value is:",result)