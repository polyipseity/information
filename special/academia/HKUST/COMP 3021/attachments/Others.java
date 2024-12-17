public class Others {
}

class Asd2 { // clash with Asd
	static class AA {
		public AA(String a) {
			System.out.println(a);
		}
	}

	static class SuperCursed {
		private AA c;

		private void aa() {
		}
	}

	static class AB extends SuperCursed {
		private AA c;
		private AA d;
		private final AA a;

		public AB() {
			final int i = 1;
			if (i == i) {
				this.a = new AA("a");
			}
		}

		private final AA b = new AA("b");

		private void aa() {
		}

		protected static void bb() {
		}

		protected static void bc() {
		}

		private static void bd() {
		}
	}

	static class BB extends AB {
		private final AA c;
		private final AA f = new AA("f");

		public BB() {
			this.c = new AA("c");
			AA c = super.c;
			bc();
			super.bc();
		}

		protected static void bc() {
			AB.bc();
		}

		private static void bd() {
		}

		{
			this.e = new AA("e");
			if (this.e instanceof Object) {

			}
		}

		private final AA d = new AA("d");
		private final AA e;

		static strictfp public void main(String args[]) {
			new BB();
		}
	}

	static class CB extends BB {

	}
}
