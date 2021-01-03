

ARRAY_C = [80.6, 120.8, -115.6, -76.1 , 131.3 , 105.1 , 138.4 , -81.3, -95.3, 89.2, -154.1 ,121.4, -85.1, 96.8 ,68.2]


def get_sign_change(signals:list):
    """
    The function will return the sign changed of the signals
    A positive number = 1, negative = -1 and zero pressure = 0
    """
    results  =  list();
    for v in signals:
        if(v == 0):
          results.append(0);
        elif(v < 0):
            results.append(-1)
        else:
            results.append(1);
    
    return results;



def differential(signals:list):
    """
     The function will differential the signal provided. 
    """
    results  = list();

    for i in range(0, len(signals)):
        results.append(signals[i] - signals[i-1]);
        
    return results;


def count_zero_crossing(signals:list):
    """
      Zero crossing is the point at which a function X(t) changes its sign.
      from negative to positive and positive to negative.
      In a basic waveform there are 2 zero crossing per cycle.
    """
    count  =   0;
    
    if(type(signals) == list):
        # Get the sign values of the signals. This should contain 0,1,-1 to show
        # the signal directions. Now you can count the number of negative or positive
        # with the list you can count the number of
        # times the sign changed to negative.
        sign_values  =  get_sign_change(signals);
        diff_values  =  differential(sign_values)
       
        for v in diff_values:
            if(v != 0):
                count = count + 1
      
    return count;

if __name__ =="__main__":
    print(count_zero_crossing(ARRAY_C))
