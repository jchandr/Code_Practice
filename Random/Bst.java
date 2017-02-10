public class Bst{
	static Node root;

	public static void addnewNode(int k){
		Node newnode = new Node(k);

		if(root == null)
			root = newnode;
		else{
			Node currentnode = root;
			Node parent;

			while(true){
				parent = currentnode;
				if(k <= currentnode.key){
					currentnode = currentnode.leftchild;

					if(currentnode == null){
						parent.leftchild = newnode;
						return;
					}
				}
				else{
					currentnode = currentnode.rightchild;

					if(currentnode == null){
						parent.rightchild = newnode;
						return;
					}
				}
			}
		}

	}

	public static void inOrder(Node focusnode){
			if(focusnode != null){
			inOrder(focusnode.leftchild);
			System.out.println(focusnode.key);
			inOrder(focusnode.rightchild);
		}
	}

	public static void preOrder(Node focusnode){
			if(focusnode != null){
			System.out.println(focusnode.key);
			inOrder(focusnode.leftchild);
			inOrder(focusnode.rightchild);
		}
	}

	public static void postOrder(Node focusnode){
			if(focusnode != null){
			inOrder(focusnode.leftchild);
			inOrder(focusnode.rightchild);
			System.out.println(focusnode.key);
		}
	}


	public static void main(String[] args) {
			Bst tree = new Bst();
			tree.addnewNode(50);
			tree.addnewNode(25);
			tree.addnewNode(15);
			tree.addnewNode(30);
			tree.addnewNode(75);
			tree.addnewNode(85);

			System.out.println("In inOrder");
			tree.inOrder(root);

			System.out.println("\n\nPre inOrder");
			tree.preOrder(root);

			System.out.println("\n\nPost inOrder");
			tree.postOrder(root);
	}

}

class Node{

	int key;
	Node leftchild,rightchild;

	Node(int key){
		this.key = key;
	}

	Node(Node n){
		this.key = n.key;
		this.leftchild = n.leftchild;
		this.rightchild = n.rightchild;
	}
}
