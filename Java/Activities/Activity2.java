package Training;

public class Activity2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = { 10, 77, 10, 54, -11, 10 };

		int temp = 0;
		for (int i = 0; i < arr.length; i++)

		{

			if (arr[i] == 10) {
				temp = temp + arr[i];

			}
		}
		System.out.println(temp);
		if (temp == 30) {
			System.out.println(true);

		}
	}

}
