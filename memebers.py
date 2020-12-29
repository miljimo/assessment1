import math;

def cycles(M=1,N=1):
	pis = (math.pi* 2);
	w  =  M * (pis / N);
	k =  (N*w)/ pis
	return k;


def list_members_cycles(N=10):
    results =  list();
    for m in range(1, N):
        c =  cycles(m);
        ic =  int(c);
        if(c%ic == 0):
            if c in results:
                break;

            results.append(ic);
    return results;
