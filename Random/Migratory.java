import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Migratory {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        TreeMap<Integer,Integer> t = new TreeMap();
        ArrayList<Integer> arrlist = new ArrayList<Integer>();
        int[] types = new int[n];
        for(int types_i=0; types_i < n; types_i++){
            types[types_i] = in.nextInt();
            arrlist.add(types[types_i]);
            t.put(types[types_i],Collections.frequency(arrlist,types[types_i]));
        }
        // your code goes here
        
        ArrayList<Integer> ids = new ArrayList<Integer>();
        ArrayList<Integer> freqs = new ArrayList<Integer>();
        for(Map.Entry<Integer,Integer> entry : t.entrySet()){
            ids.add(entry.getKey());
            freqs.add(entry.getValue());
        }
        
        int index = freqs.indexOf(Collections.max(freqs));
        System.out.print(ids.get(index));
    }
}



