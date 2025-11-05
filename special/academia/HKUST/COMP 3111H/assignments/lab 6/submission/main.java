package comp3111.labs.lab6;

/*
 * note the bad coding style (deliberately written for debugging exercise)
 */
public class main {
	public static void main(String[] args) {
		Animal animals[] = new Animal[10];

		/*
		The old code:

		```Java
		for (Animal a : animals)
			a = new Animal();
		```

		`animals` is initialized as a new `Animal` array, which holds `null` for all of its elements initially.
		The old code wants to initialize each element of the array so that `animals` contains a new object `Animal`
		for all of its elements. However, the code does not work because it creates a new `Animal` and
		assigns it to the local variable `a`. Assigning to the local variable `a` does not cause
		the corresponding element in the array `animals` to be actually assigned the new `Animal`.
		As a result, after running the old code, `animals` is not modified at all, and all of
		its elements are still `null`.

		However, the above does not cause the error directly. The direct cause of the error is in the
		later parts of the code, where elements of the array `animals` are accessed, and then methods
		of `Animals` are called using the elements. As all elements are `null`, this means we are
		calling a method on an instance of `null`, which causes `NullPointerException`. The first
		occurrence is `animals[iii].isAlive()`, which causes the error.

		The fix is to initialize elements of the array `animals` properly. The following code
		correctly create a new `Animal` for each element of the array:

		```Java
		for (int ii = 0; ii < animals.length; ++ii) {
			animals[ii] = new Animal();
		}
		```

		Then, after running the code, each element of the array is nonnull, so
		all code after the code will not encounter `NullPointerException`, as
		`animals[iii]` is always nonnull.
		*/
		for (int ii = 0; ii < animals.length; ++ii) {
			animals[ii] = new Animal();
		}

		for (int iii = 0; iii < 10; iii++) {
			int ii = 0;
			for (; ii < 100 && animals[iii].isAlive(); ii++) {
				System.out.print(animals[iii].getWeight() + " ");
				animals[iii].eat();
				if (ii % 3 == 0)
					animals[iii].poo();
			}
		}
	}
}
