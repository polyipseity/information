---
aliases:
  - Errors.java
  - HKUST COMP3021 Errors.java
tags:
  - language/in/English
---

# `Errors.java`

- HKUST COMP 3021

This was used to revise for the final examination.

- source: [`Errors.java`](attachments/Errors.java)

```Java
import java.util.Arrays;
import java.util.function.Function;

public class Main {
 int asdefg = 1;

 public static void main(String... args) {
  new Main();
 }
}

public class Main2 {

}

protected class Main3 {

}

private class Main4 {

}

class Main5 {

}

static class Main6 {

}

class Cursed0 {
 public void dd() {
  new Cursed0();
 }

 static private class Cursed3213 {

 }

 public static void ddd() {
  new Cursed0();
 }
}

class Cursed1 {
 public static void main1(String[] args) {
  double radius;
  final double PI = 3.15169;
  double area = radius * radius * PI;
  System.out.println("Area is " + area);
 }

 public static void main2(String[] args) {
  double radius = 1;
  final double PI;
  double area = radius * radius * PI;
  System.out.println("Area is " + area);
 }

 public static void main3(String[] args) {
  Object radius;
  final double PI = 3.15169;
  radius.hashCode();
  System.out.println("Area is ");
 }

 public static void main4(String[] args) {
  Object radius = null;
  final double PI = 3.15169;
  radius.hashCode();
  System.out.println("Area is ");
 }

 public static void main5(String[] args) {
  double radius = 1;
  final double PI;
  double area = radius * radius;
  System.out.println("Area is " + area);
 }

 public static void main(String[] args) {
  C2 c2 = new C2();
  C3 c3 = new C3();
  C1 asdasd = new C4();
  synchronized (null) {
   System.out.println("a");
  }
  synchronized (1) {
   System.out.println("a");
  }
  synchronized ((Object) null) {
   System.out.println("a");
  }
  var a = "a" + null;
  c2 = (C2) ((C1) c3); // Here, the first compile-time error occurs because the class types Long and
             // Point are unrelated (that is, they are not the same, and neither is a
             // subclass of the other), so a cast between them will always fail.
 }

 void asdasd() {
  C4 final_c4 = new C4();
  C3 c3 = new C4();
  A asd = (A) c3;
  A asd3 = (A) final_c4;
  C3 asd2 = (C3) c3;
 }

 interface A {
 }

 static class C1 {
 }

 static class C2 extends C1 {
 }

 static class C3 extends C1 {
 }

 final static class C4 extends C3 {
 }

 /*
  * This section is devoted to a precise explanation of the word "reachable." The
  * idea is that
  * there must be some possible execution path from the beginning of the
  * constructor, method,
  * instance initializer, or static initializer that contains the statement to
  * the statement itself.
  * The analysis takes into account the structure of statements. Except for the
  * special treatment
  * of while, do, and for statements whose condition expression has the constant
  * value true,
  * the values of expressions are not taken into account in the flow analysis.
  */
 void unreachable() {
  while (true)
   ;
  int i = 1; // no
 }

 void unreachable2() {
  boolean a = true;
  while (a)
   ;
  int i = 1; // ok
 }

 void unreachable3() {
  while (true)
   ;
  int i = 1; // no
 }

 void unreachable4() {
  while (1 == 1)
   ;
  int i = 1; // no
 }

 public void unreachable5() {
  int a = 1;
  while (a == a)
   ;
  int i = 1; // ok
 }

 public void unreachable6() {
  final int a = 1;
  while (a == a)
   ;
  int i = 1; // not ok
 }

 private void unreachable7() {
  /*
   * A constant variable is a final variable of primitive type or type String that
   * is
   * initialized with a constant expression (§15.29). Whether a variable is a
   * constant
   * variable or not may have implications with respect to class initialization
   * (§12.4.1),
   * binary compatibility (§13.1), reachability (§14.22), and definite assignment
   * (§16.1.1).
   * 
   * Constant expressions are used as case labels in switch statements and switch
   * expressions (§14.11, §15.28) and have a special significance in assignment
   * contexts (§5.2)
   * and the initialization of a class or interface (§12.4.2). They may also
   * govern the ability of a
   * while, do, or for statement to complete normally (§14.22), and the type of
   * conditional
   * operator ? : with numeric operands.
   * 
   * true
   * (short)(1*2*3*4*5*6)
   * Integer.MAX_VALUE / 2
   * 2.0 * Math.PI
   * "The integer " + Long.MAX_VALUE + " is mighty big."
   */
  final int a = 2 / 0; // ArithmeticException
  while (a == a)
   ;
  int b = 1; // ok
 }

 private void asd() {
  try {
  } catch (Exception a) {
  } catch (RuntimeException a) {
  }
 }

 private void asd2() {
  try {
  } catch (Exception | RuntimeException a) {
  } catch (RuntimeException a) {
  }
 }

 private void asd3() {
  try {
  } catch (Throwable a) {
  }
  C1[] a = new C1[1];
  Arrays.sort(a);
  Integer.parseInt("a");
  throw new NumberFormatException();
 }

 private void asd4() {
  try {
  } catch (RuntimeException a) {
  } catch (IllegalArgumentException | IllegalStateException a) {
  }
 }

 private void asd5() {
  try {
  } catch (IllegalArgumentException | IllegalStateException a) {
  } catch (RuntimeException a) {
  }
 }
}

class Test {
 static int x = 0;

 Test(int x) {
  x = x + 1;
  System.out.println(x);
 }

 public static void main(String[] args) {
  System.out.println(new Test(1));
 }
}

class Test2 {
 static int x;

 Test2(int x) {
  int a = Test2.x;
  a = a + a;
  Test2.x = x + 1;
  System.out.println(x);
 }

 public static void main(String[] args) {
  System.out.println(new Test2(1));
 }
}

class Test3 {
 Test3(int x) {
  this.x = x + 1;
  System.out.println(x);
 }

 public static void main(String[] args) {
  System.out.println(new Test3(1));
 }
}

class Arrayss {
 abstract class X {
  int a;
 }

 interface I {
  void foo();
 }

 class Q implements I {
  public void foo() {
  }
 }

 class Y extends X implements I {
  Y() {
  }

  public void foo() {
   X a;
   X b = new X();
   X c = new I();
   X d = new Y();
   I e;
   I f = new X();
   I g = new I();
   I h = new Y();
   X[] i;
   X[] j = new X[10];
   X[] k = new I[10];
   X[] l = new Y[10];
   I[] m;
   I[] n = new X[10];
   I[] o = new I[10];
   I[] p = new Y[10];
   p[0] = new Q();
  }

 }
}

abstract class Cursed3 {
 abstract public void foo();
}

class Cursed4 extends Cursed3 {
 Cursed4() {
 }

 void foo() {
 }
}

interface Cursed5 {
 void a();

 int a();

 void b();

 void c();

 static private void d() {
 }

 static protected void e() {
 }

 default int f() {
  return 1;
 }

 static void g() {
 }

 static void h() {
 }
}

class Test6 {
 int i, j;

 public void foo() throws Exception {
  this.i = this.i / this.j;
 }
}

class Cursed12 {
 class c1 {
 }

 class c2 {
 }

 interface i1 {
 }

 interface i2 {
 }

 class A extends c2 implements i1 {
 }

 class F implements i1, i2 {
 }
}

class Cursed13 {
 class A {
  public String show(D obj) {
   return ("A and D");
  }

  public String show(A obj) {
   return ("A and A");
  }
 }

 class B extends A {
  public String show(B obj) {
   return ("B and B");
  }

  public String show(A obj) {
   return ("B and A");
  }
 }

 class C extends B {
 }

 class D extends B {
 }

 public class OMG {
  public static void main(String[] args) {
   Cursed13 asd = new Cursed13();
   A a = asd.new B(); // Be careful: a is new B()
   B b = asd.new B();
   C c = asd.new C();
   D d = asd.new D();
   System.out.println(a.show(a));
   System.out.println(a.show(b));
   System.out.println(a.show(c));
   System.out.println(a.show(d));
  }
 }
}

@FunctionalInterface
interface LambdaFunction {
 int apply(int j);

 boolean equals(Object o); // ??
}

class AP {
 static class A {
  int x;

  public boolean equals(A obj) {
   return this.x == obj.x;
  }
 }

 public static class HelloWorld {
  public static void main(String[] args) {
   Object a1 = new A();
   Object a2 = new A();
   System.out.println(a1 == a2); // false
   System.out.println(a1.equals(a2)); // true?
  }
 }
}

class Asd {
 static class AA {
  public AA(String a) {
   System.out.println(a);
  }
 }

 static class AB {
  private final AA a;
  private final AA b = new AA("b");

  public AB() {
   final int i = 1;
   if (i == i) {
    this.a = new AA("a");
   }
  }
 }

 static class BB {
  private final AA c;
  private final AA d = new AA("d");

  public BB() {
   this.c = new AA("c");
  }

  static strictfp public void main(String args[]) {
   new BB();
  }
 }
}

class Lambdas {
 interface A {
  void a();
 }

 interface B {
  void b(Object a, int _a);
 }

 interface C {
  void c(Object b, Object c);
 }

 public static void something(String... args) {
  A _ = () -> {
  };
  A a = () -> {
  };
  B b = (Object asd, int asdasd) -> {
  };
  B e = (Object asd, int asdasd) -> System.out.println();
  B d = (asd, int asdasd) -> System.out.println();
  B f = (Object asd, asdasd) -> System.out.println();
  B g = (Object asd, Integer asdasd) -> System.out.println();
  var aa = 1;
  A aaa = () -> {
   aa = aa;
  };
  var bb = 123;
  A aab = () -> {
   int aaa = bb;
  };
  bb++;
  final var cc = 123;
  A aac = () -> {
   int aaa = cc;
  };
  var dd = 123;
  A aad = () -> {
   int aaa = dd;
  };
  new Object() {
   public void aa() {
    int asd = dd;
   }
  };
  {
   A bbde = () -> {
   };
  }
  bbde;
  {
   A bbde = () -> {
   };
   A aac = () -> {
   };
  }
 }
}

class Nested {
 static enum Nested2 {
  ;

  static interface AA3 {
   static interface AAAA {
    static class ABBB {

    }
   }
  }
 }

 static class A {

 }

 class AAA {
 }
}

class Others {

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
   private static AA c;
   private AA d;
   private final AA a;

   public AB() {
    final int i = 1;
    if (i == i) {
     this.a = new AA("a");
    }
    assert true : "a";
    assert true : new Object();
    assert true : null;
    assert false : false;
    assert true : 1;
    assert 1 == 1;
    assert false;
    int sdi = 1;

    switch (3) {
     case 1:
     case 2:
      break;
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

  interface BBC {
   static int omg = 1;
   static int aaaaaaaaa = 1;
   static final int aaaaaa = 1;
   private static int asdadsadsdad = 123123;
   protected static final int asdadsadsdaddddd = 123123;

   private void a() {
   }

   protected void aa() {
   }

   public void aaa() {
    a();
   }

   public default void asd() {
   }
  }

  interface BBD {
   static int omg = 1;
  }

  interface BBBBB extends BBC, BBD {
   static int omg = 1;
  }

  class AAAA implements BBBBB {

   @Override
   protected void aa() {
    super.aa();
    ((Function) (Object a) -> 1).apply(1);
    ((Function<Integer, Integer>) a -> 1).apply(1);
    ((Function<Integer, Integer>) (Integer a) -> 1).apply(1);
    ((Function<Integer, Integer>) (int a) -> 1).apply(1);
    BBBBB a = (Object & BBBBB) null;
    new AAAA() {
     public void Object() {

     }
    }.Object();
    ((Object & BBD & Runnable) () -> {
    }).run();
   }

   public AAAA() {
   }

   public void AAAA() {
    new AAAA().AAAA();
   }

   @Override
   public void aaa() {

   }
  }

  class AAAAsdsada extends AA {

   public AAAAsdsada(String a) {
    super(a);
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

   private static void bb() {
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
    if (this.e instanceof Object e) {

    }
    if (this.e instanceof AA e) {

    }
    if (this.e instanceof AA) {

    }
    if (this.e instanceof AAAAsdsada) {

    }
    if (this.e instanceof AAAAsdsada aa) {

    }
    if (this.e instanceof BB a) {

    }
    if (this.e instanceof AB) {

    }
    if (this.e instanceof AB e) {

    }
    if ((AB) this.e instanceof AB) {

    }
    if ((AA) null instanceof AB) {

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
}

class Generics {
 public static class A {
  void asd(Object a) {
  }
 }

 public class B<T extends Integer> extends A {
  void asd(T a) {
  }
 }

 {
  B<Integer> a = new B<>();
 }
}

class Ex<T> extends Exception {

}

class AA<T> {
 public strictfp <T extends Number> void asd() {
  <T>asd();
  this.asd();
  this.<T>asd();
  this.<>asd();
  this.<Number>asd();
  this.<Integer>asd();
 }
}
```
