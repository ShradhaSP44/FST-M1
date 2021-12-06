package Training;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Activity3 {

	public static void main(String[] args) {

		
		Scanner in = new Scanner(System.in);
		System.out.println("Enter age In sec:-");
		double ageInSec = in.nextDouble();
		in.close();
		
		int earth = 31557600;
		double mercury = (0.2408467) * earth;
		double venus = 0.61519726 * earth;
		double mars = 1.8808158 * earth;
		double ven = 11.862615 * earth;
		double jup = 29.447498 * earth;
		double uranus = 84.016846 * earth;
		double neptune = 164.79132 * earth;
		double age;
		age = (ageInSec / earth);
		System.out.println("age =" + Math.abs(age));

	}

}
