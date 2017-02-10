import java.util.ArrayList;

public class Add_two_numbers {
	public static class ListNode 
	{
		 int val;
		 ListNode next;
		 ListNode(int x) 
		 { 
			 val = x; 
		 } 
	}
	
	public static ListNode addTwoNumbers(ListNode l1, ListNode l2) 
	{
		ArrayList<Integer> in1 = new ArrayList<Integer>();
		ArrayList<Integer> in2 = new ArrayList<Integer>();
		int temp_1 = l1.val;
		int temp_2 = l2.val;
		while(temp_1 > 0 && temp_1 < 10)
		{
			in1.add(temp_1);
			l1 = l1.next;
		}
		System.out.println(in1);
        return l1;
    }
	
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		ListNode x = new ListNode(5);
		x.next = new ListNode(5);
		x.next.next = new ListNode(5);
		
		ListNode y = new ListNode(8);
		y.next = new ListNode(9);
		y.next.next = new ListNode(3);		

		ListNode re = new ListNode(0);
		re = addTwoNumbers(x,y);
	}

}
