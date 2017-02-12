ArrayList<Integer> arrlist = new ArrayList<Integer>();


ArrayList<Integer> freq = new ArrayList<Integer>();
        for(int i=0;i<arrlist.size()-1;i++){
            int t = arrlist.get(i);
            freq.add(Collections.frequency(arrlist,t));
        }
        System.out.print(freq);
        
        int largest_index = 0;
        int second_largest_index = 0;
        
        for(int i = 0; i < freq.size(){
            if(freq.get(i) > freq.get(largest_index)){
                largest_index = i;
            }
        }
    }