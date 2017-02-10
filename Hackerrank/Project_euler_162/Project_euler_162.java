import java.io.*;
import java.util.*;
import java.math.BigDecimal;

public class Project_euler_162
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
        int input = scan.nextInt();
        if(input < 3)
        	return;
        
        long result = 4;
        int digits = 3;
        for(int n=0;n<input-3;n++)
        {
        	result += 15*16*(n-1) + 41*14*(n-1) - (43*15*(n-1) + 13*n);
        }	
        System.out.println(result);
    }
}